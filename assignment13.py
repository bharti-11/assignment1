#Q.1- Name and handle the exception occured in the following program: 

a=3
 if a<4:
    a=a/(a-3)
     print(a)

#sol

a=3
if a<4:
 try:
    a=a/(a-3)
 except Exception:
    print("exception occurred")

#Q.2- Name and handle the exception occurred in the following program: 
l=[1,2,3]
print(l[3])
#sol  

l=[1,2,3]
try:
   print(l[3])
except Exception:
   print("exception occurred")

Q.3- What will be the output of the following code:

# Program to depict Raising Exception
 
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print "An exception"
    raise  # To determine whether the exception was raised or not
#sol

try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")
    raise  # To determine whether the exception was raised or not
	
#output
An exception
Traceback (most recent call last):
  File "n.py2", line 3, in <module>
    raise NameError("Hi there")  # Raise Error
NameError: Hi there


Q.4- What will be the output of the following code:

 # Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print "a/b result in 0"
	else:
		print c

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

#sol
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print("a/b result in 0")
	else:
		print(c)
		
# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

#output
-5.0
a/b result in 0


#Q.5- Write a program to show and handle following exceptions:
#sol 
#1. Import Error
 import error
 print("hello world")
 
#after handling
try:
 import error
 print("hello world")
except Exception:
 print("Exception occurred")
 
 
#2. Value Error
n=int(input("enter a number:"))
print("enter a number",n)

#after handling
try:
 n=int(input("enter a number:"))
 print("enter a number",n)
except Exception:
 print("Exception occurred")
 
#3.index error
l=[1,2,3]
print(l[3])

#after handling
try:
 l=[1,2,3]
 print(l[3])
except Exception:
 print("exception occurred")
   
   
   
#Q.6- Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18. 
The code must keep taking input till the user enters the appropriate age number(less than 18).

#sol

class AgeTooSmallError(Exception):
 pass
a=1
while True:
  
 print("you have to enter the age 18 or more than 18")
 try:
  a=int(input("enter the age:"))
  if a<18:
   raise  AgeTooSmallError()
  print("Correct")
  break
     
 except Exception:
   print("Incorrect Age"
 