# Model-View-Controller (MVC) architectural pattern

class Model:
    def __init__(self):
        self.admins = []
        self.students = []
        self.teachers = []
    
    def add_admin(self, admin):
        self.admins.append(admin)
    
    def add_student(self, student):
        self.students.append(student)
    
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
    
    def get_admins(self):
        return self.admins
    
    def get_students(self):
        return self.students
    
    def get_teachers(self):
        return self.teachers

class View:
    def display_data(self, data):
        print(data)
    
    def display_message(self, message):
        print(message)

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def add_admin(self, admin):
        self.model.add_admin(admin)
    
    def add_student(self, student):
        self.model.add_student(student)
    
    def add_teacher(self, teacher):
        self.model.add_teacher(teacher)
    
    def display_admins(self):
        self.view.display_data(self.model.get_admins())
    
    def display_students(self):
        self.view.display_data(self.model.get_students())
    
    def display_teachers(self):
        self.view.display_data(self.model.get_teachers())

# Factory Method and Observer design patterns

class Observer:
    def update(self, model):
        pass

class StudentObserver(Observer):
    def update(self, model):
        self.view.display_message("New student added: " + model.name)

class TeacherObserver(Observer):
    def update(self, model):
        self.view.display_message("New teacher added: " + model.name)

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name):
        super().__init__(name)

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)

class AdminFactory:
    def create_person(self, name, role):
        if role == "student":
            return Student(name)
        elif role == "teacher":
            return Teacher(name)
        else:
            return None

model = Model()
view = View()
controller = Controller(model, view)
student_observer = StudentObserver(view)
teacher_observer = TeacherObserver(view)
factory = AdminFactory()

