
import cv2
# from numpy import ny

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')


def detectFace(image):
    img = image
    img_crop = img
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        img_crop = img[y:y + h, x: x + w, :]
    # imgS = cv2.resize(img, (960, 540))
    return img, img_crop, len(faces)


