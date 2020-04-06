#!/usr/bin/env python
# coding: utf-8

# #### 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# In[39]:


l=[]
for x in range(2000,3200):
    if (x%5==0) and (x%7==0):
        l.append(x)
print(l)       


# #### 2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.

# In[35]:


first_name = input("Enter First Name ")
last_name = input("Enter Last Name ")
print("Hi"+" "+last_name+" "+first_name)


# #### 3. Write a Python program to find the volume of a sphere with diameter 12 cm.

# In[18]:


diameter = 12
radius = 12/2
pi = 3.141
print(radius)
volume = (4/3)*pi* radius**3
print(volume)


# #### 4. Write a program which accepts a sequence of comma-separated numbers from console and generate a list.

# In[26]:


Val = input("Enter comma seprated numbers :")
l = Val.split(",")
print("Generated List :",l)


# #### 5. Create the below pattern using nested for loop in Python.

# 
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# In[67]:


n = 5
for i in range(0,n):
    for j in range(i+1):
        print("*",end =' ')
    print("")
#print("over")
for i in range(n, 0 , -1):
    for j in range(0, i-1 ):
        print("* ", end="")
    print("")    
       


# #### 6. Write a Python program to reverse a word after accepting the input from the user.

# In[34]:


Name_val = input("Enter Name :")
print("Input word:",Name_val)
new_str=''
for i in range(len(Name_val)-1,-1,-1):
    new_str+=Name_val[i]
print("Output Word : ",new_str)


# #### 7. Write a Python Program to print the given string in the format specified in the sample output.
# 

# In[70]:


string = "WE, THE PEOPLE OF INDIA,{}having solemnly resolved to constitute India into a SOVEREIGN,{}SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC{}and to secure to all its citizens{}"
print(string.format('\n\t','!\n\t\t','\n\t\t',':'))


# In[ ]:




