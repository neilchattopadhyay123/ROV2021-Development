import cv2
import numpy as np

# stores points for perspective transform
refPt = []

# Read image.
img = cv2.imread('/home/neil/Downloads/musselbed.jpg', cv2.IMREAD_COLOR)

# stores the original images to remove the circles that are drawn
original_img = img.copy()


# finds distance between two points
def dist(x, y):
    return np.sqrt(np.sum((x - y) ** 2))


def four_point_transform(input_image, pts):
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
    warped = cv2.warpPerspective(input_image, matrix, (maxWidth, maxHeight))

    # return the warped image
    return warped


# stores the xy coordinate and plots the reference point for imag for perspective transform
def find_point(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 5, (255, 0, 0, 255), -1)
        refPt.append([x, y])


# creates a window to show the image and select the points
cv2.startWindowThread()
cv2.namedWindow('select')
cv2.setMouseCallback('select', find_point)

# shows image and plot points for perspective transform
while True:
    cv2.imshow('select', img)

    # allows for user to do the next perspective transform by pressing ESC
    if cv2.waitKey(20) & 0xFF == 27:
        break

# stores the perspective transform's result
result = four_point_transform(original_img, np.array(refPt, dtype='float32'))

bilateral_filtered_image = cv2.bilateralFilter(result, 5, 175, 175)
while True:
    cv2.imshow('Bilateral', bilateral_filtered_image)
    if cv2.waitKey(20) & 0xFF == 27:
        break

edge_detected_image = cv2.Canny(bilateral_filtered_image, 75, 200)
while True:
    cv2.imshow('Edge', edge_detected_image)
    if cv2.waitKey(20) & 0xFF == 27:
        break

contours, hierarchy = cv2.findContours(edge_detected_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contour_list = []
for contour in contours:
    if len(contour) > 10:
        contour_list.append(contour)

cv2.drawContours(result, contour_list, -1, (255, 0, 0), 2)
while True:
    cv2.imshow('Objects Detected', result)
    if cv2.waitKey(20) & 0xFF == 27:
        break

num_arcs = 1

for i in range(1, len(contour_list)):
    if dist(np.float32(contour_list[i][0][0]), np.float32(contour_list[i - 1][0][0])) > 12 and dist(
            np.float32(contour_list[i][1][0]), np.float32(contour_list[i - 1][1][0])) > 12:
        num_arcs += 1

font = cv2.FONT_HERSHEY_SIMPLEX

# org
org = (50, 50)

# fontScale
fontScale = 1

# Blue color in BGR
color = (0, 255, 0)

# Line thickness of 2 px
thickness = 2

# Using cv2.putText() method
image = cv2.putText(result, str(num_arcs), org, font,
                    fontScale, color, thickness, cv2.LINE_AA)

#
while True:
    cv2.imshow('print count', image)
    if cv2.waitKey(20) & 0xFF == 27:
        break


print(num_arcs)
