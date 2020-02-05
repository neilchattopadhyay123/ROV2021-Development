import cv2
import numpy as np

sides = []
ordered_sides = []

sides_contained_colors = []
color_count = 0

sides.append(cv2.imread('side_1.png'))
sides.append(cv2.imread('side_2.png'))
sides.append(cv2.imread('side_3.png'))
sides.append(cv2.imread('side_4.png'))
sides.append(cv2.imread('side_5.png'))

'''
cv2.namedWindow('window', cv2.WINDOW_NORMAL)

for side in sides:
    gray = cv2.cvtColor(side, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY)
    mask = cv2.bitwise_not(mask)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        cv2.drawContours(side, [approx], 0, (0, 0, 0), 5)

    h, w, _ = side.shape
    cv2.resizeWindow('window', (w, h))
    cv2.imshow('window', side)
    
    cv2.waitKey(0)
'''

for side in sides:
    gray = cv2.cvtColor(side, cv2.COLOR_BGR2GRAY)
    _, mono = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY)
    mono = cv2.bitwise_not(mono)

    contours, _ = cv2.findContours(mono, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 3:
        ordered_sides.append(side)
    else:
        ordered_sides.insert(0, side)

    print(len(contours))

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(side, (x, y), (x + w, y + h), (0, 255, 0), 2)
        mean_color = np.array(cv2.mean(side[y:y + h, x:x + w])).astype(np.uint8)

        print('Average color (BGR): ' + str(mean_color))
    
    cv2.imshow('window', side)
    cv2.waitKey(0)

cv2.destroyAllWindows()
