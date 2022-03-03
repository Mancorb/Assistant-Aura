import cv2
import os
import numpy as np
import Trainer as fr
import takePhoto as tP

location=tP.take_picture("subject",None, None,)

test_img =cv2.imread('images/c1.png') 
faces_detected, grey_img = fr.faceDetection(test_img)
print(f"faces_detected:{faces_detected}")

""" for (x,y,w,h) in faces_detected:
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=5)

resized_img = cv2.resize(test_img,(1000,700))
cv2.imshow("face detection res", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows() """

faces,faceID=fr.labels_training('images/0')
face_rec=fr.train_clasifier(faces,faceID)
name={0:"master"}

for faces in faces_detected:
    (x,y,w,h)=faces
    roi_grey=grey_img[y:y+h,x:x+h]
    label,confidence=face_rec.predict(roi_grey)
    print(f"confidence:{confidence}")
    print(f"label:{label}")
    fr.draw_rect(test_img,faces)
    predicted_name=name[label]
    fr.put_text(test_img,predicted_name,x,y)

resized_img = cv2.resize(test_img,(1000,700))
cv2.imshow("face detection res", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

