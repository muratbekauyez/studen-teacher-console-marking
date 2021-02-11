import json
from abc import ABC

with open("data.json") as f:
    data = json.load(f)


def write_json(data, filename="data.json"):
    with open(filename, "w") as d:
        json.dump(data, d, indent=4)


class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.role = ""
        self.status = 0

    def authorization(self):
        for user in data['users']:
            if user['username'] == self.username and user['password'] == self.password:
                self.status = 1
                self.role = user['role']
                break

        if self.status == 1:
            print('authorization complete')
        if self.status == 0:
            print('something went wrong, please try again')

        print("\n")


def viewTeachers():
    for user in data['users']:
        if user['role'] == "teacher":
            print(f"Username: {user['username']}")
            print(f"Password: {user['password']}")
            print(f"Role: {user['role']}")
            print("\n")


def viewStudents():
    for user in data['users']:
        if user['role'] == "student":
            print(f"Username: {user['username']}")
            print(f"Password: {user['password']}")
            print(f"Role: {user['role']}")
            print("\n")


def viewCourses():
    for course in data['courses']:
        print(f"course-name: {course['course-name']}")
        print(f"teacher: {course['teacher']}")
        print(f"students: {course['students']}")
        print("\n")


class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    @staticmethod
    def createTeacher(username, password):
        temp = data['users']
        new = {"username": username, "password": password, "role": "teacher"}
        temp.append(new)

        write_json(data)
        print("Teacher has been successfully uploaded")
        print("\n")

    @staticmethod
    def createStudent(username, password):
        temp = data['users']
        new = {"username": username, "password": password, "role": "student"}
        temp.append(new)

        write_json(data)
        print("Student has been successfully uploaded")
        print("\n")

    @staticmethod
    def createCourse(course_name, teacher, students):
        temp = data['courses']
        new = {"course-name": course_name, "teacher": teacher, "students": students}
        temp.append(new)

        write_json(data)
        print("Course has been successfully uploaded")
        print("\n")

    @staticmethod
    def updateTeacher():
        viewTeachers()
        edit_option = input("Which teacher would you like to change? Write his/her username: ")
        i = 0
        for entry in data['users']:
            if entry['username'] == edit_option:
                uname = entry["username"]
                passw = entry["password"]
                role = entry["role"]
                print(f"Current username is {uname}")
                uname = input("What would you like it to be? ")
                print(f"Current password is {passw}")
                passw = input("What would you like it to be? ")
                print(f"Current role is {role}")
                role = input("What would you like it to be? ")
                data['users'][i]['username'] = uname
                data['users'][i]['password'] = passw
                data['users'][i]['role'] = role
            i = i + 1

        write_json(data)
        print("Teacher data was successfully changed")
        print("\n")

    @staticmethod
    def updateStudent():
        viewStudents()
        edit_option = input("Which student would you like to change? Write his/her username: ")
        i = 0
        for entry in data['users']:
            if entry['username'] == edit_option:
                uname = entry["username"]
                passw = entry["password"]
                role = entry["role"]
                print(f"Current username is {uname}")
                uname = input("What would you like it to be? ")
                print(f"Current password is {passw}")
                passw = input("What would you like it to be? ")
                print(f"Current role is {role}")
                role = input("What would you like it to be? ")
                data['users'][i]['username'] = uname
                data['users'][i]['password'] = passw
                data['users'][i]['role'] = role
            i = i + 1

        write_json(data)
        print("Student data was successfully changed")
        print("\n")

    @staticmethod
    def updateCourse():
        viewCourses()
        edit_option = input("Which course would you like to change? Write his/her course name: ")
        i = 0
        for entry in data['courses']:
            if entry['course-name'] == edit_option:
                cname = entry["course-name"]
                cteacher = entry["teacher"]
                cstudents = entry["students"]
                print(f"Current course name is {cname}")
                cname = input("What would you like it to be? ")
                print(f"Current teacher is {cteacher}")
                cteacher = input("What would you like it to be? ")
                print(cstudents)
                print("Current students are: ")

                for e in cstudents:
                    for x in e.keys():
                        print(x, e.get(x))

                n = int(input("How many students there would be?"))
                students = [{}]
                for j in range(n):
                    name = input("What is his name?")
                    grade = input("What is his grade?")
                    students[0].update({name: grade})
                    print(students)

                data['courses'][i]['course-name'] = cname
                data['courses'][i]['teacher'] = cteacher
                data['courses'][i]['students'] = students
            i = i + 1

        write_json(data)
        print("Student data was successfully changed")
        print("\n")

    @staticmethod
    def deleteTeacher():
        with open("data.json") as f:
            new_data = json.load(f)
        viewTeachers()
        delete_option = input("Which teacher would you like to delete? Write his/her username: ")
        for i in range(len(data['users'])):
            new_data['users'].pop(0)
        for entry in data['users']:
            if entry['username'] == delete_option:
                continue
            else:
                new_data['users'].append(entry)

        write_json(new_data)
        print("Teacher data was successfully deleted")
        print("\n")

    @staticmethod
    def deleteStudent():
        with open("data.json") as f:
            new_data = json.load(f)
        viewStudents()
        delete_option = input("Which student would you like to delete? Write his/her username: ")
        for i in range(len(data['users'])):
            new_data['users'].pop(0)
        for entry in data['users']:
            if entry['username'] == delete_option:
                continue
            else:
                new_data['users'].append(entry)

        write_json(new_data)
        print("Teacher data was successfully deleted")
        print("\n")

    @staticmethod
    def deleteCourse():
        with open("data.json") as f:
            new_data = json.load(f)
        viewCourses()
        delete_option = input("Which course would you like to delete? Write his/her username: ")
        for i in range(len(data['courses'])):
            new_data['courses'].pop(0)
        for entry in data['courses']:
            if entry['course-name'] == delete_option:
                continue
            else:
                new_data['courses'].append(entry)

        write_json(new_data)
        print("Courses data was successfully deleted")
        print("\n")

    def seeRooms(self):
        for room in data['rooms']:
            print(f"{room['teacher']} is at room {room['room']}")
        print("\n")

    def setRoom(self):
        self.seeRooms()
        teacher = input("Write the teacher name you want to give room: ")
        room = input("Write the room for the teacher: ")
        data['rooms'].append(dict({"teacher": teacher, "room": room}))
        write_json(data)
        print("\n")

    def deleteRoom(self):
        self.seeRooms()
        room = input("Write the room you wish to delete: ")
        for entry in data['rooms']:
            if entry['room'].__contains__(room):
                data['rooms'].remove(entry)
                print("Room was successfully deleted")
        write_json(data)
