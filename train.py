import os
import numpy as np
from cv2 import cv2
from detect import detectFace
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
from tkinter import messagebox

def train(cap, id, thread, video, stop, _callback):
    images = []
    ids = []
    i = 0
    while i < 100 and stop is False:
        ret, frame = cap.read()
        if frame is None: continue
        frame, face, faces = detectFace(frame)
        video.setPixmap(convert_nparray_to_QPixmap(frame))
        time.sleep(0.1)
        if (face is not None) and (faces == 1):
            face = Image.fromarray(face).convert('L')
            images.append(np.array(face))
            ids.append(id)
            i += 1
            print("add to faces ", int(i))
        thread.upProgress(i)
    if stop is True:
        cap.release()
        messagebox.showwarning("Thông báo", "Sinh viên chưa được thêm vào")
        return
    ids = np.array(ids)
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    if not os.path.exists('trainer'):
        os.makedirs('trainer')
    if not os.path.exists('trainer/trainningData.yaml'):
        recognizer.train(images, ids)
        recognizer.write('trainer/trainningData.yaml')
        return
    recognizer.read('trainer/trainningData.yaml')
    recognizer.update(images, ids)
    recognizer.write('trainer/trainningData.yaml')
    print("Train oke")
    cap.release()
    _callback()
    messagebox.showinfo("Thông báo", "Thêm thành công sinh viên")
    # cv2.destroyAllWindows()

def convert_nparray_to_QPixmap(img):
    # print(img)
    w, h, ch = img.shape
    # Convert resulting image to pixmap
    if img.ndim == 1:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    qimg = QtGui.QImage(img.data, h, w, 3 * h, QtGui.QImage.Format_RGB888)
    qpixmap = QtGui.QPixmap(qimg)
    return qpixmap