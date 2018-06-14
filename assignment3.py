#Q1:Creat a list with use-defind inputs.
x=input("enter the number")
y=input("enter the number")
z=input("enter the number")
u=input("enter the number")
l=[x,y,z,u]
print(l)
#Q2:Add the following list to above created list:
#         ['google','apple','microsoft','tesla']
l2=['google','apple','microsoft','tesla']
print(l.extend(l2))
print(l)

#Q3:Count the number of time an object occurs in the list.
l=[1,3,3,3,3,4,5,6]
print(l.count(3))

#Q:4Creat the number of list and short this in ascending order.
l=[5,2,1,4,3]
l.sort()
print(l)

#Q5:given are two one-dimensional array A and B which are unsorted in ascending order.write a program to merge them into a single sorted array C that contains every item from array A and B ,in ascending order list
A=[3,5,2,7]
print(A)
B=[1,3,7,4]
print(B)
A.sort()
print(A)
B.sort()
print(B)
C=(A,B)
print(C)
C=A+B
print(C)
C.sort()
print(C)

#Q6:Impliment stack and queue.
#for stack
l=[1,2,3,4,5]
print(l.pop())
print(l)
#for queue
l=[1,2,3,4,5]
print(l)
l.reverse()
print(l)
print(l.pop())
print(l)

#Q7: count even and odd in a list.
n=int(input("enter a number: "))
if (n % 2)==0:
 print("n is even")
else:
 print("n is odd")
