import os

src_path = "img/process_by_gimp/"
des_path = "img/process_by_gimp/output/"

def main():   
    for i in range(1, 56):
        os.system("tesseract {}{}.jpg {}{} -l tha -c preserve_interword_spaces=1".format(src_path, i, des_path, i))

if __name__ == '__main__':
    main()