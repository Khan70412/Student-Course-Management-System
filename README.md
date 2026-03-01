# Student and Course Management System 

This project is a console-based Python application designed to manage student records, course offerings, and academic grading. It utilizes basic file handling via `.txt` files to store and retrieve data persistently without the need for an external database.

## Key Features
* **Student Registration:** Add new students to the system using a unique numeric ID and an alphabetic name.
* **Course Management:** Create and store new courses for students to enroll in.
* **Enrollment and Grading:** Assign students to specific courses and record grades with built-in validation (0–100).
* **Data Visualization:** Display formatted lists of all registered students and available courses.
* **Performance Tracking:** Calculate the overall average grade for a specific student across all enrolled courses.
* **Top Achiever Search:** Search specific courses to identify and display the highest-scoring student.
* **Robust Error Handling:** Includes exception handling for `ValueError`, `IOError`, `FileNotFoundError`, and `ZeroDivisionError` to prevent crashes.

## Data Storage Structure
The system uses three text files to act as a lightweight database:
* `students.txt`: Stores student ID and name separated by a comma (e.g., `1001,Ali`).
* `courses.txt`: Maintains a line-by-line list of available courses (e.g., Algorithms, Operating Systems).
* `grades.txt`: Records student ID, course name, and numeric grade (e.g., `1005,CMPS,100.0`).

## How to Run
1. **Requirements:** Ensure you have Python 3.x installed.
2. **Dependencies:** Uses standard Python libraries only (no external packages required).
3. **Execution:** Run the script in your terminal:
   ```bash
   python HW.py
