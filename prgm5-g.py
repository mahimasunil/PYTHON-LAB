#!/usr/bin/env python
# coding: utf-8

# In[5]:


def modify(string):
    if string .endswith("ing"):
        newstring=string+"ly"
    else:
        newstring=string+"ing"
    return newstring
n=input("Enter a string:")
result=modify(n)
print("The new string is ",result)


# In[ ]:




