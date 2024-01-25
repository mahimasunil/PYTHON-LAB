#!/usr/bin/env python
# coding: utf-8

# In[5]:


words=[]
def longest(word):
    lw=len(word[0])
    for i in word:
        current=len(i)
        if current>lw:
            lw=current
    print("The length of the longest word is",lw)
for i in range(0,3):
    n=input("Enter word:")
    words.append(n)
longest(words)


# In[ ]:




