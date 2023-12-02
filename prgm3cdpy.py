#!/usr/bin/env python
# coding: utf-8

# In[17]:


vowels=['a','e','i','o','u','A','E','I','O','U']
vow=[]
word=input("Enter a word:")
vow=[ i for i in word if i in vowels]
print("List of vowels in this word")
print(vow)


# In[20]:


word=input("Enter a word:")
ordinal_value=[ord(i) for i in word]
print("Ordinal values are",ordinal_value)


# In[ ]:




