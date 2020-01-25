import numpy as np
import time as ti
import cv2
from PIL import Image
from PIL import ImageGrab
import matplotlib.pyplot as plt


cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while img_counter < 5:
    
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        
        ti.sleep(4)



cam.release()

cv2.destroyAllWindows()



    
    


img1 = (Image.open(r"C:\Users\emrer\.spyder-py3\opencv_frame_0.png")).resize((1024,512))
img2 = (Image.open(r"C:\Users\emrer\.spyder-py3\opencv_frame_1.png")).resize((1024,512))
img3 = (Image.open(r"C:\Users\emrer\.spyder-py3\opencv_frame_2.png")).resize((1024,512))
img4 = (Image.open(r"C:\Users\emrer\.spyder-py3\opencv_frame_3.png")).resize((1024,512))
img5 = (Image.open(r"C:\Users\emrer\.spyder-py3\opencv_frame_4.png")).resize((1024,512))



images = [img1, img2, img3, img4, img5] #sets images values to array

def stitch(files):
    
    (width1, height1) = files[0].size #takes png image resolution and makes it into width and height for the graph
    (width2, height2) = files[1].size       
    (width3, height3) = files[2].size
    (width4, height4) = files[3].size
    (width5, height5) = files[4].size
    
    
    result_width = width1  #creates total graph width
    result_height = height1 + height2 + height3 + height4 + height5#creates total graph height
    
    result = Image.new('RGB', (result_width,result_height))
    result.paste(im=files[0], box=(0,0))
    result.paste(im=files[1], box=(0,512))
    result.paste(im=files[2], box=(0,1024))
    result.paste(im=files[3], box=(0,1536))
    result.paste(im=files[4], box=(0,2048))
    return result

plt.imshow(np.asarray(stitch(images))) #plots images into graph (not visible to humans)
plt.show() #makes a real graph
print("What can I say except your welcome!")