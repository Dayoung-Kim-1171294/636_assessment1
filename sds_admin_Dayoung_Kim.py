# ============== SELWYN DANCE SCHOOL SYSTEM ==============
# Student Name: Dayoung Kim
# Student ID : 1171294
# ================================================================
 
from datetime import date     # datetime module is required for working with dates

# Make the variables and function in sds_data.py available in this code (without needing 'sds_data.' prefix)
from sds_data import students,classes,unique_id,display_formatted_row   


def calculate_age(birth_date:date, current_date=None):
    if current_date is None:
        current_date = date.today()
    
    age = current_date.year - birth_date.year
    
    # Adjust if birthday hasn't occurred yet this year
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age

def print_student_details(student:list, format_str:str):
    id = student[0]
    fname = student[1]
    famname = student[2]
    birthdate = student[3].strftime("%d %b %Y")
    grade = student[4]
    email = student[5]

    display_formatted_row([id,fname,famname,birthdate, grade, email],format_str)    

def list_all_students():
    format_str = "{: <5} {: <15} {: <15} {: <14} {: <6} {: <20}"   
    print("- All Student -".center(90))
    print("")

    display_formatted_row(["ID","First Name","Family Name","Birth Date","Grade","e-Mail"],format_str)      
    print("-" * 85)    

    for student in students:
        print_student_details(student, format_str)


def list_students_and_classes():
    format_str = "{: <5} {: <15} {: <15} {: <14} {: <6} {: <20}"   

    print("- Students by Classes -".center(84))
        
    # Sort by family name
    sorted_students = sorted(students, key=lambda x: x[2])
    
    for class_name in classes:
        print("")
        print(f"{class_name}: {len(classes[class_name])} student(s)")

        # Handle case where no students are enrolled
        if len(classes[class_name]) == 0:
            continue

        display_formatted_row(["ID","First Name","Family Name","Birth Date","Grade","e-Mail"],format_str)      
        print("-" * 85)  
        
        # Loop through student IDs in the class
        for student_id in classes[class_name]:
            for student in sorted_students: 
                # Find student details by matching id
                if student[0] == student_id:
                    print_student_details(student, format_str)

# Add student to class based on grade and age
def add_student_to_classes(student_id:int, grade:int, birthdate:date):
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
        """
        If grade 0, assign based on age
        Fix the problems identified by the School staff: age cut-offs for classes
        """
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
def get_valid_birthdate(year:str, month:str, day:str):
    try:
        year = int(year)
        month = int(month)
        day = int(day)
        birthdate = date(year, month, day)

        # Check if the date is in the future
        if birthdate > date.today():
            print(f"⚠️  Invalid date: {birthdate} is in the future. Please try again.")
            # Prompt user again
            return get_valid_birthdate(
                input("Enter Birth Year (YYYY): "),
                input("Enter Birth Month (1-12): "),
                input("Enter Birth Day (1-31): ")
            )
        else:            
            return birthdate
    except ValueError:
        print("⚠️  Invalid date. Please enter a valid date.")
        # Prompt user again
        return get_valid_birthdate(
            input("Enter Birth Year (YYYY): "),
            input("Enter Birth Month (1-12): "),
            input("Enter Birth Day (1-31): ")
        )

# Helper function to validate integer input
def get_valid_grade():
    while True:
        try:
            value = int(input("Enter Grade (0-6+): "))
            # Check for negative grades
            if value < 0:
                print("⚠️  Cannot be negative. Please enter a valid number.")
            else:
                return value
        except ValueError:
            # Handle non-integer input
            print("⚠️  Invalid grade. Please enter a number.")

# Helper function to validate email input
def get_valid_email():
    while True:
        email = input("Enter e-Mail Address: ")
        if "@" in email and "." in email:
            return email
        else:
            print("⚠️  Invalid email format. Please enter a valid email address.")

# Helper function to validate name input
def get_valid_name(prompt:str):
    while True:
        name = input(prompt).strip()
        if name:
            return name
        else:
            print("⚠️  Name cannot be empty. Please enter a name.")

