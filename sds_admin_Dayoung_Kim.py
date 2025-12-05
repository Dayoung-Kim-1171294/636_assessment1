# ============== SELWYN DANCE SCHOOL SYSTEM ==============
# Student Name: Dayoung Kim
# Student ID : 1171294
# ================================================================
 
from datetime import datetime,timedelta,date     # datetime module is required for working with dates

# Make the variables and function in sds_data.py available in this code (without needing 'sds_data.' prefix)
from sds_data import students,classes,unique_id,display_formatted_row   

def calculate_age(birth_date, current_date=None):
    if current_date is None:
        current_date = date.today()
    
    age = current_date.year - birth_date.year
    
    # Adjust if birthday hasn't occurred yet this year
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age

def print_student_details(student, format_str):
    id = student[0]
    fname = student[1]
    famname = student[2]
    birthdate = student[3].strftime("%d %b %Y")
    grade = student[4]
    email = student[5]

    display_formatted_row([id,fname,famname,birthdate, grade, email],format_str)    

def list_all_students():
    format_str = "{: <5} {: <15} {: <15} {: <14} {: <6} {: <20}"   

    display_formatted_row(["ID","First Name","Family Name","Birth Date","Grade","e-Mail"],format_str)      
    print("-" * 85)    

    for student in students:
        print_student_details(student, format_str)

def list_students_and_classes():
    format_str = "{: <5} {: <15} {: <15} {: <14} {: <6} {: <20}"   

    for class_name in classes:
        print("")
        print(f"◉ Class: {class_name} ▶︎ {len(classes[class_name])} student(s)")

        # Handle case where no students are enrolled
        if len(classes[class_name]) == 0:
            continue

        display_formatted_row(["ID","First Name","Family Name","Birth Date","Grade","e-Mail"],format_str)      
        print("-" * 85)  

        # Sort by family name
        sorted_students = sorted(students, key=lambda x: x[2])
        
        # Loop through student IDs in the class
        for student_id in classes[class_name]:
            for student in sorted_students: 
                # Find student details by matching id
                if student[0] == student_id:
                    print_student_details(student, format_str)

def add_student_to_classes(student_id, grade, birthdate):
    age = calculate_age(birthdate)

    if grade >= 6:
        classes["Senior Dance"].append(student_id)
    elif grade == 5:
        classes["Bellbirds"].append(student_id)
    elif grade == 4:
        classes["Robins"].append(student_id)
    elif grade == 3:
        classes["Piwakawaka"].append(student_id)
    elif grade == 2:
        classes["Butterflies"].append(student_id)
    elif grade == 1:
        classes["Fireflies"].append(student_id)
    else:
        if age >= 12:
            classes["Bellbirds"].append(student_id)
        elif age >= 10:
            classes["Robins"].append(student_id)
        elif age >= 8.5:
            classes["Piwakawaka"].append(student_id)
        elif age >= 7:
            classes["Butterflies"].append(student_id)
        elif age >= 6:
            classes["Fireflies"].append(student_id)
        else:
            classes["Glowworms"].append(student_id)
            
# Helper function to validate a date
def get_valid_birthdate(year, month, day):
    try:
        year = int(year)
        month = int(month)
        day = int(day)
        birthdate = date(year, month, day)

        if birthdate > date.today():
            print(f"Invalid date: {birthdate} is in the future. Please try again.")
            return get_valid_birthdate(
                input("Enter Birth Year (YYYY): "),
                input("Enter Birth Month (1-12): "),
                input("Enter Birth Day (1-31): ")
            )
        else:            
            return birthdate
    except ValueError:
        print("Invalid date. Please enter a valid date.")
        return get_valid_birthdate(
            input("Enter Birth Year (YYYY): "),
            input("Enter Birth Month (1-12): "),
            input("Enter Birth Day (1-31): ")
        )

# Helper function to validate integer input
def get_valid_grade(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Cannot be negative. Please enter a valid number.")
            else:
                return value
        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a number.")

# Helper function to validate email input
def get_valid_email(prompt):
    while True:
        email = input(prompt)
        if "@" in email and "." in email:
            return email
        else:
            print("Invalid email format. Please enter a valid email address.")

def add_new_student():
    fname = input("Enter First Name: ")
    famname = input("Enter Family Name: ")
    birthyear = input("Enter Birth Year (YYYY): ")
    birthmonth = input("Enter Birth Month (1-12): ")
    birthday = input("Enter Birth Day (1-31): ")
    birthdate = get_valid_birthdate(birthyear, birthmonth, birthday)
    email = get_valid_email("Enter e-Mail Address: ")
    grade = get_valid_grade("Enter Grade (0-6+): ")
    new_id = unique_id()

    students.append([new_id, fname, famname, birthdate, grade, email])
    add_student_to_classes(new_id, grade, birthdate)
    print(f"Student {fname} {famname} added with ID {new_id}.")

def list_students_and_ages():
    format_str = "{: <5} {: <15} {: <15} {: <14}"   

    print("❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ Dancers Ages ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖".center(44))
    display_formatted_row(["ID","First Name","Family Name", "Age"],format_str)      
    print("-" * 44)    

    for student in students:
        id = student[0]
        fname = student[1]
        famname = student[2]
        age = calculate_age(student[3])

        display_formatted_row([id,fname,famname,age],format_str)   

def disp_menu():
    """
    Displays the menu and current date.  No parameters required.
    """
    print("==== WELCOME TO SELWYN DANCE SCHOOL SYSTEM ===")
    print(" 1 - List Students")
    print(" 2 - List Students and their Classes")
    print(" 3 - List Students and their Ages")
    print(" 4 - Not Implemented")
    print(" 5 - Not Implemented")
    print(" 6 - Add New Student")
    print(" X - eXit (stops the program)")


# ------------ This is the main program ------------------------

# Don't change the menu numbering or function names in this menu.
# Although you can add arguments to the function calls, if you wish.
# Repeat this loop until the user enters an "X" or "x"
response = ""
while response.upper() != "X":
    disp_menu()
    # Display menu for the first time, and ask for response
    response = input("Please enter menu choice: ")    
    print("")   # Print a blank line for spacing
    if response == "1":
        list_all_students()
    elif response == "2":
        list_students_and_classes()
    elif response == "3":
        list_students_and_ages()
    elif response == "4":
        pass
    elif response == "5":
        pass
    elif response == "6":
        add_new_student()
    elif response.upper() != "X":
        print("\n*** Invalid response, please try again (enter 1-6 or X)")

    print("")

print("\n=== Thank you for using the SELWYN DANCE SYSTEM! ===\n")

