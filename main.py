import os
import cv2 as cv
import numpy 
from dir import * 

def windows_init():
    cv.namedWindow("threshold_image", cv.WINDOW_NORMAL)
    cv.namedWindow("raw_image", cv.WINDOW_NORMAL)

def threshold_image(image):
    img = cv.imread("{}{}".format(RAW_IMG_DIR, image))
    img = cv.GaussianBlur(img, (9, 9), 0)
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, threshold_image = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)

    contours, hierarchy = cv.findContours(threshold_image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    max_h = 10
    max_w = 10

    for contour in contours:
        x, y, w, h = cv.boundingRect(contour)
        # cv.rectangle(threshold_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # cv.drawContours(img, [contour], 0, (0, 0, 255), 3)
        if ((w > max_w) and (h > max_h)):
            max_h = h
            max_w = w
            max_x = x
            max_y = y
        
    cv.rectangle(img, (max_x, max_y), (max_x + max_w, max_y + max_h), (0, 255, 0), 5)
    crop_thesh_img = threshold_image[max_y:max_y + max_h, max_x:max_x + max_w]

    crop_thesh_img = cv.resize(crop_thesh_img, None, fx=0.2, fy=0.2)
    cv.imwrite("{}{}".format(THRSH_IMG_DIR, image), threshold_image)
    cv.imwrite("{}{}".format(RAW_WITH_REC_DIR, image), img)
    cv.imwrite("{}{}".format(CROP_DIR, image), crop_thesh_img)
#     cv.imshow("threshold_image", threshold_image)
#     cv.imshow("raw_image", img)

def tesseract_cmd(image, lang):
    os.system("tesseract {}{} {}{} -l {} -c preserve_interword_spaces=1".format(CROP_DIR, image, OUTPUT_DIR, image, lang)) 

def main():
    windows_init()
    
    for i in range(1, 44):
        threshold_image("{}.jpg".format(i))
        tesseract_cmd("{}.jpg".format(i), "tha")

if __name__ == '__main__':
    main()
    cv.waitKey(0)