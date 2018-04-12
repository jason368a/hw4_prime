
# coding: utf-8

# In[3]:


def is_prime():
    num=int(input('Please type a number.'))
    if num == 2:
        return True
    for  i in range (2,num):
        if i**2 <= num and num%i ==0:
            return False             
        return True
 


# In[2]:


a=is_prime()


# In[3]:


a

