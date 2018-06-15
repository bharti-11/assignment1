             # TUPLES
#Write a program to creat a tuple with different data type.
t=('a','b',1,3.5,2,"bharti")
print(t)

#Find the length of the tuples.
t=(1,2,3,4)
print(len(t))

#Find largest and smallest element of  a tuples.
#for smallest
t=(2,2,4,5)
print(min(t))
#for largest
print(max(t))

#Write a program to find the product of all element of a tuples.
t=(1,2,3,4)
p=1
p=p*t[0]
p=p*t[1]
p=p*t[2]
p=p*t[3]
print(p)

          #SETS
#Create two sets using user defind values.
s1=set(input("enter a number"))
print(s1)
s2=set(input("enter a number"))
print(s2)
#Calculate difference between two sets.
s1=set([1,2,4,5])
s2=set([2,3,4,6])
print(s1-s2)
#Compare two sets.	     

#Print the result of intersection of two sets.
s1=set([1,2,3,4])
s2=set([2,4,5,6])
print(s1&s2)

         #DICTIONARY
#Create a two dictionary to store name and marks of ten students.
d={}
name=input("enter your name:")
marks=int(input("enter your marks:"))		 
d[name]=marks
name=input("enter your name:")
marks=int(input("enter your marks:"))		 
d[name]=marks
name=input("enter your name:")
marks=int(input("enter your marks:"))		 
d[name]=marks
name=input("enter your name:")
marks=int(input("enter your marks:"))		 
d[name]=marks
name=input("enter your name:")
marks=int(input("enter your marks:"))		 
d[name]=marks
name=input("enter your name:")
marks=int(input("enter your marks:"))		 
d[name]=marks
name=input("enter your name:")
marks=int(input("enter your marks:"))		 
d[name]=marks
name=input("enter your name:")
marks=int(input("enter your marks:"))		 
d[name]=marks
name=input("enter your name:")
marks=int(input("enter your marks:"))		 
d[name]=marks
name=input("enter your name:")
marks=int(input("enter your marks:"))		 
d[name]=marks
print(d)

#Sort the dictionary created in previous according to the marks.
values=list(d.values())
print(values)
values.sort()
print(values)




#Count the number of occurence of each letter in word "MISSISSIPPI".store count of  every letter with the letter in a dictionary
t=list("MISSISSIPPI")
d={}
d['M']=t.count('M')
d['I']=t.count('I')
d['S']=t.count('S')
d['P']=t.count('P')
print(d)



                        
