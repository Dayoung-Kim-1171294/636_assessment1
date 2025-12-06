# COMP 636: Python Assessment

## 🧪 Test Data Strategy
The following table outlines the test data used to verify the class allocation logic and the new validation features. All student entry tests begin by selecting the **"Add New Student"** option (menu 6). 

| Feature Tested | Input Data Entered | Expected Result |
| :--- | :--- | :--- |
| **Class Allocation (Bellbirds)** | **Grade:** `5`<br>**(Other fields valid)** | Student assigned to **Bellbirds**. |
| **Class Allocation (Bellbirds)** | **Grade:** `0`<br>**Year:** `2012` | Student assigned to **Bellbirds**. (Age: 12 or 13) |
| **Class Allocation (Senior Dance)** | **Grade:** `6` | Student assigned to **Senior Dance**. |
| **Class Allocation (Robins)** | **Grade:** `0`<br>**Year:** `2014` | Student assigned to **Robins** (Age: 10 or 11). |
| **Class Allocation (Piwakawaka)** | **Grade:** `3` | Student assigned to **Piwakawaka**. |
| **Class Allocation (Butterflies)** | **Grade:** `0`<br>**Year:** `2017` | Student assigned to **Butterflies** (Age: 7 or 8). |
| **Class Allocation (Fireflies)** | **Grade:** `1` | Student assigned to **Fireflies**. |
| **Class Allocation (Glowworms)** | **Grade:** `0`<br>**Year:** `2020` | Student assigned to **Glowworms**. (Age: 4 or 5)|
| **Input Validation (Non-numeric)** | **Grade:** `abc` | Error message ("Invalid grade. Please enter a number.") displayed, prompts user again. |
| **Input Validation (Negative)** | **Grade:** `-1` | Error message ("Cannot be negative. Please enter a valid number.") displayed, prompts user again. |
| **Date Validation (Invalid Date)** | **Month:** `2`, **Day:** `30` | Error message ("Invalid date. Please enter a valid date.") displayed, prompts user again. |
| **Date Validation (Future Date)** | **Year:** `2099` | Error message ("Invalid date: {input date} is in the future. Please try again.") displayed, prompts user again. |
| **Date Validation (Text Input)** | **Year:** `two thousand` | Error message ("Invalid date. Please enter a valid date.") displayed, prompts user again. |
| **Email Validation (Missing @)** | **Email:** `dayoung.com` | Error message ("Invalid email format. Please enter a valid email address.") displayed, prompts user again. |
| **Email Validation (Missing .)** | **Email:** `dayoung@gmail` | Error message ("Invalid email format. Please enter a valid email address.") displayed, prompts user again. |


## 💭 Reflection

The most significant challenge in this assessment was implementing a robust **Data Validation System** to ensure the program never crashes due to user error.

Initially, simple inputs like dates or grades were prone to errors if a user entered text or invalid numbers. To solve this, I focused on creating specialised helper functions for each data type:

1.  **Date Validation (`get_valid_birthdate`):** This was the most complex part. I had to handle non-numeric text, invalid calendar dates (e.g., February 30th), and future dates. I implemented a recursive approach to ensure the user is prompted until a valid date is provided.
2.  **Grade and Email Validation (`get_valid_grade`, `get_valid_email`):** I applied similar logic to other fields, ensuring grades are not negative and emails contain essential characters like '@' and '.'.