# Create a class Employee and then do the following
# Base/Parent Class - Employee
#class 1
class classEmployee:

    # Create a data members to count the number of Employees and average salary
  print("---Non-Fulltime employees list---")
  empcount=0
  Totalsalary=0

# Create a constructor to initialize name, family, salary, department
  def __init__(self,ename,esal,edept): # Use of self
      self.ename=ename     # Use of self
      self.esal=esal
      self.edept=edept
      classEmployee.empcount+=1
      classEmployee.Totalsalary+=esal
# Member method
  def display(self):

      print("name:",self.ename,"salary:",self.esal,"dept:",self.edept)


# Inheritance
# Child/Base Class - Full time Employee which inherits properties of parent class
# class 2
class Fulltime(classEmployee):

    fulltimecount=0
    fulltimetotalsalary=0
    def __init__(self,ename,esal,edept,ecity):
        super().__init__(ename,esal,edept) # Use of super call
        self.ecity=ecity
        Fulltime.fulltimecount+=1
        Fulltime.fulltimetotalsalary+=esal
    def display(self):

        classEmployee.display(self)
        print("Employment City:",self.ecity) # Use of self

# Inheritence
# class 3
class Manager(classEmployee):
    managercount=0
    def __init__(self,ename,esal,edept,eexp):
        super().__init__(ename,esal,edept)   # Use of super call
        self.eexp=eexp
        Manager.managercount+=1
    def display(self):
        print("")
        print("---Manager details---")
        classEmployee.display(self)
        print("Manager Experience:",self.eexp,"years") # Use of self

# class 4
class Applicants:
    def __init__(self,aname,ajobid,alocation):
        self.aname=aname
        self.ajobid=ajobid
        self.alocation=alocation
    def display(self):

        print("Applicant name:", self.aname)
        print("Applicant jobid:", self.ajobid)
        print("Applicant job location:", self.alocation)

# class 5
class Recruiter:
    recruitercount=0
    def __init__(self,rname,rdept):
        self.rname=rname
        self.__rdept=rdept # Use of a private member
        Recruiter.recruitercount+=1

    def display(self):
        print("---Interview Schedule---")
        print("Recruiter name:",self.rname)
        print("Recruiter dept:",self.__rdept) # Use of a private member

# class 6 :defines the interviewing schedule by extending Recuiter class and Applicants class
# Multiple Inheritence
class Interview(Recruiter,Applicants):
    def __init__(self,rname,rdept,aname,ajobid,alocation):
        Recruiter.__init__(self,rname,rdept)
        Applicants.__init__(self,aname,ajobid,alocation)
    def display(self):
        Recruiter.display(self)
        Applicants.display(self)

# Created instances for all classes and displaying relationships between them
# Creating objects of the parent class Employee

employee1=classEmployee("Revanth",1000,"IT")
employee2=classEmployee("Swathi",1500,"HR")
employee3=classEmployee("Sravya",2000,"Development")

# Creating objects of the Child class Fulltime
employee4=Fulltime("Vineeth",3000,"Android applications","Kansas City")

employee5=Fulltime("Ajay",2000,"IOS applications","California")

employee6=Manager("Michael Adams",10000,"Recruitment RegionalHead",10)

applicant1=Applicants("Maheshbabu",785489,"Pittsburgh")

interview1=Interview("Narasimham","Senior Recruiter","MaheshBabu",785489,"Pittsburgh")
# Calling member functions of the employee class
employee1.display()
employee2.display()
employee3.display()

print("")
print("---Fulltime employees list---")
# Calling member functions of the Full time class
employee4.display()

employee5.display()

employee6.display()

print("")
print("---Job Applicant details---")
applicant1.display()

print("")
interview1.display()
print("")
# Calculating count of employees | # Calculating average salary of the employees
print("Total number of employees:", classEmployee.empcount,"|","Average salary of all employees:",classEmployee.Totalsalary//classEmployee.empcount)
print("")
print("Total number of fulltime employees:",Fulltime.fulltimecount,"|","The average salary of fulltime employees:",Fulltime.fulltimetotalsalary//Fulltime.fulltimecount)

print("")
print("Total number of Managers:",Manager.managercount,"|","Total number of Recruiters:",Recruiter.recruitercount )
