from admin import *
from teacher import *
from student import *

print("Welcome to the Moodle")
print("\n")

while True:
    # username and password prompts by the user
    username_prompt = input("Please type your username:")
    password_prompt = input("Please type your password:")

    # authentication and authorization
    prompt = User(username_prompt, password_prompt)
    prompt.authorization()
    if prompt.status == 1:
        break

# set the role of the user
if prompt.role == 'admin':
    user = Admin(username_prompt, password_prompt)
    admin = ("Methods to do: \n"
             "1.Create teacher account \n"
             "2.Create student account \n"
             "3.Create course \n"
             
             "4.Update teacher account \n"
             "5.Update student account \n"
             "6.Update course \n"
             
             "7.Delete teacher account \n"
             "8.Delete student account \n"
             "9.Delete course \n"
             
             "10.See teacher rooms \n"
             "11.Add teacher room \n"
             "12.Delete teacher room \n"
             
             "13. See commands again \n"
             "14. Quit \n"
             )
    print(admin)
    while True:
        print("If you want to see command again, please press 13")
        print("If you want to quit, please press 14")
        action = input("Enter a command number: ")
        if action == "1":
            uname = input("Enter teacher username: ")
            passw = input("Enter teacher password: ")
            user.createTeacher(uname, passw)
        elif action == "2":
            uname = input("Enter student username: ")
            passw = input("Enter student password: ")
            user.createStudent(uname, passw)
        elif action == "3":
            course_name = input("Enter course name: ")
            teacher = input("Enter teacher name: ")
            student = input("Enter student name: ")
            user.createCourse(course_name, teacher, student)
        elif action == "4":
            user.updateTeacher()
        elif action == "5":
            user.updateStudent()
        elif action == "6":
            user.updateCourse()
        elif action == "7":
            user.deleteTeacher()
        elif action == "8":
            user.deleteStudent()
        elif action == "9":
            user.deleteCourse()
        elif action == "10":
            user.seeRooms()
        elif action == "11":
            user.setRoom()
        elif action == "12":
            user.deleteRoom()
        elif action == "13":
            print(admin)
        elif action == "14":
            break
        else:
            print("Please try again! \n")
if prompt.role == 'teacher':
    user = Teacher(username_prompt, password_prompt)
    teacher = ("Methods to do: \n"
               "1. See subject you are leading \n"
               "2. Mark students \n"
               "3. Add student to course \n"
               "4. Delete student from course \n"
               "5. See commands again \n"
               "6. Quit \n"
               )
    print(teacher)
    while True:
        print("If you want to see command again, please press 5")
        print("If you want to quit, please press 6")
        action = input("Enter a command number: ")
        if action == "1":
            user.seeSubjects()
        elif action == "2":
           user.markStudents()
        elif action == "3":
            user.addStudent()
        elif action == "4":
            user.deleteStudent()
        elif action == "5":
            print(teacher)
        elif action == "6":
            break
        else:
            print("Please try again!")
if prompt.role == 'student':
    user = Student(username_prompt, password_prompt)
    student = ("Methods to do: \n"
               "1. Enroll to course \n"
               "2. UnEnroll from course \n"
               "3. See marks of yours \n"
               "4. See all teachers \n"
               "5. See free courses to enroll \n"
               "6. See commands again \n"
               "7. Quit \n"
               )
    print(student)
    while True:
        print("If you want to see command again, please press 6")
        print("If you want to quit, please press 7")
        action = input("Enter a command number: ")
        if action == "1":
            user.enroll()
        elif action == "2":
            user.unenroll()
        elif action == "3":
            user.seeMarks()
        elif action == "4":
            user.seeTeachers()
        elif action == "5":
            user.freeCoursestoEnroll()
        elif action == "6":
            print(student)
        elif action == "7":
            break
        else:
            print("Please try again!")

