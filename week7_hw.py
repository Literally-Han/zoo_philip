#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

get_ipython().run_line_magic('precision', '3')
get_ipython().run_line_magic('matplotlib', 'inline')
    


# In[5]:


x_set=np.array([1,2,3,4,5,6])


# In[6]:


def f(x):
    if x in x_set:
        return x/21
    else:
        return 0
        


# In[7]:


X=[x_set,f]


# In[8]:


prob=np.array([f(x_k) for x_k in x_set])
dict(zip(x_set,prob))


# In[10]:


fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(111)
ax.bar(x_set,prob)
ax.set_xlabel('value')
ax.set_ylabel('probability')

plt.show()


# In[12]:


np.all([prob>=0])


# In[13]:


np.sum(prob)


# In[14]:


a={'사과':1,'딸기':5,'귤':10}


# In[15]:


a


# In[17]:


a={('초콜릿',200):20,('마카롱',500):15,('쿠키',300):30}
a


# In[21]:


a={'사과':1,'딸기':5,'귤':10}
v1=a['딸기']
v1


# In[22]:


v2=a['레몬']
v2


# In[23]:


f1='딸기'in a
f1


# In[24]:


f2='레몬' not in a
f2


# In[25]:


f3='레몬' in a


# In[26]:


v1=a.get('딸기')
v1


# In[27]:


v2=a.get('레몬')
v2


# In[28]:


a={'초콜릿':1,'마카롱':2,'쿠키':3}
a['초콜릿']='One'
a['마카롱']='Two'
a['쿠키']='Three'
a


# In[29]:


d=dict(초콜릿=20,마카롱=15,쿠키=30)
d


# In[30]:


ket=['초콜릿','마카롱','쿠키']
value=[20,15,30]
d=dict(zip(ket,value))
d


# In[31]:


d=dict([('초콜릿',20),('마카롱',15),('쿠키',30)])
d


# In[32]:


def F(x):
    return np.sum([f(x_k) for x_k in x_set if x_k <=x])


# In[33]:


F(3)


# In[35]:


y_set=np.array([2 * x_k + 3 for x_k in x_set])
prob=np.array([f(x_k) for x_k in x_set])
dict(zip(y_set,prob))


# In[39]:


np.sum([x_k * f(x_k) for x_k in x_set])


# In[41]:


np.random.choice(5,5,replace=False)


# In[43]:


np.array([1,3,0,3,2])


# In[46]:


np.random.choice(5,3,replace=False)


# In[47]:


np.random.choice(5,10)


# In[49]:


np.random.choice(5,10,p=[0.1,0,0.3,0.6,0])


# sample=np.random.choice(x_set,int(1e6),p=prob
# np.mean(sample)

# In[52]:


def E(X,g=lambda x: x):
    x_set,f=X
    return np.sum([g(x_k)*f(x_k) for x_k in x_set])


# In[53]:


E(X)


# In[54]:


E(X,g=lambda x: 2*x +3)


# In[56]:


2*E(X)+3


# In[59]:


strings=['hyeja','parkhyeja','youngtae','kimyoungtae','bbangte']


# In[60]:


strings.sort(key=lambda x: len(set(list(x))))


# In[61]:


strings


# In[62]:


2*E(X)+3


# In[64]:


mean=E(X)
np.sum([(x_k-mean)**2*f(x_k) for x_k in x_set])


# In[66]:


mean=E(X)
np.sum([(x_k-mean)**2*f(x_k) for x_k in x_set])


# In[67]:


def V(X,g=lambda x: x):
    x_set,f=X
    mean = E(X,g)
    return np.sum([g(x_k)-mean**2*f(x_k) for x_k in x_set])


# In[68]:


V(X)


# In[69]:


V(X,lambda x:2*x+3)


# In[70]:


2**2 * V(X)


# In[71]:


2**2*V(X)


# In[ ]:




