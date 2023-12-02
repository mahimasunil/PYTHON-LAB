#!/usr/bin/env python
# coding: utf-8

# In[3]:


firstname=[]
coun=0
for i in range(0,5):
    name=input("Enter first name:")
    firstname.append(name)
print(firstname)
for i in firstname:
    coun+=i.count('a')
print("The number of occurance of 'a' in the list is",coun)


# In[ ]:


string=input("Enter a string:")
newstring=string[0]+string[1:].replace(string[0],'$')
print("The new string is",newstring)


# In[3]:


string=input("Enter a string")
newstring=string[-1]+string[1:-1]+string[0]
print("The new string is",newstring)


# In[ ]:


filename=input("Enter file name:")
ext=filename.split('.')
print("Extension of file :",ext[-1])


# In[3]:


color=input("Enter colors: ")
ncolor=color.split(',')
print("The first color is",ncolor[0])
print("The last color is ",ncolor[-1])


# In[2]:


n=input("Enter a string:")
w=n.split(" ")

print("The string is",w)
new=[]
for i in w:
    if i not in new:
        new.append(i)
print(new)
for i in new:
    count=0
    for j in w:
        if i==j:
            count=count+1
    print("The string",i,"has",count,"times words")


# In[5]:


colorlist1=input("Enter the first list of colors")
color_list1=colorlist1.split(",")
print("First list of colors",color_list1)
colorlist2=input("Enter the second list of colors")
color_list2=colorlist2.split(",")
print("second list of colors",color_list2)
diff=set(color_list1)-set(color_list2)
print("Colors from color_list1 not contained in color_list2",diff)


# In[1]:


string1=input("Enter first string:")
string2=input("Enter second string:")
string3=string2[0]+string1[1:]+" "+string1[0]+string2[1:]
print(string3)


# In[6]:


dict1={}
for i in range(0,4):
    key=input("Enter key:")
    value=input("Enter  value:")
    dict1[key]=value
print("Dictionary in ascending order:",dict(sorted(dict1.items())))
print("Dictionary in descending order:",dict(sorted(dict1.items(),reverse=True)))


# In[5]:


dict1={}
for i in range(0,3):
    key=int(input("Enter key:"))
    value=input("Enter a value:")
    dict1[key]=value
print("The first dictionary:",dict1)
dict2={}
for i in range(0,3):
    key=int(input("Enter key:"))
    value=input("Enter a value:")
    dict2[key]=value
print("The second dictionary:",dict2)
dict1.update(dict2)
print("The merged dictionary",dict1)


# In[ ]:




