#!/usr/bin/env python
# coding: utf-8

# In[28]:


#import matplotlib
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[24]:


#create a figure object called figure, set the axes at (0,0,1,1) and set the title to 'Meow', plot two arrays of 5 integers 
figure = plt.figure()
axes = figure.add_axes([0,0,1,1])
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('Meow')
x = [1,2,3,4,5]
y = [6,7,8,9,10]
axes.plot(x,y)


# In[25]:


#set the x limits from 0 to 5 and y limits from 0 to 10
figure = plt.figure()
axes = figure.add_axes([0,0,1,1])
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('Meow')

axes.set_xlim([0,5])
axes.set_ylim([0,10])

x = [1,2,3,4,5]
y = [6,7,8,9,10]
axes.plot(x,y)


# In[14]:


#create subplots of 1 row and 2 columns
figure, axes = plt.subplots(1,2)


# In[16]:


#set the color of the first column to red and that of the second column to blue
figure, axes = plt.subplots(1,2)
axes[0].plot(x,y, color='blue')
axes[1].plot(x,y, color='red')


# In[27]:


#change the figure size to 10x2
figure, axes = plt.subplots(1,2, figsize=(10,2))
axes[0].plot(x,y, color='blue')
axes[1].plot(x,y, color='red')


# In[ ]:




