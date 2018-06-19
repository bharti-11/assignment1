#Q.1- What is Time Tuple.
import time 
print(time.gmtime())
#Q.2- Write a program to get formatted time.
import time
print(time.asctime(time.localtime(time.time())))


#Q.3- Extract month from the time.
import datetime
print(datetime.date.today())
d= datetime.date.today()
print(d.month)


#Q.4- Extract day from the time.
import datetime
print(datetime.date.today())
d= datetime.date.today()
print(d.day)


#Q.5- Extract date (ex : 11 in 11/01/2021) from the time.

import time
t=time.gmtime()
date=t[4]
print("the current date is:",date)

#Q.6- Write a program to print time using localtime method.
import time
print(time.localtime())

#Q.7- Find the factorial of a number input by user using math package functions.
import math
print(math.factorial(int(input("enter a number:"))))

#Q.8- Find the GCD of a number input by user using math package functions.
x=int(input("enter a number:"))
y=int(input("enter a number:"))
import math
print(math.gcd(x,y))

#Q.9- Use OS package and do the following tasks: 

1. Get current working directory.
import os
print(os.getcwd)

2. Get the user environment.
import os
print(os.environ)