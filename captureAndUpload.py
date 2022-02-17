import dropbox
import cv2
import time
import random

start_time = time.time()

def takeSnap():
    number = random.randint(0,100)
    vcObj = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = vcObj.read()
        imgName = 'img'+str(number)+'.png'
        cv2.imwrite(imgName, frame)
        start_time = time.time()
        result = False
    return(imgName)
    print('Your picture is successfully taken... :)')
    vcObj.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = 'sl.BCPFKPjmPBME4_lyjT5d099-zPwaeQik_-kujaPv1YFzb4YfljqCzlK0b4CFxnzGbPTYTbKFR7fLt7bUBT3dJ-5X20yrpgs1guCMfJLanfpalYblHEdv_-auOEXep-Mf5_R6h4iqcXE'
    file = img_name
    file_from = file
    file_to = '/Pictures/'+(img_name)
    dbx = dropbox.Dropbox(access_token)
    
    with open(file_from, 'rb') as f:
     # to resolve the path errors last parameter is added
        dbx.files_upload(f.read(),file_to, mode=dropbox.files.WriteMode.overwrite)
        print('Your file is uploaded... :)')

def main():
    while(True):
        if( (time.time()-start_time) >= 5 ):
            name = takeSnap()
            upload_file(name)
main()

    