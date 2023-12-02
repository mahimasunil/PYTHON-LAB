#!/usr/bin/env python
# coding: utf-8

# In[9]:


current=int(input("Enter the current year"))
final=int(input("Enter the final year"))
future=[]
for i in range(current,final+1):
    if(i%4==0 and i%100!=0)or(i%400==0):
        future.append(i);
print("Leap year",future)


# In[15]:


list=[]
for i in range(0,5):
    n=int(input("Enter integers"))
    list.append(n)
print(list)
list=[i for i in list if i>0]
print("Positive number",list)
                                                


# In[1]:


list=[]
square=[]
for i in range(0,5):
    n=int(input("Enter integers"))
    list.append(n)
print(list)
square=[i*i for i in list]
print("square list of given list",square)
         
         


# 
# 
# 
