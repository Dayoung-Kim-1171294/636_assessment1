# COMP 636: Python Assessment
**Student Name:** Dayoung Kim  
**Student ID:** 1171294


## Test Data Strategy
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




## Reflection

The most challenging aspect of this assessment was planning the logic required for the Data Validation System. It was difficult because it required handling multiple conditional layers. It was particularly confusing to combine try-except blocks with while loops to ensure the programme would not crash and would keep asking for input until the user provided a valid answer.

Trying to account for every possible invalid input was tricky. I found it quite overwhelming to predict the unpredictable ways a user might break the programme. Consequently, I spent a lot of time debugging and testing various scenarios to ensure the final result ran smoothly.