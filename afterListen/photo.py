import cv2

def photo_take():
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    if ret:
        cv2.imwrite("photo.jpg", frame)
    camera.release()
    return "photo.jpg"
