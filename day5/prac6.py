from prac5_re import C

Employees = []

inp = int(input("Enter a no.: "))
for i in range(inp):
    print("-------------------------"+"Enter details of Employee "+str(i+1)+"-----------------------")
    name = input("Enter name of the Employee: ")
    course = input("Enter course of the Employee: ")
    company = input("Enter company of the Employee: ")
    address = input("Enter address of the Employee's address: ")
    c = C(name, course, company, address)
    Employees.append(c)

for i in Employees:
    print("Details of Employee "+str(Employees.index(i)+1)+"===========>>")
    print(i.getName(), i.getCompanyName(), i.giveCourseDetails())
