<!--Title Image-->
![certificate generator banner_1.gif](https://github.com/jeanjusten/CS50P_Python_Final_Project/blob/main/certificate%20generator%20banner_1.gif?raw=true)

 # :minidisc: CERTIFICATE GENERATOR v.1.0
Welcome to the PDF Certificate Generator!
With this program you'll be able to generate a PDF certificate for a list of students.
Check out the ***Table of Contents*** section to navigate through this documentation.

## :large_orange_diamond: Table of Contents
- [1. Introduction](#large_orange_diamond-introduction)
  - [1.1 Description](#arrow_forward-description)
  - [1.2 Functions](#arrow_forward-functions)
  - [1.3 Libraries](#arrow_forward-libraries)
  - [1.4 Additional Info](#arrow_forward-additional-info)
- [2. Video Demo](#large_orange_diamond-video-demo)
  - [2.1 Youtube](#arrow_forward-youtube)
  - [2.2 Streamable](#arrow_forward-streamable)
- [3. Requirements](#large_orange_diamond-requirements)
  - [3.1 Install Requirements](#arrow_forward-install-requirements)
  - [3.2 Other Requirements](#arrow_forward-other-requirements)
- [4. How to Use](#large_orange_diamond-how-to-use)
  - [4.1 Getting Started](#arrow_forward-getting-started)
  - [4.2 Navigating](#arrow_forward-navigating)
  - [4.3 List Consulting](#arrow_forward-list-consulting)
  - [4.4 List Adding](#arrow_forward-list-adding)
  - [4.5 Generating a Certificate](#arrow_forward-generating-a-certificate)
  - [4.6 Exiting the Program](#arrow_forward-exiting-the-program)
  - [4.7 Customizing](#arrow_forward-customizing)
- [5. Links](#large_orange_diamond-links)
  - [5.1. Project Repository](#arrow_forward-project-repository)
  - [5.2. Social Links](#arrow_forward-social-links)
  - [5.3. Libraries Links](#arrow_forward-libraries-links)
- [6. Etcetera](#large_orange_diamond-etcetera)
  - [6.1 About](#arrow_forward-about)
  - [6.2 License](#arrow_forward-license)

## :large_orange_diamond: Introduction
### :arrow_forward: Description
Certificate Generator is a simple python based program that allows you to make a certificate in PDF format, branding a student name and desired date to the outputed file.<br>

The program takes a CSV(comma separated values) file containing the name and grade of a student and, if he is qualified, outputs a certificate with the student's name and current(or any other) date.

### :arrow_forward: Functions
Other than main function, Certificate Generator runs on other functions as well.<br>

- ***is_qualified***(_grade_):
This function takes a student grade as an argument, and automatically calculates whether or not the student is qualified to receive a certificate. The grade threshold default value is **70** and it can be changed by modifiying the ***"grade_threshold"*** variable value on the code.<br>
After the user inserts a name for the student, he will be prompted to insert a grade. This grade will be passed to the _is_qualified()_ function and will output **"Qualified"**, or **"Not qualified"** in the CSV file. In this example, we will assign a grade of **95** for a stundent called Harry:

        grade = 95
        is_qualified(grade)


    **The output in the CSV file should be:**

        Student,Grade,Qualified
        Harry,95,Qualified
  

- ***spacing***(_string, color_):
The purpose of ***spacing()*** is to manage the spacing between outputs and the main-menu, and print out program messages and alerts. It takes the string that is going to be formated and printed as its first argument, and the color of it(Default value is _"bright_white"_) as the second argument. The color options for customization can be acessed at [Rich Documentation](https://rich.readthedocs.io/en/stable/appendix/colors.html).
<br>

**In this example:**

    spacing("Hello, World!", "red1")

**The output would be: (In the color RED)** <br>

<span style="color:red">
 
    =============================================
    • Hello, World!
    =============================================
        
</span><br>


- ***plot_certificate***(_student, date_):
This function takes a student name as its first argument, a date as its second argument and then prints them out in the certificate sample specified. All the styling such as PDF format, orientation, font styling and printing position can be customized by modifying the code in this function. To see more on customization, visit the [4.7 Customizing](#arrow_forward-customizing) section.

<br>

- ***list_size***(_list, header_):
This function takes a list as its first argument, and a str as its second. It then returns a formated string with the header name, followed by the list length.


      list1 = ["Draco", "Crabbe", "Goyle"]

      list_size(list1, "Mocking List")

    **Output result:**

      "Mocking List - 3 students found"


- ***new_student***(_name_):
The _"new_student()"_ function acts as a formating tool for a new student name added to the list. It takes a student's name for argument and strips any aditional (or accidental) whitespaces in both start and end of the name, and it also title-case the student's name.

      name = "  harry potter  "

      name = new_student(name)

    **Outuput result:**

      name = "Harry Potter"


### :arrow_forward: Libraries
Certificate Generator uses a few Libraries that allow the program to run its core functions and enhance the user interface for a better experience. The libraries used are:

- **fpdf2:**
Used for the program's core function: to generate a PDF based on a image sample and print a student name and date on it.

- **Tabulate:**
Used for formating the main-menu, and therefore presenting the user with a better, very intuitive and friendly UI.

- **Rich:**
Used in every printing you see in the program. It gives colors to the main-menu and output messages and commands.



### :arrow_forward: Additional Info
Although this version of the program outputs a pre-made certificate model **("certificate-sample.png")**, you can add your own certificate design to be outputed instead. The same is true for the grading system, which uses **70** as the grade threshold by default.<br>
Check out **[4.7 Customizing](#arrow_forward-customizing)** section for more info on how to customize the code.

## :large_orange_diamond: Video Demo
View the project in action.

### :arrow_forward: Youtube
Watch it on Youtube
<https://youtu.be/09MscpB8rF8>

### :arrow_forward: Streamable
Watch it on Streamable
<https://streamable.com/o6ryg4>

## :large_orange_diamond: Requirements
<p>Below, are the requirements listed for you to test this program.</p>

### :arrow_forward: Install Requirements
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

### :arrow_forward: Other Requirements
You will need a CSV file called **"students_list.txt"** on the root folder. The file could contain student data or be completely empty.<br>
The last requirement is a PNG sample of the certificate called **"certificate-sample.png"**, which must be on the root folder as well.

Both aditional files are included in the project repository. Check out [Certificate Generator's GitHub Repository](https://github.com/jeanjusten/CS50P_Python_Final_Project) if you want to download them.

## :large_orange_diamond: How to Use
### :arrow_forward: Getting Started
To start the program, open your terminal and enter the command:

    python project.py

### :arrow_forward: Navigating
After the program starts running you will be presented to the main menu, where you are prompted to insert your command.<br>

* Enter **1** to check your students list.<br>
* Enter **2** to add a new student to the list.<br>
* Enter **3** to generate a certificate.<br>
* Enter **4** to terminate the program.<br>

Any other value in the prompt will result in a error and the system will reprompt the user for a valid input.

### :arrow_forward: List Consulting
By entering **"1"** in the main menu, the complete list will be displayed in your terminal.<br>
The command prints all the students, one per line, with the following elements:<br>

* **Student ID**¹
* **Student Name**
* **Student Grade**
* **Student Qualification**²

¹ _The Student ID is given to the list based on the python's "***enum()***" function._<br>
² _The Student Qualification represents whether the student is qualified to receive a certificate or not. This element is automatically calculated based on the grade threshold (default value is **70**) of the **"is_qualified()"** function_<br>

### :arrow_forward: List Adding
By entering **"2"** in the main menu, you will be able to add a new student to your list.<br>The Program will prompt you for a student name first, and then a grade³.<br>
If the input format is correct, the CSV file will automatically be updated.<br>

³ _The grade value must be in the **0-100** range, or the user will be reprompted._

### :arrow_forward: Generating a Certificate
By entering **"3"** in the main menu, you will be able to generate a certificate.<br>
The complete students list will be printed in the terminal, with the qualified students being printed green, and the unqualified students being printed red. The program will then prompt the user for a student ID.<br>

- If the user inserts a valid ID⁴, the program will now prompt for a date⁵.<br>
After this, the certificate will be created in the root folder and a success message will be displayed in your terminal.

⁴ _The user must insert a valid student ID. Trying to insert a ID that are not in the list, or inputing a out-of-range value, will result in a error and the user will be sent back to the main menu._<br>
⁵ _The date can be set in any format the user chooses, as its registered as a **str**._

### :arrow_forward: Exiting the Program
By entering **"4"** in the main menu, the program will be terminated.<br>
Note that you can force-exit the program at any time by typing **CTRL+C** in your terminal.

### :arrow_forward: Customizing
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

## :large_orange_diamond: Links
### :arrow_forward: Project Repository
* [Certificate Generator's GitHub Repository](https://github.com/jeanjusten/CS50P_Python-Final-Project)

### :arrow_forward: Social Links
* [Jean Justen's Github page](https://github.com/jeanjusten)
* [Jean Justen's LinkedIn page](https://www.linkedin.com/in/jeanjusten/)

### :arrow_forward: Libraries Links
* [fpdf2 documentation](https://pypi.org/project/fpdf2/)
* [Tabulate documentation](https://pypi.org/project/tabulate/)
* [Rich documentation](https://rich.readthedocs.io/en/stable/introduction.html)

## :large_orange_diamond: Etcetera
### :arrow_forward: About
<p>The Certificate Generator is a program developed by Jean Justen, and it was made as a final project for "CS50's Introduction with Python" course. The program's purpose is to put in use the many tools and concepts learned in the CS50P's Introduction to Python 9 weeks' course.<br>

### :arrow_forward: License
You may use, copy, share and modify the code as you please. No credits needed.</p>
