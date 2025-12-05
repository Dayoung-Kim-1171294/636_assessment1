# COMP 636: Python Assessment

## 🧪 Test Data Strategy
The following table outlines the test data used to verify the class allocation logic and the new validation features. All student entry tests begin by selecting the **"Add New Student"** option (menu 6).

| Feature Tested | Menu Option | Input Data Entered (Key Fields) | Expected Result |
| :--- | :---: | :--- | :--- |
| **Class Allocation (Bellbirds)** | `6` | **Grade:** `5`<br>**(Other fields valid)** | Student assigned to **Bellbirds** (Logic: Grade 5). |
| **Class Allocation (Bellbirds)** | `6` | **Grade:** `0`<br>**Year:** `2012` (Age ~13) | Student assigned to **Bellbirds** (Logic: Age 12+). |
| **Class Allocation (Senior Dance)**| `6` | **Grade:** `6` | Student assigned to **Senior Dance** (Logic: Grade 6+). |
| **Class Allocation (Priority)** | `6` | **Grade:** `0`<br>**Year:** `2020` (Age 5) | Student assigned to **Glowworms** (Logic: Age < 6). |
| **Input Validation (Non-numeric)** | `6` | **Grade:** `abc` | Error message ("Invalid input") displayed, prompts user again. |
| **Input Validation (Negative)** | `6` | **Grade:** `-1` | Error message ("Cannot be negative") displayed, prompts user again. |
| **Date Validation (Invalid Date)** | `6` | **Month:** `2`, **Day:** `30` | Error message ("Invalid date") displayed, prompts user again. |
| **Date Validation (Future Date)** | `6` | **Year:** `2099` | Error message ("Invalid date... future") displayed, prompts user again. |
| **Date Validation (Text Input)** | `6` | **Year:** `two thousand` | Error message ("Invalid date") displayed, prompts user again. |
| **Email Validation (Missing @)** | `6` | **Email:** `kimdayoung.com` | Error message ("Invalid email format") displayed, prompts user again. |
| **Search Function** (If added) | `4` | **Name:** `(Existing Student Name)` | Displays details of the student. |


## 💭 Reflection

The most significant challenge in this assessment was implementing a robust **Data Validation System** to ensure the program never crashes due to user error.

Initially, simple inputs like dates or grades were prone to errors if a user entered text or invalid numbers. To solve this, I focused on creating specialized helper functions for each data type:

1.  **Date Validation (`get_valid_birthdate`):** This was the most complex part. I had to handle three layers of potential errors: non-numeric text, invalid calendar dates (e.g., February 30th), and future dates. I implemented a recursive approach (or loop) to ensure the user is prompted until a valid date is provided.
2.  **Grade and Email Validation (`get_valid_grade`, `get_valid_email`):** I applied similar logic to other fields, ensuring grades are not negative and emails contain essential characters like '@' and '.'.