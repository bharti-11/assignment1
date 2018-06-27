    # ASSIGNMENT-14 (FILE HANDLING)


#Q.1- Write a Python program to read last n lines of a file
#sol.
# f=open("test.txt",encoding="utf8")
# content=f.readlines()
# print(content)
# f.close

# n=(int(input("enter the no of lines")))
# while n>0:
   # print(content[-n])
   # n=n-1

#Q.2- Write a Python program to count the frequency of words in a file. 
#sol.
# words=open('test.txt','r',encoding="utf8").read().split() 
# print(words)
# print(type(words))
# uniqWords=sorted(set(words))
# print(type(uniqWords))
# for word in uniqWords:
    # print(words.count(word),word)


#Q.3- Write a Python program to copy the contents of a file to another file 
#sol.
# with open('test.txt','r',encoding="utf8")as f1:
   # with open('new.txt','w')as f2:0 
      # for line in f1:
         # f2.write(line)
#Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.
#sol.
# with open('test.txt','r',encoding="utf8")as f1:
   # with open('new.txt','r')as f2:
      # for line1,line2 in zip(f1,f2):
          # print(line1+line2)
#Q.5- Write a Python program to write 10 random numbers into a file. 
#     Read the file and then sort the numbers and then store it to another file.
#sol.
import random
with open("test.txt","w") as f:
    for i in range(10):
      numbers=str(random.randint(1,100))
      f.writelines(numbers+'\n')
      print(numbers)
with open("test.txt") as f1,open("new.txt",'w') as f2:
   numbers=f1.read().split()
   numbers.sort()
   print(numbers)
   for n in numbers:
      f2.write(n)  
      f2.write("\n")