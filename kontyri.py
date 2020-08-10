import numpy as np
import cv2

"""im = cv2.imread('M:\FS.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#img = cv2.drawContours(imgray, contours, -1, (0,255,0), 3)
img = cv2.drawContours(imgray, contours, 4, (0,255,0), 3)
#cnt = contours[4]
#img = cv2.drawContours(im, [cnt], 0, (0,255,0), 3)
cv2.imshow('img',img)
cv2.imshow('im',imgray)
cv2.waitKey(0)"""

hsv_min = np.array((15, 100, 100), np.uint8)
hsv_max = np.array((130, 255, 255), np.uint8)

if __name__ == '__main__':
    print(__doc__)

   # путь к файлу с картинкой
    img = cv2.imread('FS.jpg')

    hsv = cv2.cvtColor( img, cv2.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV
    thresh = cv2.inRange( hsv, hsv_min, hsv_max ) # применяем цветовой фильтр
    # ищем контуры и складируем их в переменную contours
    contours, hierarchy = cv2.findContours( thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # отображаем контуры поверх изображения
    cv2.drawContours( img, contours, -1, (255,0,0), 3, cv2.LINE_AA, hierarchy, 1 )
    cv2.imshow('contours', img) # выводим итоговое изображение в окно

    cv2.waitKey()
    cv2.destroyAllWindows()