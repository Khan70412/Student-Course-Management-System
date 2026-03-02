def main():
    while True:
        print("1. Add a new student")
        print("2. Add a new course")
        print("3. Enroll a student in a course and assign a grade")
        print("4. Display all students")
        print("5. Display all courses")
        print("6. Calculate average grade for a student")
        print("7. Find the highest scoring student in a course")
        print("8. Exit")
        print()
        try:
            option = int(input("Enter the the option "))
            if option == 8:
                print("Exiting the program ")
                break
            elif option == 1:
                Add_Student()
            elif option == 2:
                Add_Course()
            elif option == 3:
                Enroll_Student()
            elif option == 4:
                Display_Students()
            elif option == 5:
                Display_Courses()
            elif option == 6:
                Calculate_avg()
            elif option == 7:
                find_top_student()
            else:
                print("Enter the correct option")

        except ValueError as error:
            print("Incorrect data type, option needs to be entered as an integer", error)
        



def Student_exists(student_id):
    try:
        with open("students.txt", "r") as file:
            for line in file:
                if student_id == line.strip().split(",")[0]:
                    return True
        return False
    except FileNotFoundError:
        print("students.txt file not found.")
        return False
    except IOError as error:
        print("Error occurred while handling students.txt:", error)
        return False


def Course_exists(course_name):
    try:
        with open("courses.txt", "r") as file:
            for line in file:
                if line.strip() == course_name:
                    return True
        return False
    except FileNotFoundError:
        print("courses.txt file not found.")
        return False
    except IOError as error:
        print("Error occurred while handling courses.txt:", error)
        return False



def check_aplhabets_and_spaces(name): # function to check for alphabets and spaces
    for char in name:
        if not (char.isalpha() or char.isspace()): 
            return False
    return True


def Add_Student():
    id = input("Enter the Student ID ")
    if id.isdigit(): 
        if not Student_exists(id): 
            student_name = input("Enter the student name ")
            if check_aplhabets_and_spaces(student_name):
                try:
                    with open("students.txt", "a") as file:
                        file.write(id + "," + student_name + "\n")
                    print("Student was successfully added.")
                except FileNotFoundError:
                    print("File not found")
                except IOError as error:
                    print("Error occurred while file handling operations", error)


            else:
                print("Student name does not only contain numbers and aplhabets ")
        else:
            print("Student id already exists in the file")
    else:
        print("The id does not contain all numeric letters")



def Add_Course():
    Course_name = input("Enter the course name ")
    
    if check_aplhabets_and_spaces(Course_name):      
        if not Course_exists(Course_name):
            try:
                with open("courses.txt", "a") as file:
                    file.write(Course_name + "\n")
                print("Course was successfully added.")
            except FileNotFoundError:
                print("File not found")
            except IOError as error:
                print("Error occurred while file handling operations", error)
      

        else:
            print("Course already exists in the file")
    else:
        print("The name doesn't contain only aplhabets")




def validate_grade(grade):
        return  0 <= grade <= 100






def Enroll_Student():
    try:
        id = input("Enter the id ")       
        if Student_exists(id):
            Course = input("Enter the course name ")
            if Course_exists(Course):
                grade = float(input("Enter the grade "))
                if validate_grade(grade):
                    try:
                        with open("grades.txt", "a") as file:
                            file.write(id + "," + Course + "," + str(grade) + "\n")
                        print("Student enrollment and grade were saved.")
                    except FileNotFoundError:
                        print("File not found")
                    except IOError as file_error:
                        print("Error occured in the file handling operations", file_error)

                else:
                    print("invalid grade")
            else:
                print("Course does not exist in the file")
        else:
            print("Student  does not exist in the file")
    except ValueError as error:
        print("Invalid data type",error)
    except FileNotFoundError:
        print("File not found")
    

def Display_Students():
    try: 
        with open('students.txt', 'r') as file:
            lines = []
            for line in file:
                line = line.strip()
                if line != "":
                    lines.append(line)

            if len(lines) == 0:
                print("No students found.")
                return

            print()
            print("id \t name")
            print("--------------------------")
            for line in lines:
                parts = line.split(",")
                if len(parts) == 2:
                    student_id = parts[0]
                    name = parts[1]
                    print(f"{student_id} \t {name}")
            print()
    except FileNotFoundError:
        print("File not found")
    except IOError as error:
        print("Error occurred while file handling operations", error)



def Display_Courses():
    try:
        with open("courses.txt", "r") as file:
            # Collect non-empty lines manually (no list comprehension)
            lines = []
            for line in file:
                line = line.strip()
                if line != "":
                    lines.append(line)

        if len(lines) == 0:
            print("No courses found.")
            return
        print()
        print("Courses")
        print('-------------------')

        for course in lines:
            print(course.strip())

            print()
    except FileNotFoundError:
        print("courses.txt file not found.")
    except IOError as error:
        print("Error occurred while handling courses.txt:", error)


def Calculate_avg():

    id = input("Enter the student id ")

    if Student_exists(id):
        student_grades = [] # using an array to store the student grades 
        try:
            with open("grades.txt", 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 3 and parts[0] == id:
                        grade = parts[2]
                        if grade != '':
                            student_grades.append(float(grade))

            if len(student_grades) == 0: # checking if no grades exist
                print("No grade exists")
            else:
                try:
                    average = sum(student_grades)/len(student_grades)
                    print(f"The average grade for the student is {average:.2f}")

                except ZeroDivisionError as error:
                    print("Run time error, division with zero ", error)

        except IOError as error:
            print("Error occurred while file handling operations", error)
        except FileNotFoundError:
            print("File not found")

    else:
        print("Student record doesn't exist in the file")


def find_top_student():
    try:
        course = input("Enter the course name: ")
        if not Course_exists(course):
            print("Course does not exist in the file.")
            return

        top_grade = -1
        top_student_id = None

        try:
            with open("grades.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) == 3 and parts[1] == course:
                        grade_str = parts[2]
                        if grade_str == "":
                            grade = 0
                        else:
                            grade = float(grade_str)
                        if grade > top_grade and grade != 0:
                            top_grade = grade
                            top_student_id = parts[0]
        except FileNotFoundError:
            print("grades.txt file not found.")
            return
        except IOError as error:
            print("Error occurred while handling grades.txt:", error)
            return

        if top_grade == -1 or top_student_id is None:
            print("No valid grades exist for this course.")
            return
        try:
            top_student_name = None
            with open("students.txt", "r") as file2:
                for line in file2:
                    parts = line.strip().split(",")
                    if len(parts) == 2 and parts[0] == top_student_id:
                        top_student_name = parts[1]
                        break

            if top_student_name:
                print(f"The top student for the course {course} is {top_student_name} with grade {top_grade}.")
            else:
                print("Top student ID found, but no matching student record in students.txt.")
        except FileNotFoundError:
            print("students.txt file not found.")
        except IOError as error:
            print("Error occurred while handling students.txt:", error)
    except ValueError as error:
        print("Invalid data type:", error)


    

main()
