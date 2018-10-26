import os
import cv2 as cv

RAW_IMG_DIR = "img/raw/"
THRSH_IMG_DIR = "img/threshold/"
OUTPUT_DIR =  "img/output/"

def windows_init():
    cv.namedWindow("threshold_image", cv.WINDOW_NORMAL)
    cv.namedWindow("raw_image", cv.WINDOW_NORMAL)

def threshold_image(image):
    img = cv.imread("{}{}".format(RAW_IMG_DIR, image))
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, threshold_image = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)

    contours, hierarchy = cv.findContours(threshold_image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x, y, w, h = cv.boundingRect(contour)
        # cv.rectangle(threshold_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv.imwrite("{}{}".format(THRSH_IMG_DIR, image), threshold_image)
    cv.imshow("threshold_image", threshold_image)
    cv.imshow("raw_image", img)

def tesseract_cmd(image, lang):
    os.system("tesseract {}{} {}{} -l {} -c preserve_interword_spaces=1".format(THRSH_IMG_DIR, image, OUTPUT_DIR, image, lang)) 

def main():
    windows_init()
    threshold_image("020.jpg")
    tesseract_cmd("020.jpg", "tha")

if __name__ == '__main__':
    main()
    cv.waitKey(0)