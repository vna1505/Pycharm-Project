
from  functools import lru_cache


'''Factorial of n number'''


def fact(n):

    if n==1:
        return 1
    else:
        print('n is ', n)
        return n*fact(n-1)


print(fact(int(input('Enter the number for factorial:'))))

'''Sum till 10 using recursive '''

def sum_recur(num,tot):

    if num == 11:
        return print('Sum till 10 is :', tot)
    else:
        return sum_recur(num +1, tot+num)

print(sum_recur(1,0))

''' Fibonacci using recursive 

def fibo_recur(prev):
    if prev==0:
        return 0
    elif prev==1:
        return 1
    else:
        return fibo_recur(num-1) + fibo_recur(num-2)


num=int(input('Enter the number for fibonacci:'))

print(fibo_recur(num))
'''

def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return print(first_child)
    else:
        return print(second_child)

parent(1)