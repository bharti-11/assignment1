#Q1.
#SOL.
year=int(input("enter the year:"))
if ((year%400==0)or((year%4==0)and(year%100!=0))):
  print("%d is a leap year"%year)
else:
  print("%d is not a leap year"%year)

  
#Q2
#SOL 
l=int(input("enter the length: "))
b=int(input("enter the breadth: "))
if l==b:
 print("square")
else:
 print("rectangle")
#Q3
#SOL
x=int(input("enter the age of x: "))
y=int(input("enter the age of y: "))
z=int(input("enter the age of z: "))
if x>=y and x>=z:
 print("x is oldest")
elif y>=z and y>=x:
 print("y is oldest")
elif x>=y and x>=z:
 print("z is oldest")
else:
 print("all are of the same age")
if x<=y and x<=z:
 print("x is younger")
elif y<=x and y<=z:  
 print("y is younger")
elif z<=x and z<=y:
 print("z is younger")
else:
print("all are of the same age")
 

#Q4
#SOL
if n<=50:
 print("no prize") 
elif n<=150:
 print("wooden prize") 
elif n<=180:
 print("book")
else:
 print("choclates") 
#Q5
#SOL 
qty=int(input("enter the quantity: "))
totalexp=qty*100
if totalexp>1000:
 dis=totalexp*0.1
 totalexp=totalexp-dis
 print("cost is %d" %totalexp)
else:
 print("total cost is %d" %totalexp)
 