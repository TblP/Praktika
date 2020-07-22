#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2

import numpy as np

cap = cv2.imread("M:\FG.JPG")


# In[4]:


while(1):
 
    
    hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([70, 0 , 0])
    upper_blue = np.array([80, 200, 200])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(cap,cap, mask = mask)
  
    cv2.imshow('frame',cap)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    if cv2 . waitKey ( 0 ):
        break
    

cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:




