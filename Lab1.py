class Student:
    ID=int()
    first_name=str()
    last_name=str()
    email=str()
    Course=str()
    Year=int()
    GPA=float()
    University=str()
    Mobile=int()
    def email_generator(self,first_name,last_name):
        self.email=first_name.replace(' ','')+last_name+"@"+self.University

    def __init__(self,ID,first_name,last_name,Course,Year,GPA,University,Mobile):
        self.ID=ID
        self.first_name=first_name
        self.last_name=last_name
        self.Course=Course
        self.Year=Year
        self.GPA=GPA
        self.University=University
        self.Mobile=Mobile
        self.email_generator(first_name,last_name)
    def change_fname(self,first_name):
        self.first_name=first_name
        self.email_generator(first_name,self.last_name)
    def change_lname(self,last_name):
        self.last_name=last_name
        self.email_generator(self.first_name,last_name)

A=Student(int(input()),input(),input(),input(),int(input()),float(input()),input(),int(input()))
print(A.email)