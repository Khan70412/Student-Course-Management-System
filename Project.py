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
        



def Student_exists(id):
    try:
        file = open('students.txt', 'r')
        Found = False
        for line in file:
            if id == line.strip().split(',')[0]:
                Found = True
        file.close()
        
        return Found
    
    except IOError as error: 
        print("Error occurred while file handling operations", error)
    except FileNotFoundError:
        print("File not found")


def Course_exists(Course_name):
    try:
        file = open('courses.txt', 'r')
        Found = False
        for line in file:
            if line.strip() == Course_name: 
                Found = True
        file.close()
        return Found

    except IOError as error:
        print("Error occurred while file handling operations", error)
    except FileNotFoundError:
        print("File not found")


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
                    file = open('students.txt', 'a')
                    file.write(id + ',' + student_name + '\n')
                    file.close()
                    print("Student was successfully added")

                except IOError as error:
                    print("Error occurred while file handling operations", error)
                except FileNotFoundError:
                    print("File not found")

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
                file = open('courses.txt', 'a')
                file.write(Course_name + '\n' )
                file.close()
                print("Course was successfully added")
            except IOError as error:
                print("Error occurred while file handling operations", error)
            except FileNotFoundError:
                print("File not found")

        else:
            print("Course already exists in the file")
    else:
        print("The name doesn't contain only aplhabets")




def validate_grade(grade):
    is_valid = False
    if 0 <= grade <= 100:
        is_valid = True
    return is_valid



def Enroll_Student():
    try:
        id = input("Enter the id ")       
        if Student_exists(id):
            Course = input("Enter the course name ")
            if Course_exists(Course):
                grade = float(input("Enter the grade "))
                if validate_grade(grade):
                    try:
                        file = open('grades.txt', 'a')
                        file.write(id + ',' + Course + ',' + str(grade) + '\n')
                        print("Student was added to the file")
                        
                    except IOError as file_error:
                        print("Error occured in the file handling operations", file_error)
                    except FileNotFoundError:
                        print("File not found")
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
    
def check_empty_files(line):
    if line == '':
        return True # file is empty
    else:
        return False # file is not empty

def Display_Students():
    try: 
        file = open('students.txt', 'r')
        line1 = file.readline().strip()
        if not check_empty_files(line1): # check for empty files
            print()
            print("id \t name")
            print("--------------------------")
            contents_of_line = line1.split(',')
            id = contents_of_line[0]
            name = contents_of_line[1]
            print(f'{id} \t {name}') # printing the first record in the file

            for line in file:
                contents_of_line = line.strip().split(',')
                id = contents_of_line[0]
                name = contents_of_line[1]
                print(f'{id} \t {name}')
            print()
            file.close()
        else:
            print("File is empty")
    except IOError as error:
        print("Error occurred while file handling operations", error)
    except FileNotFoundError:
        print("File not found")


def Display_Courses():
    try:
        file = open("courses.txt", 'r')
        line1 = file.readline().strip()
        if not check_empty_files(line1):
            print()
            print("Courses")
            print('-------------------')
            print(line1) # printing the first line
            for line in file:
                print(line.strip())
            file.close()
            print()
        else:
            print("The file is empty")
    except IOError as error:
        print("Error occurred while file handling operations", error)



def Calculate_avg():

    id = input("Enter the student id ")

    if Student_exists(id):
        student_grades = [] # using an array to store the student grades 
        try:
            file = open("grades.txt", 'r')
            for line in file:
                if line.strip().split(',')[0] == id:
                    grade = line.strip().split(',')[2]
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
        top_grade = -1
        Course = input("Enter the course name ")
        top_student = " " 
        top_student_id = " "
        if Course_exists(Course):
            file = open("grades.txt", 'r')
            for line in file:
                if line.strip().split(',')[1] == Course:
                    if line.strip().split(',')[2] == "": # checking if no grade exists 
                        grade = 0  # when grade doesn't exist, assigning grade the value of 0
                    else:
                        grade = float(line.strip().split(',')[2])
                        if grade > top_grade and grade != 0: 
                            top_grade = grade
                            top_student_id = line.strip().split(',')[0]
                        

            file.close()
            if grade != 0: # finding the top_student only when the grade exists
                file2 = open("students.txt",'r')
                for line in file2:
                    if top_student_id == line.strip().split(',')[0]:
                        top_student = line.strip().split(',')[1]
                print(f"The top student for the course {Course} is {top_student}")
            else:
                print("grade does not exist")
        else:
            print("Course does not exist in the file")


    except IOError as error:
        print("Error occurred while file handling operations", error)
    except FileNotFoundError:
        print("File is not found")
        
    except ValueError as error:
        print("Invalid datatypes", error)


    

main()
