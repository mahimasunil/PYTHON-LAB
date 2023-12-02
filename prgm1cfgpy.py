#!/usr/bin/env python
# coding: utf-8

# In[4]:


def gcd(a,b): 
    if(b==0):
        return a 
    else: return gcd(b,a%b)
num1=int(input("Enter first number:"))

num2=int(input("Enter second number:"))

gc=gcd(num1,num2)
print("gcd(num1,num2):",gc) 


# In[6]:


def hello():
    print("Hello world")
hello()
    
  


# In[8]:


def sum():
    print("sum",a+b)
a=int(input("Enter no 1:"))
b=int(input("Enter no 2:"))
sum()


# In[13]:


list=[]
n=int(input("Enter n"))
for i in range(n):
    num=int(input("Enter an integer:"))
    list.append(num);
print(list)
for i in list:
    if i%2==0:
        list.remove(i)
print("After removing even numbers")
print(list)


# In[ ]:




