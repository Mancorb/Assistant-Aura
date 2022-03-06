import cv2
import os
import numpy as np
import Trainer as tr
import takePhoto as tP

location=tP.take_picture("test",None, None,"images")

test_img =cv2.imread("images/test.png") 
faces_detected, grey_img = tr.faceDetection(test_img)
#print(f"faces_detected:{faces_detected}")

if not len(faces_detected):
    print("No image detected")
    exit()

""" for (x,y,w,h) in faces_detected:
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(240,240,255),thickness=1)

resized_img = cv2.resize(test_img,(900,800))
cv2.imshow("face detection res", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows() """
faces,faceID=tr.labels_training('images/0')
face_rec=tr.train_clasifier(faces,faceID)
name={0:"master"}

for faces in faces_detected:
    (x,y,w,h)=faces
    roi_grey=grey_img[y:y+h,x:x+h]
    label,confidence=face_rec.predict(roi_grey)
    print(f"confidence:{confidence}")
    print(f"label:{label}")
    
    predicted_name=name[label]

    """ tr.draw_rect(test_img,faces)
    tr.put_text(test_img,predicted_name,x,y,confidence) """

""" resized_img = cv2.resize(test_img,(800,800))
cv2.imshow("face detection res", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows() """

