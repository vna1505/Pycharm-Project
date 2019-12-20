'''
n=int(input('Enter the dimension of the array: '))
# a=[[0]*n] * n

a=[]
for i in range(n):
    a.append([0]*n)

print(a)
for i in range(n):
    for j in range(n):
        if (i==j):
            a[i][j]=1
        if(i>j):
            a[i][j]=0
        if (i<j):
            a[i][j]=2

for i in range(n):
    print(a[i])
 '''

ary=[[1,0,3], [2,3,4,56]]
print(ary[0])
print(ary[1])
print(ary[1][3])
print(ary)
for i in ary:
            print(i)

for i in ary:
    for j in i:
        print (j,end=' ' )

for i in range(ary):
    for j in range(ary):
        print(ary[i][j])



