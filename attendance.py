import os
import cv2
import argparse
from user import User

def run(frame, list, recognizer, face_cascade, callback):
    font = cv2.FONT_HERSHEY_COMPLEX
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)
    # -- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        nbr_predicted, conf = recognizer.predict(frame_gray[y:y + h, x:x + w])
        print(nbr_predicted)
        if conf < 70:
            profile = nbr_predicted
            callback(profile)
            cv2.putText(frame, list.get(profile, User(0, "Nothing")).fullname, (x + 10, y), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
        else:
            cv2.putText(frame, "Unknow", (x + 10, y), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
    return frame

# cap = cv2.VideoCapture(0)
# while (True):
#     ret, frame = cap.read()
#     run(frame, {})
#     if cv2.waitKey(10) == 27:
#         break