# Add a new student and assign to class
def add_new_student():
    fname = get_valid_name("Enter First Name: ")
    famname = get_valid_name("Enter Family Name: ")
    birthyear = input("Enter Birth Year (YYYY): ")
    birthmonth = input("Enter Birth Month (1-12): ")
    birthday = input("Enter Birth Day (1-31): ")
    birthdate = get_valid_birthdate(birthyear, birthmonth, birthday)
    email = get_valid_email()
    grade = get_valid_grade()
    new_id = unique_id()

    students.append([new_id, fname, famname, birthdate, grade, email])
    add_student_to_classes(new_id, grade, birthdate)
    print(f"Student {fname} {famname} added with ID {new_id}.")

def list_students_and_ages():
    format_str = "{: <5} {: <15} {: <15} {: <14}"   

    # A new report “Dancers Ages” added
    print("- Dancers Ages -".center(44))
    print("")
    display_formatted_row(["ID","First Name","Family Name", "Age"],format_str)      
    print("-" * 44)    

    for student in students:
        id = student[0]
        fname = student[1]
        famname = student[2]
        # student birthdate is in student[3]
        age = calculate_age(student[3])

        display_formatted_row([id,fname,famname,age],format_str)   

# find student(s) and display details by family name
def find_student_by_family_name():
    format_str = "{: <5} {: <15} {: <15} {: <14} {: <6} {: <20}"
    """
    Get family name to search for. 
    Case insensitive search
    """
    search_name = input("Enter Family Name to search: ").strip().lower()
    # Find all matching students. Put into a list.
    matches = [student for student in students if student[2].strip().lower() == search_name]

    if not matches:
        print(f"⚠️  No students found with family name '{search_name}'.")
        return

    print("")
    print(f"- Students with Family Name: {search_name} -".center(74))
    print("")
    display_formatted_row(["ID","First Name","Family Name","Birth Date","Grade","e-Mail"], format_str)
    print("-" * 85)

    for student in matches:
        print_student_details(student, format_str)

# Remove a student by ID and update class enrolments
def remove_student():
    while True:
        try:
            # Get student ID to remove
            student_id = int(input("Enter the Student ID to remove: ").strip())
            break
        except ValueError:
            print("⚠️  Invalid ID. Please enter a number.")

    """
    initialise 'student_to_remove' variable to None
    Why not initialise to []? -> searching for a single student, not a list of students.
    """
    student_to_remove = None
    # Find the student in the students list
    for student in students:
        if student[0] == student_id:
            student_to_remove = student
            # Exit loop once found
            break

    if not student_to_remove:
        print(f"⚠️  No student found with ID {student_id}.")
        return
    
    # Confirm removal
    print("")
    print("❓ Are you sure you want to remove the following student?")
    print("")
    format_str = "{: <5} {: <15} {: <15} {: <14} {: <6} {: <20}"
    display_formatted_row(["ID","First Name","Family Name","Birth Date","Grade","e-Mail"], format_str)
    print("-" * 85) 
    print_student_details(student_to_remove, format_str)
    print("")

    # Get confirmation from user
    confirm = input("Type 'y' to confirm removal: ").strip().lower()
    if confirm != 'y':
        print("⚠️  Removal cancelled.")
        return

    # Remove student from students list
    students.remove(student_to_remove)

    # Remove student from classes
    for class_name, student_ids in classes.items():
        if student_id in student_ids:
            student_ids.remove(student_id)

    print(f"Student with ID {student_id} has been removed.")

def disp_menu():
    """
    Displays the menu and current date.  No parameters required.
    """
    print("==== WELCOME TO SELWYN DANCE SCHOOL SYSTEM ===")
    print(" 1 - List Students")
    print(" 2 - List Students and their Classes")
    print(" 3 - List Students and their Ages")
    print(" 4 - Find Student")
    print(" 5 - Remove Student")
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
        find_student_by_family_name()
    elif response == "5":
        remove_student()
    elif response == "6":
        add_new_student()
    elif response.upper() != "X":
        print("\n*** Invalid response, please try again (enter 1-6 or X)")

    print("")

print("\n=== Thank you for using the SELWYN DANCE SYSTEM! ===\n")

