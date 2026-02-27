Student and Course Management System
This project is a console-based Python application designed to manage student records, course offerings, and academic grading. It utilizes basic file handling (.txt files) to store and retrieve data persistently without the need for an external database.

Key Features
Student Registration: Add new students to the system using a unique numeric ID and an alphabetic name.

Course Management: Create and store new courses for students to enroll in.

Enrollment and Grading: Assign a student to a specific course and record their grade, with built-in validation to ensure grades are between 0 and 100.

Data Visualization: Display a formatted list of all registered students and available courses.

Performance Tracking: Calculate the overall average grade for a specific student across all their enrolled courses.

Top Achiever Search: Search a specific course to identify and display the highest-scoring student.

Robust Error Handling: Includes exception handling for ValueError, IOError, FileNotFoundError, and ZeroDivisionError to prevent the program from crashing during invalid inputs or missing files.

Data Storage Structure
The system uses three text files to act as a lightweight database:


students.txt: Stores the student ID and name separated by a comma (e.g., 1001,Ali).


courses.txt: Maintains a line-by-line list of available courses, such as Algorithms, Computer Networks, and Operating Systems.


grades.txt: Records the student ID, the course name, and the numeric grade (e.g., 1005,CMPS,100.0).

Requirements and Execution
Language: Python 3.x

Dependencies: Standard Python libraries only (no external packages required).

To Run: Execute the script in your terminal using python HW.py and follow the on-screen numeric menu prompts.
