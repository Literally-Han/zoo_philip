#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

get_ipython().run_line_magic('precision', '3')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


x_set=np.array([1,2,3,4,5,6])


# In[5]:


def f(x):
    if x in x_set:
        return x/21
    else:
        return 0


# In[7]:


X=[x_set,f]


prob=np.array([f(x_k) for x_k in x_set])
dict(zip(x_set,prob))


# In[10]:


fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(111)
ax.bar(x_set,prob)
ax.set_xlabel('value')
ax.set_ylabel('probability')

plt.show()


# In[11]:


np.all([prob>=0])


# In[12]:


np.sum(prob)


# In[13]:


a={'사과':1,'딸기':5,'귤':10}


# In[14]:


a


# In[15]:


a={('초콜릿',200):20,('마카롱',500):15,('쿠키',300):30}
a


# In[16]:


a={'사과':1,'딸기':5,'귤':10}
v1=a['딸기']
v1


# In[18]:


v2=a['레몬']
v2


# In[19]:


f1='딸기'in a
f1


# In[20]:


f2='레몬' not in a
f2


# In[21]:


f3='레몬' in a


# In[22]:


v1=a.get('딸기')
v1


# In[23]:


v2=a.get('레몬')
v2


# In[24]:


a={'초콜릿':1,'마카롱':2,'쿠키':3}
a['초콜릿']='One'
a['마카롱']='Two'
a['쿠키']='Three'
a


# In[25]:


d=dict(초콜릿=20,마카롱=15,쿠키=30)
d


# In[26]:


ket=['초콜릿','마카롱','쿠키']
value=[20,15,30]
d=dict(zip(ket,value))
d


# In[27]:


d=dict([('초콜릿',20),('마카롱',15),('쿠키',30)])
d


# In[28]:


def F(x):
    return np.sum([f(x_k) for x_k in x_set if x_k <=x])


# In[29]:


F(3)


# In[30]:


y_set=np.array([2 * x_k + 3 for x_k in x_set])
prob=np.array([f(x_k) for x_k in x_set])
dict(zip(y_set,prob))


# In[31]:


np.sum([x_k * f(x_k) for x_k in x_set])


# In[32]:


np.random.choice(5,5,replace=False)


# In[33]:


np.array([1,3,0,3,2])


# In[34]:


np.random.choice(5,3,replace=False)


# In[35]:


np.random.choice(5,10)


# In[36]:


np.random.choice(5,10,p=[0.1,0,0.3,0.6,0])


# In[37]:


def E(X,g=lambda x: x):
    x_set,f=X
    return np.sum([g(x_k)*f(x_k) for x_k in x_set])


# In[38]:


E(X)


# In[39]:


E(X,g=lambda x: 2*x +3)


# In[40]:


2*E(X)+3


# In[41]:


strings=['hyeja','parkhyeja','youngtae','kimyoungtae','bbangte']


# In[42]:


strings.sort(key=lambda x: len(set(list(x))))


# In[43]:


strings


# In[44]:


2*E(X)+3


# In[45]:


mean=E(X)
np.sum([(x_k-mean)**2*f(x_k) for x_k in x_set])


# In[46]:


mean=E(X)
np.sum([(x_k-mean)**2*f(x_k) for x_k in x_set])


# In[47]:


def V(X,g=lambda x: x):
    x_set,f=X
    mean = E(X,g)
    return np.sum([g(x_k)-mean**2*f(x_k) for x_k in x_set])


# In[48]:


V(X)


# In[49]:


V(X,lambda x:2*x+3)


# In[50]:


2**2 * V(X)


# In[51]:


2**2*V(X)


# In[54]:


x_set=np.arange(2,13)
y_set=np.arange(1,7)


# In[55]:


def f_XY(x,y):
    if 1<=y<=6 and 1 <= x - y <=6:
        return y*(x-y)/441
    else:
        return 0


# In[56]:


XY=[x_set,y_set,f_XY]


# In[61]:


prob = np.array([[f_XY(x_i,y_j) for y_j in y_set]
                 for x_i in x_set])
fig = plt.figure(figsize=(10,8))
ax=fig.add_subplot(111)

c=ax.pcolor(prob)
ax.set_xticks(np.arange(prob.shape[1])+0.5,minor = False)
ax.set_yticks(np.arange(prob.shape[0])+0.5,minor = False)
ax.set_xticklabels(np.arange(1,7),minor=False)
ax.set_yticklabels(np.arange(2,13),minor=False)
ax.invert_yaxis()
ax.xaxis.tick_top()
fig.colorbar(c,ax=ax)
plt.show()


# In[62]:


np.all(prob>=0)


# In[63]:


np.sum(prob)


# In[66]:


np.all(prob>=0)


# In[65]:


np.sum(prob)


# In[74]:


def f_X(x):
    return np.sum([f_XY(x,y_k) for y_k in y_set])


# In[75]:


def f_Y(x):
    return np.sum([f_XY(x_k,y) for x_k in x_set])


# In[76]:


def f_y(y):
    return np.sum([f_XY(x_k,y) for x_k in x_set])


# In[77]:


X=[x_set,f_X]
Y=[y_set, f_Y]


# In[81]:


prob_x=np.array([f_X(x_k) for x_k in x_set])
prob_y= np.array([f_y(y_k) for y_k in y_set])

fig=plt.figure(figsize=(12,4))
ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)

ax.bar(x_set,prob_x)
ax1.set_title('X_mariginal probability distribution')
ax1.set_xlabel('X_value')
ax1.set_ylabel('probability')
ax1.set_xticks(x_set)

ax2.bar(y_set,prob_y)
ax2.set_title('Y_mariginal probaility distribution')
ax2.set_xlabel('Y_value')
ax2.set_ylabel('probability')

plt.show()


# In[82]:


np.sum([x_i*f_XY(x_i,y_j) for x_i in x_set for y_j in y_set])


# In[83]:


def E(XY,g):
    x_set, y_set,f_XY=XY
    return np.sum([g(x_i,y_j)*f_XY(x_i,y_j)
    for x_i in x_set for y_j in y_set])


# In[84]:


mean_X=E(XY,lambda x,y:x)
mean_X


# In[86]:


mean_Y=E(XY,lambda x, y:y)
mean_Y


# In[87]:


a,b=2,3


# In[91]:


E(XY,lambda x, y: a*x+b*y)


# In[90]:


a*mean_X+b*mean_Y


# In[92]:


np.sum([(x_i-mean_X)**2*f_XY(x_i,y_j)
        for x_i in x_set for y_j in y_set])


# In[94]:


def V(XY,g):
    x_set,y_set,f_XY=XY
    mean=E(XY,g)
    return np.sum([(g(x_i,y_j)-mean)**2*f_XY(x_i,y_j)
    for x_i in x_set for y_j in y_set])


# In[95]:


var_X=V(XY,g=lambda x, y:x)
var_X


# In[96]:


var_Y=V(XY,g=lambda x, y: y)
var_Y


# In[97]:


def Cov(XY):
    x_set, y_set, f_XY=XY
    mean_X=E(XY,lambda x, y:x)
    mean_Y=E(XY,lambda x , y:y)
    return np.sum([(x_i-mean_X)*(y_j-mean_Y)*f_XY(x_i,y_j)
    for x_i in x_set for y_j in y_set])


# In[98]:


cov_xy=Cov(XY)
cov_xy


# In[99]:


V(XY,lambda x, y: a*x + b*y)


# In[101]:


a**2 * var_X + b**2 * var_Y + 2*a*b * cov_xy


# In[102]:


cov_xy/np.sqrt(var_X*var_Y)


# In[ ]:




