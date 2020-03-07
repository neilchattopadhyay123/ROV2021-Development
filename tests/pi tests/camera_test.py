import numpy as np
import cv2

camera = cv2.VideoCapture(0)

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
##camera.set(cv2.CAP_PROP_FPS, 60)

print(camera.get(cv2.CAP_PROP_MODE))

while(True):
    # Capture frame-by-frame
    ret, frame = camera.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
camera.release()
cv2.destroyAllWindows()
