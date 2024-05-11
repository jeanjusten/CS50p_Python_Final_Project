# ========================================================================================
# CERTIFICATE GENERATOR
# CS50p's Introduction to Programming with Python - Final Project
# Github: /jeanjusten  || edX: /jeanjusten
# ========================================================================================

from fpdf import FPDF
from tabulate import tabulate
from rich.console import Console
import csv
import sys

# ========================================================================================
# FUNCTIONS
# ========================================================================================
# Function that formats a header with the number of students found in a file and prints it as a header for the list
def list_size(list, header):
    return f"{header} - {len(list)} students found"

def new_student(name):
    return str(name).title().strip()

# Function that checks if the student has a grade high enough to qualify for a certificate
def is_qualified(grade):
    grade_threshold = 70 # This is the minimum value needed for a student be qualified for a certificate
    if grade >= grade_threshold:
        return "Qualified"
    else:
        return "Not qualified"

# Function for spacing and formating printed lines
def spacing(string,color="bright_white"):
    console = Console()
    print("\n")
    console.print(f"[{color}]=============================================")
    console.print(f"[{color}]• {string}")
    console.print(f"[{color}]=============================================")

# Function for PDF certificate settings and certificate output
def plot_certificate(student, date):
    certificate_file = "certificate-sample.png" # Change this value if you want to use your own certificate design
    # Using a design sample in A4 format / Landscape orientation
    certificate_sample = certificate_file
    certificate = FPDF()
    certificate.set_page_background(certificate_sample)
    certificate.add_page(orientation ="landscape", format="A4")
    # Adding student name to certificate
    certificate.set_font("Helvetica", size=44)
    certificate.set_font(style="B")
    certificate.set_text_color(0, 0, 0)
    # Adding date to certificate
    certificate.cell(30,234,student,border=0,center="C",align="C")
    certificate.set_font("Times", size=26)
    certificate.set_font(style="B")
    certificate.set_y(165)
    certificate.cell(116,20,date,border=0,align="C")
    # Outputing the PDF file
    file_name = f"certificate_{student}.pdf"
    certificate.output(file_name)

# ========================================================================================
# MAIN PROGRAM
# ========================================================================================
def main():
    console = Console()
    students = []
    file = "students_list.txt"

    # Reading the file and storing its values on students list
    with open(file,"r") as before_file:
        before_info = csv.DictReader(before_file)
        for line in before_info:
            st_name = line["Name"]
            st_grade = line["Grade"]
            st_qualified = is_qualified(float(line["Grade"]))
            students.append({"Name":st_name.title(),"Grade":st_grade,"Qualified":st_qualified})

    # Main Menu
    program_name = [{"★ CS50 FINAL PROJECT": "CERTIFICATE GENERATOR","developed by":"Jean Justen","Version":"V1.0"}]
    main_menu = [
        {"OPTION": "1", "DESCRIPTION": "Check students list"},
        {"OPTION": "2", "DESCRIPTION": "Add student to the list"},
        {"OPTION": "3", "DESCRIPTION": "Create a student certificate"},
        {"OPTION": "4", "DESCRIPTION": "Exit Program"},]

    print("\n")
    tabulated_name = tabulate(program_name, headers="keys", tablefmt="heavy_grid")
    tabulated_menu = tabulate(main_menu, headers="keys", tablefmt="heavy_grid")
    console.print(f"[dark_orange3]{tabulated_name}")

    while True:
        console.print(f"[orange1]{tabulated_menu}")
        user_input = int(input("Please select a option: "))

        if user_input not in (1,2,3,4):
            spacing("Invalid command input","red1")

        # 1) Check students
        elif user_input == 1:
            st_list_header = list_size(students, "STUDENTS LIST")
            spacing(st_list_header, "grey93")
            for i, student in enumerate(students):
                console.print(f"[bright_white]||ID: {i+1}|| {str(student["Name"]).lstrip().title()} || Grade: {str(student["Grade"]).strip(" ")} || {student["Qualified"]} for a certificate")
            print("\n")

        # 2) Add a new student
        elif user_input == 2:
            nst_name = new_student(input("Insert student's name: "))
            while True:
                try:
                    nst_grade = float(input("Insert student's grade: "))
                    if 0 <= nst_grade <= 100:
                        break
                    else:
                        spacing("Please insert a grade value between 0-100","red1")
                except ValueError:
                    spacing("Please insert a correct grade format","red1")

            nst_qualified = is_qualified(nst_grade)
            students.append({"Name":nst_name,"Grade":nst_grade,"Qualified":nst_qualified})
            # Updating the CSV file
            with open(file, "w") as new_file:
                after_info = csv.DictWriter(new_file, fieldnames=["Name","Grade","Qualified"])
                after_info.writeheader()
                for row in students:
                    after_info.writerow(row)
            spacing("Student was successfully added to the list","chartreuse3")

        # 3) Plot a Student Certificate
        elif user_input == 3:
            try:
                spacing("STUDENTS LIST", "grey93")
                for i, student in enumerate(students):
                    if student["Qualified"] == "Qualified":
                        console.print(
                            f"[chartreuse1]||ID: {i+1}|| {str(student["Name"]).lstrip().title()} || Grade: {str(student["Grade"]).strip(" ")} || {student["Qualified"]} for a certificate")
                    else:
                        console.print(
                            f"[red1]||ID: {i+1}|| {str(student["Name"]).lstrip().title()} || Grade: {str(student["Grade"]).strip(" ")} || {student["Qualified"]} for a certificate")
                print("\n")
                student_input = int(input("Insert the student ID to receive a certificate: "))

                if student_input > len(students) or student_input == 0:
                    spacing("Student ID does not exist", "red1")
                else:
                    for i, student in enumerate(students):
                        if student_input == (i+1):
                            if student["Qualified"] == "Qualified":
                                certificate_date = (input("Insert the current date for the certificate: "))
                                plot_certificate(str(student["Name"]), certificate_date)
                                spacing("The certificate was created successfully","chartreuse1")
                            else:
                                spacing("Student not qualified for certificate","red1")
            except ValueError:
                spacing("Please insert a valid student ID", "red1")

        elif user_input == 4:
            sys.exit(spacing("Program terminated", "red1"))

if __name__ == "__main__":
    main()
