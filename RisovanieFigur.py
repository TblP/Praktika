#!/usr/bin/env python
# coding: utf-8

# In[75]:


import numpy as np
import cv2
from matplotlib import pyplot as plt


# In[85]:


img = np.zeros((512,512,3), np.uint8)
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
img = cv2.rectangle(img,(0,0),(511,511),(145,255,245),5)
img = cv2.circle(img,(440,40), 35, (0,0,255), -1)
img = cv2.ellipse(img,(400,100),(100,70),0,0,180,255,-1)
pts = np.array([[20,15],[30,20],[80,30],[80,5]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(154,255,255))
font  =  cv2 . FONT_HERSHEY_SIMPLEX 
cv2 . putText ( img , 'Doka2' , ( 10 , 500 ),  font ,  4 , ( 255 , 255 , 255 ), 7 , cv2 . LINE_AA )
cv2 . imwrite ( 'M:\img.png' ,img )
cv2 . imshow ('M:\img.png', img )
cv2.waitKey(0)
cv2.destroyAllWindows ()


# In[ ]:





# In[ ]:




