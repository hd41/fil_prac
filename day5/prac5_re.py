class College:
    college_name=""
    course=""
    def __init__(self,a,b):
        self.college_name=a
        self.course=b
    def setName(self,name):
        self.college_name = name
    def setCourse(self,arg):
        self.course = arg
    def getName(self):
        return self.college_name
    def giveCourseDetails(self):
        return self.course

class Company:
    company_name=""
    company_address = ""
    def __init__(self,a,b):
        self.company_name = a 
        self.company_address = b
    def setCompanyName(self,arg):
        self.company_name = ""
    def setCompanyAddress(self, arg):
        self.company_address = arg
    def getCompanyAddress(self):
        return self.company_address
    def getCompanyName(self):
        return self.company_name

class C(College, Company):
    def __init__(self, arg1,arg2,arg3,arg4):
        self.college_name  = arg1
        self.course = arg2
        self.company_name = arg3
        self.company_address = arg4
    def __call__(self):
        print(self.college_name,self.course,self.company_address)

c = C("Himanshu","CSE","FIL","Gurugram")
d = C("Parvesh", "ECE", "Google", "Hyderabad")

Employees = []
Employees.append(c)
Employees.append(d)
