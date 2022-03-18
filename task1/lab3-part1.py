#!/usr/bin/env python
# coding: utf-8

# In[1]:


def max_tow_numbers(num1,num2) :
    if num1 > num2 : 
        return(num1)
    else :
        return(num2)
def max_three_numbers (num1,num2,num3):
    m = max_tow_numbers(num1,num2) 
    fin = max_tow_numbers(m,num3)
    
    return(fin)
num1 = input('plz enter 1st number : ')
num2 = input('plz enter 2nd number : ')
num3 = input('plz enter 3rd number : ')

res = max_three_numbers(num1,num2,num3)

print('max of three numbers is : ',res)


# In[ ]:





# In[ ]:




