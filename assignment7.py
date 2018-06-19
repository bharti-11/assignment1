#Q.1- Create a function to calculate the area of a circle by taking radius from user.
def area():
 pi=3.14
 rad=float(input("enter the radius"))
 area=(pi*rad*rad)
 print(area)
area()


#Q.2- Write a function “perfect()” that determines if parameter number is a perfect number.
      #Use this function in a program that determines and prints all the perfect numbers between 1 and 1000. 
     #[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number.
      # E.g., 6 is a perfect number because 6=1+2+3].
def perfect(n):
    sum=0
	for x in range(i,n):
	    if n%x==0:
		   sum=sum+x
		   
    if sum==n:
	   print("perfect number",n)
for x in range(1,1001):
    perfect(x)
	  
	  
#Q.3- Print multiplication table of 12 using recursion
 def table(x):
     print(n*1)
     i=i+1
	 ifi<=10:
 table(12,1)
 
 
#Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.
def power(a,b):
 if b==1:
  return(a)
 if(b!=1:
  return(a*power(a,b-1))
 a=int(iput("enter the base")):
 b=int(input("enter exponential value")):
 print("result:",power(a,b))


#Q.5- Write a function to find factorial of a number but also store the factorials calculated in a dictionary
def factorial (n):
    if(n<=1):
	    return 1
	else:
	    return(n*factorial(n-1))
n=int(input("enter number:"))
print("factorial:")
print(factorial(n))
c=factorial(n)
l="output"
d={}
d{1}=c
print(d)