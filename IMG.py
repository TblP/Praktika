#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import cv2
from matplotlib import pyplot as plt


# In[9]:


img  =  cv2.imread ( 'M:\klinok.jpg' , 0 )


# In[10]:


cv2.namedWindow ( 'M:\klinok.jpg' ,  cv2.WINDOW_NORMAL ) 
cv2.imshow ( 'M:\klinok.jpg' , img ) 
cv2.waitKey ( 0 ) 
cv2.destroyAllWindows ()


# In[13]:


plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([]) 
plt.show()


# In[ ]:




