from threading import Thread
import cv2

class VideoStream:
    def __init__(self, src=-1):
        self.camera = cv2.VideoCapture(src)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.camera.set(cv2.CAP_PROP_FPS, 30)
        
        self.thread = Thread(target=self.update, args=())
        _, self.frame = self.camera.read()
        
        self.stopped = False

    def start(self):
        self.thread.start()
        
        return self

    def update(self):
        while True:
            if self.stopped:
                return

            _, self.frame = self.camera.read()
            
    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True

        self.thread.join()
        self.camera.release()

stream = VideoStream().start()

while True:
    frame = stream.read()

    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
stream.stop()
