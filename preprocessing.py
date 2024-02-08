import cv2
import os
import string
minValue = 70

#function which converts RGB image to our desired format
def func(path):    
    frame = cv2.imread(path)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),2)
    th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
    ret, res = cv2.threshold(th3, minValue, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    return res

#This function executed for every directory of the dataset.
#Path of directory
directory = "/Users/ankitprasad/Desktop/Project Hand/data/L"

# iterating over every RGB image of the directory
for file in os.listdir(directory):
    f = os.path.join(directory, file)
    if file.endswith(".jpg"):
        bimg = func(f)
        cv2.imwrite(f,bimg)
