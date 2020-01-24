import cv2
import numpy as np

FONT = cv2.FONT_HERSHEY_COMPLEX

def get_color_of_contour (cnt, img):
    ''' Get the average color of the area inside of a contour '''
    
    # Get the bounding rect of the contour
    x, y, w, h = cv2.boundingRect(cnt)

    # Crop out the contour in the image
    cropped_img = img[y:y + h, x:x + w]

    # Return the average color of the contour
    return np.array(cv2.mean(cropped_img))

def subtract_colors (color_1, color_2):
    ''' Subtract two colors '''

    color = [0] * 4

    for i in range(0, 3):
        color[i] = int(color_1[i] - color_2[i])

    return color

def count_negatives (arr, inc_0=True):
    ''' Count how many negative numbers (including 0) are in an array '''

    # The number of negative numbers
    count = 0
    
    for i in arr:
        if i < 0 or (inc_0 and i <= 0):
            count += 1

    return count

def main ( ):
    # Load images
    prev_img = cv2.imread('./previous_image.png')
    curr_img = cv2.imread('./current_image.png')

    # Find the differences in the images
    diff_1 = cv2.cvtColor(cv2.subtract(curr_img, prev_img), cv2.COLOR_BGR2GRAY)
    diff_2 = cv2.cvtColor(cv2.subtract(prev_img, curr_img), cv2.COLOR_BGR2GRAY)
    _, diff_1_mask = cv2.threshold(diff_1, 0, 255, cv2.THRESH_BINARY)
    _, diff_2_mask = cv2.threshold(diff_2, 0, 255, cv2.THRESH_BINARY)

    # Combine the differences into 1 image
    diff = cv2.add(diff_1_mask, diff_2_mask)

    '''
    *** NOTE ***

            For final product, there is going to need to be logic to delete the small differences that may occur
    '''

    # Get the contours around the differences in the images
    _, contours, _ = cv2.findContours(diff, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt_img = curr_img.copy( )

    # Loop through all contours in the image
    for cnt in contours:
        # Approximate the contour
        approx = cv2.approxPolyDP(cnt, 0.03 * cv2.arcLength(cnt, True), True)

        # Get the center of the contour
        moments = cv2.moments(approx)
        center_x = int(moments['m10']/moments['m00'])
        center_y = int(moments['m01']/moments['m00'])

        # Coral label and color based on change
        cnt_label = ''
        cnt_color = (0, 0, 0)

        # Get the colors of the changed areas in both the previous image and the current image
        prev_color = get_color_of_contour(approx, prev_img.copy( ))
        curr_color = get_color_of_contour(approx, curr_img.copy( ))

        # Find the difference in colors
        color_diff = subtract_colors(prev_color, curr_color)

        print(color_diff)

        # Determine what happened to the coral
        if count_negatives(color_diff) == len(color_diff):
            cnt_label = 'Death'
            cnt_color = (0, 0, 255)
        elif count_negatives(color_diff, False) == 0:
            cnt_label = 'Growth'
            cnt_color = (0, 255, 0)
        else:
            if count_negatives(color_diff) == 2:
                cnt_label = 'Decay'
                cnt_color = (255, 255, 0)
            elif count_negatives(color_diff) == 3:
                cnt_label = 'Restoration'
                cnt_color = (0, 255, 255)

        # Draw bounding contours and labels
        cv2.drawContours(cnt_img, [approx], 0, cnt_color, 5)
        cv2.putText(cnt_img, cnt_label, (center_x, center_y), FONT, 1, cnt_color)

    # Apply mask to the current image to determine color of the differences
    # res = cv2.bitwise_and(curr_img, curr_img, mask=diff)

    # Display the image
    cv2.imshow('cnt_img', cnt_img)
    cv2.waitKey(0)

if __name__ == '__main__':
    main( )
