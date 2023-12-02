#!/usr/bin/env python
# coding: utf-8

# In[2]:


def factorial(n):
    fact=1
    if n<0:
        print("Invalid input")
        return
    elif n==0:
        return 1
    else:
        for i in range(1,n+1):
            fact=fact*i
        return fact
num=int(input("Enter number"))
result=factorial(num)
print("Factorial of",num,"is",result)


# In[7]:


num=int(input("Enter number:"))
def fibonacci(n):
    a=0
    b=1
    fib=0
    if n==0:
        return a
    elif n==1:
        return b
    else:
        print(a)
        print(b)
        for i in range(2,n+1):
            fib=a+b
            a=b
            b=fib
            print(fib)
print("Fibonacci series for given number is:")
fibonacci(num)


# In[ ]:





# In[11]:


list1=[]
total=0
for i in range(0,4):
    n=int(input("Enter number:"))
    list1.append(n)
print(list1)
for i in list1:
    total=total+i
print("Sum of all items in the list is",total)


# In[ ]:


square=[]
initial=int(input("Enter initial number"))
final=int(input("Enter final numbers"))
for i in range(initial,final+1):
    sqr=i*i
    d=sqr
    while(d>0):
        digit=d%10
        if digit%2==0:
            square.append(sqr)
        else:
            break
print(square)
    


# In[ ]:




