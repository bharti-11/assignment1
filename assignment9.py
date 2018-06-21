#Q.1-Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
class Circle():
    def __init__(self, r):
        self.radius = r

    def getarea(self):
        return self.radius**2*3.14
    
    def getcircumference(self):
        return 2*self.radius*3.14

NewCircle = Circle(8)
print(NewCircle.getarea())
print(NewCircle.getcircumference())



#Q.2- Create a Student class and initialize it with name and roll number. Make methods to :
#1. Display - It should display all informations of the student.
class student:
  def __init__ (self,name,roll):
	  self.name=name
	  self.roll=roll
  def display(self):
          print(self.name,self.roll)	  
s1=student(226,"bharti")         
s1.display()

#Q.3- Create a Temprature class. Make two methods :
#1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
#2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
 
class temperature:
  def __init__(self,celsius,fahrenheit):
    self.fahrenheit=fahrenheit
	self.celsius=celsius
  def getfahrenheit(self):
    print("fahrenheit",(1.8* self.celsius)+32
  def getcelsius(self):
    print("celsius",(self.fahrenheit-32)*05.5)
		
fahrenheit=float(input("enter fahrenheit"))
celsius=float(input("enter celsius"))
t=temperature(celsius,fahrenheit)
t.getfahrenheit()
t.getcelsius()
 
 

#**Q.4- Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
#Make methods to 
#1. Display-Display the details.
#2. Update- Update the movie details.

class MovieDetails():
    def __init__ (self,movie_name,artist_name,releasing_date,ratings):
        self.movie_name=movie_name
        self.artist_name=artist_name
        self.releasing_date=releasing_date
        self.ratings=ratings

    def update(self, movie_name, artist_name, releasing_date, ratings):
        self.movie_name = movie_name
        self.artist_name = artist_name
        self.releasing_date = releasing_date
        self.ratings = ratings

    def show(self):
         print(self.movie_name,self.artist_name,self.ratings,self.releasing_date)
movie_name=input("enter movie name: ")
artist_name=input("enter artist name: ")
ratings=int(input("enter the ratings out of 5: "))
releasing_date=input("enter releasing date: ")
s1=MovieDetails(movie_name,artist_name,ratings,releasing_date)
s1.show()
s1.update("abcd","dance","5","1999")
s1.show()





#Q.5- Create a class Expenditure and initialize it with expenditure,savings.Make the following methods. 
#1. Display expenditure and savings 
#2. Calculate total salary
#3. Display salary

class expenditure:
  def __init__ (self,expenditure,saving):
   self.expenditure = expenditure
   self.saving = saving
  def getdisplay(self):
   print("expend is",self.expenditure,"saving is",self.saving)
  def getcalculation(self):
   print("total salary=",self.expenditure+self.saving)
c=expenditure(50000,70000)
c.getdisplay()
c.getcalculation()
