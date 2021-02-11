from admin import *
from student import *


class Teacher(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def seeSubjects(self):
        for course in data['courses']:
            if course['teacher'] == self.username:
                print(f"course-name: {course['course-name']}")
        print("\n")

    def markStudents(self):
        self.seeSubjects()
        subjectname = input("Please choose subject name: ")
        for course in data['courses']:
            if course['teacher'] == self.username:
                if course['course-name'] == subjectname:
                    print("Students enrolled to this course: ")
                    for e in course['students']:
                        for x in e.keys():
                            print(f"{x} marked with {e.get(x)}")
                    student_to_mark = input('Choose student to mark him: ')
                    grade = input('Choose the mark you give him: ')
                    for e in course['students']:
                        for x in e.keys():
                            if x == student_to_mark:
                                e.update({student_to_mark: grade})
                                print("Student was successfully marked")

        write_json(data)
        print("\n")

    def deleteStudent(self):
        self.seeSubjects()
        subjectname = input("Please choose subject name: ")
        for course in data['courses']:
            if course['teacher'] == self.username:
                if course['course-name'] == subjectname:
                    print("Students enrolled to this course: ")
                    for e in course['students']:
                        for x in e.keys():
                            print(f"{x} marked with {e.get(x)}")
                    student_to_delete = input('Choose student to delete him: ')
                    course['students'][0].pop(student_to_delete)
                    print("Student was successfully deleted")

        write_json(data)
        print("\n")

    def addStudent(self):
        self.seeSubjects()
        subjectname = input("Please choose subject name: ")
        for course in data['courses']:
            if course['teacher'] == self.username:
                if course['course-name'] == subjectname:
                    print("Students enrolled to this course: ")
                    for e in course['students']:
                        for x in e.keys():
                            print(f"{x} marked with {e.get(x)}")
                    student_to_add = input('Write student\'s name to add him: ')
                    course['students'][0].update({student_to_add: ""})
                    print("Student was successfully added")

        write_json(data)
        print("\n")
