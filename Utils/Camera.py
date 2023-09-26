import cv2

resolucao_x = 1280
resolucao_y = 720
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH,resolucao_x)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT,resolucao_y)

def read():
    return camera.read()
def getKey():
    return cv2.waitKey(1)