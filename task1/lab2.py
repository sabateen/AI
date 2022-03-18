#!/usr/bin/env python
# coding: utf-8

# In[6]:


#read 1st number 
num1 = input("plz enter 1st number : ")
#read 2nd number 
num2 = input ("plz enter 2nd number : ")
#read oper
op = input ("plz enter your opera : ")

#convert numbers 
num1 = float(num1)
num2 = float(num2)
if op == '+' : 
    res = num1 + num2
elif op == '-' :
    res = num1 - num2
elif op == '*' :
    res = num1 * num2 
elif op == '/' :
    res = num1 / num2
print (res)


# In[ ]:




