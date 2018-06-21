#Q.1- Create a class Animal as a base class and define method animal_attribute.
#     Create another class Tiger which is inheriting Animal and access the base class method.

class animal: 

  def method_animal(self):
        print("tiger")
		
class tiger(animal):
  pass
a=animal()
a.method_animal()



#Q.2- What will be the output of following code.

class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print(a.f(), b.f())
print(a.g(), b.g())

#OUTPUT=A B
 #      A B


 
#Q.3- Create a class Cop. Initialize its name, age , work experience and designation.
#     Define methods to add, display and update the following details.
#     Create another class Mission which extends the class Cop. 
#     Define method add_mission _details. 
#     Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission.
class Cop:
  def __init__( self,name, age , work_experience,designation):
    self.name=name
    self.age=age
    self.work_experience=work_experience
    self.designation=designation


  def display(self):
    print("details")
    print(self.name)
    print(self.age)
    print(self.work_experience)
    print(self.designation)
 
  def update( self,name, age , work_experience,designation):
    self.name=name
    self.age=age
    self.work_experience=work_experience
    self.designation=designation
   
   
class mission(Cop):
    fighter_plans=10
    tankers=3
    def add_mission_details(self):
      print("number of fighter plans ",self.fighter_plans)
      print("number of tankers",self.tankers)

name=input("Name:")
age=int(input("Age:"))
work_experience=input("Work Experience:")
designation=input("Designation:")

a=mission(name,age,work_experience,designation)
print("")
a.display()
print("")
a.add_mission_details()
print("")
a.update(input("Name:"),int(input("Age:")),input("Work_Experience:"),input("Designation:"))
print("")
a.display()
a.add_mission_details()  
  
 
 #Q.4- Create a class Shape.Initialize it with length and breadth Create the method Area.
 #     Create class rectangle and square which inherits shape and access the method Area.
 class Shape:
 def __init__(self,length,breadth):
  self.length=length
  self.breadth=breadth
  
  
 def area(self):
  self.area=self.length*self.breadth
  
  
class square(Shape):
 def area_sqr(self):
  print("area of square:", self.area)
  
  
class rectangle(Shape):
 def area_rect(self):
  print("area of rectangle:", self.area)

length=int(input("enter the length: "))
breadth=int(input("enter the breadth: "))
c = rectangle(length,breadth)
b = square(length,breadth)
if length == breadth:
    b.area()
    b.area_sqr()
else:
    c.area()
    c.area_rect()
