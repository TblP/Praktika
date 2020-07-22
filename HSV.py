#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import cv2
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print (flags)
img = cv2.imread("M:\klinok.jpg")
window_name = 'Image'
image = cv2.cvtColor( img , cv2.COLOR_BGR2HSV)
cv2.imshow( window_name, image)
cv2 . waitKey ( 0 ) 
cv2 . destroyAllWindows ()
cv2.imwrite("M:\image.png", image)


# In[ ]:





# In[ ]:





# In[ ]:




