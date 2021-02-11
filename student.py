from admin import *
from teacher import *


class Student(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def enroll(self):
        self.freeCoursestoEnroll()
        course_to_enroll = input("Input the course you want to enroll: ")
        for course in data['courses']:
            if course['course-name'] == course_to_enroll:
                course['students'][0].update({self.username: ""})
                print("You have been successfully enrolled")

        write_json(data)
        print("\n")

    def unenroll(self):
        print("These are available courses to unenroll")
        for course in data['courses']:
            if course['students'][0].__contains__(self.username):
                print(course['course-name'])
            else:
                pass
        course_to_unenroll = input("Input the course you want to unenroll: ")
        for course in data['courses']:
            if course['course-name'] == course_to_unenroll:
                course['students'][0].pop(self.username)
                print("You have been successfully unenrolled")
        write_json(data)
        print("\n")

    def seeMarks(self):
        for course in data['courses']:
            if course['students'][0].__contains__(self.username):
                print(f"{course['course-name']} marked with {course['students'][0][self.username]}")
            else:
                pass
        print("\n")

    def seeTeachers(self):
        for course in data['courses']:
            print(f"{course['course-name']} is taught by {course['teacher']}")
        print("\n")

    def freeCoursestoEnroll(self):
        print("These are available courses to enroll")
        for course in data['courses']:
            if course['students'][0].__contains__(self.username):
                pass
            else:
                print(course['course-name'])
        print("\n")
