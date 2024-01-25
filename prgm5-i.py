#!/usr/bin/env python
# coding: utf-8

# In[20]:


num=int(input("Enter number:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*" , end="")
    print(" ")
for i in range(num,0,-1):
    for j in range(0,i-1):
        print("*" , end="")
    print(" ")
        
        






