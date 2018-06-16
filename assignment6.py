1. Take 10 integers from user and print it on screen
for p in range(0,10):
l.append(int(input("enter any integers:")))
print(p)
	
	
2.write an infinte loop.An infinte loop never end.condtion is always true.
     #first method
i=1
while i<10:
 print("Hello world")
print(i)
  
      #second method
i=1
while (i!=-1):
 print("Hello world")
print(i)

#3. Create a list of integer elements by user input. Make a new list which will store square of elements of previous list. 
l=[]
s=[]
for x in range(5):
    l.append(int(input("enter a number")))
for x in l:
    s.append(x**2)
print(l)
print(s)

    

#4.From a list containing ints, strings and floats, make three lists to store them separately 
l=[]
for x in range(0,3):
 x=int(input("enter number: "))
 l.append(x)
for x in range(3,6):
 x=input("enter string: ")
 l.append(x)
for x in range(6,9):
 x=float(input("enter floats:"))
 l.append(x)
print(l)
list1=[]
list2=[]
list3=[]
for x in l:
 if type(x)==int:
  list1.append(x)
 elif type(x)==str:
  list2.append(x)
 elif type(x)==float:
  list3.append(x)
 print(list1)
 print(list2)
 print(list3)
 

#5.Using range(1,101), make a list containing even and odd numbers. 
list1=[]
list2=[]
for i in range(1,101):
 if (i%2==0):
  print("even",i)
  list1.append(i)
 elif(i%2==1):
  print("odd",i)
  list2.append(i)
 print(list2)
 
#6.
num=int(input("enter the number of rows:"))
for i in range(0,10):
 for j in range(0,i):
  print("*",end="")
 print()
 
 
#7.
d={}
for x in range(5):
 keys=str(input("enter the keys:"))
 values=int(input("enter value item:"))
 d[keys]=values
print(d)


#8.
l=[]
flag=0
for x in range(5):
 x=int(input("enter the number:"))
 l.append(x)
print(l)
y=int(input("select any number you want to search:"))
for x in l:
 if x==y:
  l.remove(x)
  flag=1
print(l)
if flag==0:
 print("the number you entered is not in the list")