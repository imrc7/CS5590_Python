# Create a class Employee and then do the following
# Base/Parent Class - Employee
class classEmployee:

    # Create a data members to count the number of Employees and average salary
  empcount=0
  Totalsalary=0
# Create a constructor to initialize name, family, salary, department
  def __init__(self,ename,efamily,esal,edept):
      self.ename=ename
      self.efamily=efamily
      self.esal=esal
      self.edept=edept
      classEmployee.empcount+=1
      classEmployee.Totalsalary+=esal
# Member method
  def display(self):
      print("name:",self.ename,"family:",self.efamily,"salary:",self.esal,"dept:",self.edept)


# Inheritance
# Child/Base Class - Full time Employee which inherits properties of parent class
class Fulltime(classEmployee):
    def __init__(self,n,f,s,d):
        classEmployee.__init__(self,n,f,s,d)

# Creating objects of the parent class Employee

emplpoyee1=classEmployee("Revanth","Chakilam",1000,"IT")
emplpoyee2=classEmployee("Swathi","Singh",1500,"HR")
emplpoyee3=classEmployee("Sravya","Topper",2000,"Development")

# Creating objects of the Child class Fulltime
emplpoyee4=Fulltime("Vineeth","Reddy",3000,"Recruitment")

# Calling member functions of the employee class
emplpoyee1.display()

# Calling member functions of the Full time class
emplpoyee4.display()

# Calculating count of employees
print("Total number of employees:", classEmployee.empcount)

# Calculating average salary of the employees
print("The average salary is:",classEmployee.Totalsalary//classEmployee.empcount)