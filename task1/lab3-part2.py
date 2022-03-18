#!/usr/bin/env python
# coding: utf-8

# In[2]:


def uniqelist(nonunique) :
    res = []
    for n in nonunique : 
        if n not in res :
            res.append(n)
    return(res)
numbers = [1,2,3,4,3,5,6,7,7,7,8,9]
result = uniqelist(numbers)
print (result)


# In[ ]:




