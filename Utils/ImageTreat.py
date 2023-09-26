import cv2


def flip(img):
    return cv2.flip(img, 1)


def to_rgb(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def show(img, winame="Webcam"):
    cv2.imshow(winame, img)

def BlurFaces(result,frame):
    faces = []
    for detection in result.detections:
        bboxC = detection.location_data.relative_bounding_box
        ih, iw, _ = frame.shape
        x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
            int(bboxC.width * iw), int(bboxC.height * ih)
        faces.append(faceImg(frame[y:y + h, x:x + w],(x,y,w,h)))
    for face in faces:
        face.img = cv2.GaussianBlur(face.img, (99, 99), 30)
        x,y,w,h = face.bound
        frame[y:y + h, x:x + w] = face.img
class faceImg():
    def __init__(self,img,bound):
        self.img = img
        self.bound = bound