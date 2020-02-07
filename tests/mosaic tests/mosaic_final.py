# import statements
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# list of points used to do perspective transform
refPt = []

# resulting images
results = []

# finds out if the long side is
while True:
    yes_no = input("is long side on the left(y for yes, n for no): ")

    if yes_no == 'y' or yes_no == 'yes':
        yes_no = False
        break
    elif yes_no == 'n' or yes_no == 'no':
        yes_no = True
        break

# stores whether or not the long side is on the left
reverse = yes_no

# mirrors image if long side is on the right so that long side is on the left
if reverse:
    original_image1 = cv2.flip(cv2.resize(cv2.imread("/home/neil/MATE2020/Images/photomosaic2_imageflipped.jpg"), (756, 900)), 1)
    image1 = original_image1.copy()

    original_image2 = cv2.flip(cv2.resize(cv2.imread("/home/neil/MATE2020/Images/photomosaic1_imageflipped.jpg"), (756, 900)), 1)
    image2 = original_image2.copy()
else:
    original_image1 = cv2.resize(cv2.imread("/home/neil/Downloads/photomosaic2.jpg"), (756, 900))
    image1 = original_image1.copy()

    original_image2 = cv2.resize(cv2.imread("/home/neil/Downloads/photomosaic1.jpg"), (756, 900))
    image2 = original_image2.copy()


# does perspective transform on image
def four_point_transform(image, pts):
    # obtain a consistent order of the points and unpack them
    # individually
    (tl, tr, br, bl) = pts

    # compute the width of the new image, which will be the
    # maximum distance between bottom-right and bottom-left
    # x-coordiates or the top-right and top-left x-coordinates
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    # compute the height of the new image, which will be the
    # maximum distance between the top-right and bottom-right
    # y-coordinates or the top-left and bottom-left y-coordinates
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    # now that we have the dimensions of the new image, construct
    # the set of destination points to obtain a "birds eye view",
    # (i.e. top-down view) of the image, again specifying points
    # in the top-left, top-right, bottom-right, and bottom-left
    # order
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    # compute the perspective transform matrix and then apply it
    matrix = cv2.getPerspectiveTransform(pts, dst)
    warped = cv2.warpPerspective(image, matrix, (maxWidth, maxHeight))

    # return the warped image
    return warped


# stores the xy coordinate and plots the reference point for image1 for perspective transform
def find_point_image1(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(image1, (x, y), 5, (255, 0, 0), -1)
        refPt.append([x, y])


# stores the xy coordinate and plots the reference point for image1 for perspective transform
def find_point_image2(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(image2, (x, y), 5, (255, 0, 0), -1)
        refPt.append([x, y])

# stitches the new images to create the photomosaic
def stitch(files):
    (width1, height1) = files[0].size  # takes jpg image resolution and makes it into width and height for the graph
    (width2, height2) = files[1].size
    (width3, height3) = files[2].size
    (width4, height4) = files[3].size

    result_width = width1 + width2 + width3 + width4  # creates total graph width
    result_height = height1 + height2  # creates total graph height

    # pastes together the images
    output = Image.new('RGB', (result_width, result_height))
    output.paste(im=files[0], box=(0, 512))
    output.paste(im=files[1], box=(1024, 512))
    output.paste(im=files[2], box=(0, 0))
    output.paste(im=files[3], box=(1536, 512))
    output.paste(im=files[4], box=(2560, 512))

    return output

# creates a window for image1
cv2.startWindowThread()
cv2.namedWindow('image1')
cv2.setMouseCallback('image1', find_point_image1)

# plots and shows reference points and image1 for perspective transform
for i in range(0, 3):
    while True:
        cv2.imshow('image1', image1)

        # allows for user to do the next perspective transform by pressing ESC
        if cv2.waitKey(20) & 0xFF == 27:
            break

    # adds image from perspective transform to results
    results.append(four_point_transform(image1, np.float32(refPt)))

    # emptys reference points for the next perspective transform
    refPt = []

    # clears image
    image1 = original_image1

    # destroys the window when three images have been made for the photomosaic
    if i == 3:
        cv2.destroyAllWindows()

# creates a window for image1
cv2.startWindowThread()
cv2.namedWindow('image2')
cv2.setMouseCallback('image2', find_point_image2)

# plots and shows reference points and image1 for perspective transform
for i in range(0, 2):
    while True:
        cv2.imshow('image2', image2)

        # allows for user to do the next perspective transform by pressing ESC
        if cv2.waitKey(20) & 0xFF == 27:
            break

    # adds image from perspective transform to results
    results.append(four_point_transform(image2, np.float32(refPt)))

    # emptys reference points for the next perspective transform
    refPt.clear()

    # clears image
    image2 = original_image2

    # destroys the window when two images have been made for the photomosaic
    if i == 2:
        cv2.destroyAllWindows()

# stores results as PIL image objects
pil_images = []

# converts results which are opencv images to PIL image objects
for i in range(len(results)):
    img = cv2.cvtColor(results[i], cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    pil_images.append(img)

# resizes the images properly
pil_images[0] = pil_images[0].resize((1024, 512))
pil_images[1] = pil_images[1].resize((512, 512))
pil_images[2] = pil_images[2].resize((1024, 512))
pil_images[3] = pil_images[3].resize((1024, 512))
pil_images[4] = pil_images[4].resize((512, 512))

# stitchs the PIL images to get the final photomosaic and shows it using matplotlib
result = stitch(pil_images)
plt.imshow(result)
plt.show()
