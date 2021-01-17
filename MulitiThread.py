import cv2
from threading import Thread
from detect import detectFace
from train import train
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from attendance import run
import os

class TrainThead(Thread):

    def __init__(self, user, video, stop, updateProgress, _callback):
        super(TrainThead, self).__init__()
        self.user = user
        self.updatdeProgress = updateProgress
        self.video = video
        self.stop = stop
        self._callback = _callback

    def run(self):
        cap = cv2.VideoCapture(0);
        train(cap, self.user.id, self, self.video, self.stop, _callback=self._callback)
        # cap.release()

    def upProgress(self, progress):
        self.updatdeProgress(progress)

class AtenndanceThread(Thread):
    def __init__(self, name, delay, pixmap, video, list, _callback):
        super(AtenndanceThread, self).__init__()
        self.name = name
        self.delay = delay
        self.cam = False
        self.pixmap = pixmap
        self.video = video
        self.list = list
        path = "trainer/trainningData.yaml"
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        if (os.path.exists(path)):
            self.recognizer.read(path)
        self.face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')
        self._callback = _callback

    def run(self):
        cap = cv2.VideoCapture(0)
        self.cam = True
        i = 1
        print(self.cam)
        while self.cam:
            ret, frame = cap.read()
            frame_video = run(frame, self.list, recognizer=self.recognizer, face_cascade=self.face_cascade, callback=self._callback)
            self.video.setPixmap(convert_nparray_to_QPixmap(frame_video))
            time.sleep(0.1)
        cap.release()

class myThread(Thread):
    def __init__(self, name, delay, pixmap, video, list):
        super(myThread, self).__init__()
        self.name = name
        self.delay = delay
        self.cam = False
        self.pixmap = pixmap
        self.video = video
        self.list = list

    def run(self):
        cap = cv2.VideoCapture(0)
        self.cam = True
        i = 1
        print(self.cam)
        while self.cam:
            ret, frame = cap.read()
            frame_video = run(frame, self.list)
            self.video.setPixmap(convert_nparray_to_QPixmap(frame_video))
            time.sleep(0.1)
        cap.release()
def convert_nparray_to_QPixmap(img):
    w, h, ch = img.shape
    # Convert resulting image to pixmap
    if img.ndim == 1:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    qimg = QtGui.QImage(img.data, h, w, 3 * h, QtGui.QImage.Format_RGB888)
    qpixmap = QtGui.QPixmap(qimg)
    return qpixmap