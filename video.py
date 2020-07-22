#!/usr/bin/env python
# coding: utf-8

# In[1]:


import  numpy  as  np 
import  cv2 


# In[2]:


cap  =  cv2.VideoCapture ( 'M:\TT.mp4' ) 


# In[3]:



fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('M:\TT2.mp4',fourcc, 30.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()


# In[70]:





# In[ ]:





# In[ ]:




