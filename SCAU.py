

class Person:
    def __init__(self, name, age, cpf, address):
        self.name = name
        self.age = age
        self.cpf = cpf
        self.address = address

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_cpf(self):
        return self.cpf

    def get_address(self):
        return self.address

class Employee(Person):
    def __init__(self, name, age, cpf, address, job_title):
        super().__init__(name, age, cpf, address)
        self.job_title = job_title
    
    def get_job(self):
        return self.job_title 

class Patient(Person):
    def __init__(self, name, age, cpf, address, phone):
        super().__init__(name, age, cpf, address)
        self.phone = phone
        self.promptuary = Promptuary()

    def add_promptuary(self):
        pass

class Promptuary:
    def __init__(self):
        self.group = None
        self.origin = None
        self.mode = None
        self.illness = None
        self.status = True
        self.family_member = None
        self.tr = None

    def get_group(self):
        return group

    def get_origin(self):
        return origin
    
    def get_mode(self):
        return mode

    def get_illness(self):
        return illness

    def get_status(self):
        return status

    def get_family_member(self):
        return family_member

    def get_tr(self):
        return tr

     def set_group(self, group):
         self.group = group

    def set_origin(self, origin):
        self.origin = origin
          
    def set_mode(self, mode):
        self.mode = mode
       
    def set_illness(self, illness):
        self.illness = illness

    def set_status(self, status):
       self.status = status

    def set_family_member(self, name, age, cpf, address):
        self.family_member = Person(name, age, cpf, address)

    def set_tr(self, name, age, cpf, address, job_title):
        self.tr = Employee(name, age, cpf, address, job_title)
              


s4 = Student(input(": "), int(input(": ")), int(input(": ")))
course.add_student(s4)
print(course.get_average_grade())
