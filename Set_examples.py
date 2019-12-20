
st1=set()
st1={"a","b","c","c"}
st1.add(1)
st1.add((1,2))
#st1=int(input('Enter the values for set: '))
print(st1)
print('Letters are: ',st1)

a=['bb','cc','dd','ee']
str="veena"

print(a[:])
print(str[:])

x=[10,[3.141,20,[30,'baz',2.718]],'foo']

print(x[1][2][1:])

x[2]=[]
print(x)

x.extend(['d'])
print(x)

x+='ef'
print(x)

print(x[-1:])
print(x[:-1])

a=[1,2,7,8]
a[2:2]=[3,4,5,6]
print(a)