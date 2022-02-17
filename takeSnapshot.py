import cv2

def take_snap():
     #initializing cv2
     vcObj = cv2.VideoCapture(0)
     result = True
     while( result ):
          #read the frames while the camera is on
          # ret is a dummy variable returns boolean value, if something is being returned or not             
          ret,frame = vcObj.read()
          #cv2.imwrite() method is used to save an image to any storage device
          cv2.imwrite('pragya.jpg' , frame  )
          result = False

     #closes the camera
     vcObj.release()
     #close all windows that might have opned during this process
     cv2.destroyAllWindows()


take_snap()

