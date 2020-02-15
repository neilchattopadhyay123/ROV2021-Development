import cv2
import numpy as np

# stores points for perspective transform
refPt = []

# Read image.
img = cv2.imread('/home/neil/Pictures/small_circles.jpg', cv2.IMREAD_GRAY)
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

# stores the original images to remove the circles that are drawn
original_img = img.copy()

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

# Convert to grayscale.
gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

# Blur using 3 * 3 kernel.
gray_blurred = cv2.blur(gray, (3, 3))

# Apply Hough transform on the blurred image.
detected_circles = cv2.HoughCircles(gray_blurred,
                                    cv2.HOUGH_GRADIENT, 1, 20, param1=250,
                                    param2=17, minRadius=1, maxRadius=40)

# Draw circles that are detected.
if detected_circles is not None:

    # Convert the circle parameters a, b and r to integers.
    # a is x coordinate of center b is y coordinate of center and r is radius
    detected_circles = np.uint16(np.around(detected_circles))

    # prints the number of circles found
    print('Found ' + str(detected_circles.shape[1]) + ' circles.')

    # iterates though the circle parameters
    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]

        # Draw the circumference of the circle.
        cv2.circle(result, (a, b), r, (0, 255, 0), 2)

        # Draw a small circle (of radius 1) to show the center.
        cv2.circle(result, (a, b), 1, (0, 0, 255), 3)

while True:
    cv2.imshow('output', result)

    # allows for user to stop showing the image by pressing ESC
    if cv2.waitKey(20) & 0xFF == 27:
        break
