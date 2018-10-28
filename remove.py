import os
from dir import * 

def system_init():
    os.system("rm -r {}*".format(OUTPUT_DIR)) 
    os.system("rm -r {}*".format(THRSH_IMG_DIR)) 
    os.system("rm -r {}*".format(RAW_WITH_REC_DIR)) 
    os.system("rm -r {}*".format(THRSH_CROP_DIR)) 

system_init()