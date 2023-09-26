import Utils.Camera as cam
import Utils.ImageTreat as Image
import Utils.FaceDetector as FaceDetector
while True:
    sucess, img = cam.read()
    img = Image.flip(img)
    img_rgb = Image.to_rgb(img)

    results = FaceDetector.process(img_rgb)
    if results:
        Image.BlurFaces(results,img)
    tecla = cam.getKey()
    Image.show(img)
    if tecla == 27:
        break