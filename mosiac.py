import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img1 = (Image.open(r"C:\Users\emrer\Downloads\Photomosaic1.JPG")).resize((1024,512))
img2 = (Image.open(r"C:\Users\emrer\Downloads\Photomosaic2.JPG")).resize((512,512))
img3 = (Image.open(r"C:\Users\emrer\Downloads\Photomosaic3.JPG")).resize((1024,512))
img4 = (Image.open(r"C:\Users\emrer\Downloads\Photomosaic4.JPG")).resize((512,512))
img5 = (Image.open(r"C:\Users\emrer\Downloads\Photomosaic5.JPG")).resize((1024,512))

images = [img1, img2, img3, img4, img5] #

def stitch(files):
    
    (width1, height1) = files[0].size #takes jpg image resolution and makes it into width and height for the graph
    (width2, height2) = files[1].size
    (width3, height3) = files[2].size
    (width4, height4) = files[3].size
    
    
    result_width = width1 + width2 + width3 + width4 #creates total graph width
    result_height = height1 + height2 #creates total graph height
    
    result = Image.new('RGB', (result_width,result_height))
    result.paste(im=files[0], box=(512,512))
    result.paste(im=files[1], box=(1536,512))
    result.paste(im=files[2], box=(2048,512))
    result.paste(im=files[3], box=(0,512))
    result.paste(im=files[4], box=(512,0))
    return result

plt.imshow(np.asarray(stitch(images))) #plots images into graph (not visible to humans)
plt.show() #makes a real graph
print("What can I say except your welcome!")
    
    