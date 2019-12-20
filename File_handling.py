

f1= open("file1.txt", 'r')
print(type(f1))


for line in f1:
   print(line,end='')
f1.close()

f2=open("file2.txt",'r')
print('\n',f2.read())
f2.close()

f1= open("file1.txt", 'r')
print('reading first 10','\n',f1.readline(10))
print('reading the next 10','\n',f1.readline(10))
print(list(f1))
f1.close()

with open("file2.txt") as f3:
   print(f3.read())

#iertate the file using readline
with open('dog_breeds.txt') as dg:
   line=dg.readline()
   while line!='':
      print(line,end='')
      line=dg.readline()

#iterate the file using readlines
with open('dog_breeds.txt','r') as dg1:
   line=dg1.readlines()
   for lines in line:
      print(lines, end='')

#the above method can be simplified as below , which is more efficient
with open('dog_breeds.txt','r') as dg1:
    for lines in line:
      print(lines, end='')

