import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('M:\j.png',0)
kernel = np.ones((9,9),np.uint8)
#erosion = cv2.erode(img,kernel,iterations = 1)
#dilation = cv2.dilate(img,kernel,iterations = 1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
tophat  =  cv2 . morphologyEx ( img ,  cv2 . MORPH_TOPHAT ,  kernel )
blackhat  =  cv2 . morphologyEx ( img ,  cv2 . MORPH_BLACKHAT ,  kernel )
titles = ['Original Image', 'top','black', 'gradient']
images = [img, tophat, blackhat,gradient]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(0)