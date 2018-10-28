import os
import cv2 as cv
import numpy 
from dir import * 

def pre_tesseract_process(src_path, image):
    img = cv.imread("{}{}".format(src_path, image))
    img = cv.GaussianBlur(img, (9, 9), 0)
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, threshold_image = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)

    contours, hierarchy = cv.findContours(threshold_image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    max_h = 1
    max_w = 1
    for contour in contours:
        x, y, w, h = cv.boundingRect(contour)
        if ((w > max_w) and (h > max_h)):
            max_h = h
            max_w = w
            max_x = x
            max_y = y
        
    crop_size = {
        "x": max_x + 200,
        "y": max_y + 100,
        "height": (max_y + max_h) - 100,
        "wide": (max_x + max_w) - 200
    }

    cv.rectangle(img, (crop_size["x"], crop_size["y"]), (crop_size["wide"], crop_size["height"]), (0, 255, 0), 10)
    crop_thesh_img = threshold_image[crop_size["y"]:crop_size["height"], crop_size["x"]:crop_size["wide"]]

    crop_thesh_img = cv.resize(crop_thesh_img, None, fx=0.3, fy=0.3)
    cv.imwrite("{}{}".format(THRSH_IMG_DIR, image), threshold_image)
    cv.imwrite("{}{}".format(RAW_WITH_REC_DIR, image), img)
    cv.imwrite("{}{}".format(THRSH_CROP_DIR, image), crop_thesh_img)

def tesseract_cmd(src_path, image, des_path, lang):
    os.system("tesseract {}{} {}{} -l {} -c preserve_interword_spaces=1".format(src_path, image, des_path, image, lang)) 

def main():   
    for i in range(1, 56):
        pre_tesseract_process(RAW_IMG_DIR, "{}.jpg".format(i))
        tesseract_cmd(THRSH_CROP_DIR, "{}.jpg".format(i), OUTPUT_DIR, "tha")

if __name__ == '__main__':
    main()
    cv.waitKey(0)