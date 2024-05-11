 ___
 # CERTIFICATE GENERATOR v.1.0
Welcome to the PDF Certificate Generator!
With this program you'll be able to generate a PDF certificate for a list of students.
Check out the ***Table of Contents*** section to navigate through this documentation.
___
## Table of Contents
* [1. Introduction](#1.-Introduction)
    - [1.1 Description](#1.1-Description)
    - [1.2 Functions](#1.2-Functions)
    - [1.3 Libraries](#1.2-Libraries)
    - [1.4 Additional Info](#1.4-Additional-Info)
* [2. Video Demo](#2.-Video-Demo)
    - [2.1 Youtube](#3.1-Youtube)
    - [2.2 Streamable](#3.2-Streamable)
* [3. Requirements](#3.-Requirements)
    - [3.1 Install Requirements](#3.1-Install-Requirements)
    - [3.2 Other Requirements](#3.2-Other-Requirements)
* [4. How to Use](#4.-How-to-Use)
    - [4.1 Getting Started](#4.1-Getting-Started)
    - [4.2 Navigating](#4.2-Navigating)
    - [4.3 List Consulting](#4.3-List-Consulting)
    - [4.4 List Adding](#4.4-List-Adding)
    - [4.5 Generating a Certificate](#4.5-Generating-a-Certificate)
    - [4.6 Exiting the Program](#4.6-Exiting-the-Program)
    - [4.7 Customizing](#4.7-Customizing)
* [5. Links](#5.-Links)
    - [5.1. Project Repository](#5.1-Project-Repository)
    - [5.2. Social Links](#5.2-Social-Links)
    - [5.3. Libraries Links](#5.3-Libraries-Links)
* [6. Etcetera](#6.-Etcetera)
    - [6.1 About](#6.1-About)
    - [6.2 License](#6.2-License)
___
## 1. Introduction
### 1.1 Description
Certificate Generator is a simple python based program that allows you to make a certificate in PDF format, branding a student name and desired date to the outputed file.<br>

The program takes a CSV(comma separated values) file containing the name and grade of a student and, if he is qualified, outputs a certificate with the student's name and current(or any other) date.

### 1.2 Functions
Other than main function, Certificate Generator runs on other functions as well.<br>

- ***is_qualified***(_grade_):
This function takes a student grade as an argument, and automatically calculates whether or not the student is qualified to receive a certificate. The grade threshold default value is **70** and it can be changed by modifiying the ***"grade_threshold"*** variable value on the code.<br>
After the user inserts a name for the student, he will be prompted to insert a grade. This grade will be passed to the _is_qualified()_ function and will output **"Qualified"**, or **"Not qualified"** in the CSV file. In this example, we will assign a grade of **95** for a stundent called Harry:

        grade = 95
        is_qualified(grade)


    **The output in the CSV file should be:**

        Student,Grade,Qualified
        Harry,95,Qualified
<br>

- ***spacing***(_string, color_):
The purpose of ***spacing()*** is to manage the spacing between outputs and the main-menu, and print out program messages and alerts. It takes the string that is going to be formated and printed as its first argument, and the color of it(Default value is _"bright_white"_) as the second argument. The color options for customization can be acessed at [Rich Documentation](https://rich.readthedocs.io/en/stable/appendix/colors.html).
<br>

    **In this example:**

        spacing("Hello, World!", "red1")

    **The output would be:**<br>
<span style="color:red">
        =============================================<br>
        • Hello, World!<br>
        =============================================<br>
</span><br>


- ***plot_certificate***(_student, date_):
This function takes a student name as its first argument, a date as its second argument and then prints them out in the certificate sample specified. All the styling such as PDF format, orientation, font styling and printing position can be customized by modifying the code in this function. To see more on customization, visit the [4.7 Customizing](#4.7-Customizing) section.

<br>

- ***list_size***(_list, header_):
This function takes a list as its first argument, and a str as its second. It then returns a formated string with the header name, followed by the list length.


        list1 = ["Draco", "Crabbe", "Goyle"]

        list_size(list1, "Mocking List")

    **Output result:**

        "Mocking List - 3 students found"

<br>

- ***new_student***(_name_):
The _"new_student()"_ function acts as a formating tool for a new student name added to the list. It takes a student's name for argument and strips any aditional (or accidental) whitespaces in both start and end of the name, and it also title-case the student's name.

        name = "  harry potter  "

        name = new_student(name)

    **Outuput result:**

        name = "Harry Potter"


### 1.3 Libraries
Certificate Generator uses a few Libraries that allow the program to run its core functions and enhance the user interface for a better experience. The libraries used are:

- **fpdf2:**
Used for the program's core function: to generate a PDF based on a image sample and print a student name and date on it.

- **Tabulate:**
Used for formating the main-menu, and therefore presenting the user with a better, very intuitive and friendly UI.

- **Rich:**
Used in every printing you see in the program. It gives colors to the main-menu and output messages and commands.



### 1.4 Additional Info
Although this version of the program outputs a pre-made certificate model **("certificate-sample.png")**, you can add your own certificate design to be outputed instead. The same is true for the grading system, which uses **70** as the grade threshold by default.<br>
Check out **[4.7 Customizing](#4.7-Customizing)** section for more info on how to customize the code.
___
## 2. Video Demo
View the project in action.

### 2.1 Youtube
Watch it on Youtube
<https://youtu.be/09MscpB8rF8>

### 2.2 Streamable
Watch it on Streamable
<https://streamable.com/o6ryg4>

___
## 3. Requirements
<p>Below, are the requirements listed for you to test this program.</p>

### 3.1 Install Requirements
* ### Python<br>
To run Certificate Generator, you'll need Python to be downloaded and installed in your computer.
[Download Python latest version](https://www.python.org/downloads/)

* ### FPDF2<br>

You can install fpdf2 with the following command in your console:

    pip install fpdf2

* ### Tabulate<br>

You can install Tabulate with the following command in your console:

    pip install tabulate

* ### Rich<br>

You can install Rich with the following command in your console:

    pip install rich

### 3.2 Other Requirements
You will need a CSV file called **"students_list.txt"** on the root folder. The file could contain student data or be completely empty.<br>
The last requirement is a PNG sample of the certificate called **"certificate-sample.png"**, which must be on the root folder as well.

Both aditional files are included in the project repository. Check out [Certificate Generator's GitHub Repository]() if you want to download them.

___
## 4. How to Use
### 4.1 Getting Started
To start the program, open your terminal and enter the command:

    python project.py

### 4.2 Navigating
After the program starts running you will be presented to the main menu, where you are prompted to insert your command.<br>

* Enter **1** to check your students list.<br>
* Enter **2** to add a new student to the list.<br>
* Enter **3** to generate a certificate.<br>
* Enter **4** to terminate the program.<br>

Any other value in the prompt will result in a error and the system will reprompt the user for a valid input.

### 4.3 List Consulting
By entering **"1"** in the main menu, the complete list will be displayed in your terminal.<br>
The command prints all the students, one per line, with the following elements:<br>

* **Student ID**¹
* **Student Name**
* **Student Grade**
* **Student Qualification**²

¹ _The Student ID is given to the list based on the python's "***enum()***" function._<br>
² _The Student Qualification represents whether the student is qualified to receive a certificate or not. This element is automatically calculated based on the grade threshold (default value is **70**) of the **"is_qualified()"** function_<br>

### 4.4 List Adding
By entering **"2"** in the main menu, you will be able to add a new student to your list.<br>The Program will prompt you for a student name first, and then a grade³.<br>
If the input format is correct, the CSV file will automatically be updated.<br>

³ _The grade value must be in the **0-100** range, or the user will be reprompted._

### 4.5 Generating a Certificate
By entering **"3"** in the main menu, you will be able to generate a certificate.<br>
The complete students list will be printed in the terminal, with the qualified students being printed green, and the unqualified students being printed red. The program will then prompt the user for a student ID.<br>

- If the user inserts a valid ID⁴, the program will now prompt for a date⁵.<br>
After this, the certificate will be created in the root folder and a success message will be displayed in your terminal.

⁴ _The user must insert a valid student ID. Trying to insert a ID that are not in the list, or inputing a out-of-range value, will result in a error and the user will be sent back to the main menu._<br>
⁵ _The date can be set in any format the user chooses, as its registered as a **str**._

### 4.6 Exiting the Program
By entering **"4"** in the main menu, the program will be terminated.<br>
Note that you can force-exit the program at any time by typing **CTRL+C** in your terminal.

### 4.7 Customizing
This section will cover how you can customize the Certificate Generator to fit your needs.<br>

- On the top of the coding file, you will find two variables. One for the default value for the grading function, and the other for the certificate sample.

        #Customization
        grade_threshold = 70
        certificate_file = "certificate-sample.png"

- To change the PDF size and orientation, go under **"plot_certificate()"** function. Default for the size is "A4", and for the orientation is "Landscape".

        certificate.add_page(orientation ="landscape", format="A4")

- To style a new font and font size for the student name printed, you can change the values inside the quotation marks.

        certificate.set_font("Helvetica", size=44)
        certificate.set_font(style="B")

- You can do the same for the printed date.

        certificate.set_font("Times", size=26)
        certificate.set_font(style="B")

- Note that you can also change the position in which the program will print the student name and date by replacing the fpdf2 cell position values (Default position is middle-centered). You can check out how to use fpdf2 text cells with the [fpdf2 Documentation](https://py-pdf.github.io/fpdf2/PageFormatAndOrientation.html). The cell values are all under the **"plot_certificate()"** function

        certificate.cell(30,234,student,border=0,center="C",align="C")

___
## 5. Links
### 5.1 Project Repository
* [Certificate Generator's GitHub Repository]()

### 5.2 Social Links
* [Jean Justen's Github page](https://github.com/jeanjusten)
* [Jean Justen's LinkedIn page](https://www.linkedin.com/in/jeanjusten/)

### 5.3 Libraries Links
* [fpdf2 documentation](https://pypi.org/project/fpdf2/)
* [Tabulate documentation](https://pypi.org/project/tabulate/)
* [Rich documentation](https://rich.readthedocs.io/en/stable/introduction.html)

___
## 6. Etcetera
### 6.1 About
<p>The Certificate Generator is a program made by Jean Justen, and it was made as a final project for "CS50's Introduction with Python" course. The program was developed to put in use the many tools and concepts learned in the CS50P's Introduction to Python 9 weeks' course.<br>

### 6.2 License
You may use, copy, share and modify the code as you please. No credits needed.</p>
___
