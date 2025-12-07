# COMP 636: Python Assessment
**Student Name:** Dayoung Kim  
**Student ID:** 1171294

## ✨ New Features Implemented
* **New Classes:** Logic updated to support 'Bellbirds' (Grade 5 or Age 12+) and 'Senior Dance' (Grade 6+ only).
* **New Reports:** 
    * `List Students and their Classes`: Displays students grouped by class, sorted by family name.
    * `List Students and their Ages`: Displays the age of each student.
* **Menu 4 (Find Student):** Allows case-insensitive search for students by their family name.
* **Menu 5 (Remove Student):** Allows removal of a student by ID, requiring confirmation and updating class lists.
* **Data Validation:** Implemented for grades, dates, and email formats to prevent program crashes and ensure user-friendliness.


## 🧪 Test Data Strategy
The following table outlines the test data used to verify the class allocation logic and the new features/validation checks.

| Feature Tested | Menu | Input Data Entered | Expected Result |
| :--- | :--- | :--- | :--- |
| **Class Allocation (Bellbirds)** |`6`| **Grade:** `5` | Student assigned to **Bellbirds**. Assigned by grade. |
| **Class Allocation (Bellbirds)** |`6`| **Grade:** `0`<br>**Year:** `2012` | Student assigned to **Bellbirds**. Assigned by age(12 or 13) as grade is **0** |
| **Input Validation (Non-numeric)** |`6`| **Grade:** `abc` | Error message ("⚠️  Invalid grade. Please enter a number.") displayed, prompts user again. |
| **Input Validation (Negative)** |`6`| **Grade:** `-1` | Error message ("⚠️  Cannot be negative. Please enter a valid number.") displayed, prompts user again. |
| **Date Validation (Invalid Date)** |`6`| **Month:** `2`, **Day:** `30` | Error message ("⚠️  Invalid date. Please enter a valid date.") displayed, prompts user again. |
| **Date Validation (Future Date)** | `6`|**Year:** `2099` | Error message ("⚠️  Invalid date: {input date} is in the future. Please try again.") displayed, prompts user again. |
| **Date Validation (Text Input)** |`6`| **Year:** `two thousand` | Error message ("⚠️  Invalid date. Please enter a valid date.") displayed, prompts user again. |
| **Email Validation (Missing @ or .)** | `6`|**Email:** `dayoung@lincolnuni` | Error message ("⚠️  Invalid email format. Please enter a valid email address.") displayed, prompts user again. |
| **Find Student** |`4`| **Family Name:** `charles` | Displays details for all students with family name 'Charles'. Case is insensitive|
| **Find Student - Not Found** | `4`|**Family Name:** `abc` | Error message ("⚠️  No students found with family name 'abc'.") displayed. |
| **Remove Student - Success** | `5`|**ID:** `121`<br>**Confirm:** `y` | Student 121 removed from students list and class lists. |
| **Remove Student - Cancel** | `5`|**ID:** `801`<br>**Confirm:** `n`(any input except `y`) | Removal cancelled, student 801 remains in the system. |
| **Remove Student - Invalid ID** |`5`| **ID:** `abc` | Error message ("⚠️  Invalid ID. Please enter a number.") displayed. |
| **Remove Student - Not Found** |`5`| **ID:** `111` | Error message ("⚠️  No student found with ID 111.") displayed. |



## 💭 Reflection

The most significant challenge in this assessment was implementing a robust **Data Validation System** to ensure the program never crashes due to user error.

Initially, simple inputs like dates or grades were prone to errors if a user entered text or invalid numbers. To solve this, I focused on creating specialised helper functions for each data type:

1.  **Date Validation (`get_valid_birthdate`):** This was the most complex part. I had to handle non-numeric text, invalid calendar dates (e.g., February 30th), and future dates. I implemented a recursive approach to ensure the user is prompted until a valid date is provided.
2.  **Grade and Email Validation (`get_valid_grade`, `get_valid_email`):** I applied similar logic to other fields, ensuring grades are not negative and emails contain essential characters like '@' and '.'.

Despite these challenges, I enjoyed implementing the new features for Menu 4 and 5. It was fun to manipulate the data in diverse ways to create these search and removal functions, and seeing them work successfully was very rewarding.