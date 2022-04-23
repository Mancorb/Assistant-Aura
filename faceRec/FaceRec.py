import cv2
import os
import faceRec.Trainer as tr
from tkinter import filedialog

def picture(loc, name):
    # define a video capture object
    capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    #capture.open()
    if capture.isOpened() :
        while(True):

            ret, frame = capture.read()
            # Display the resulting frame
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.imwrite('images/test.png',frame)
                break
        capture.release()
        cv2.destroyAllWindows()

    else: 
        print("camera not opened")
        capture.release(0)
        cv2.destroyAllWindows()


def takePicture():
    try:
        picture("images","test")
        cv2.imread(f"images/test.png") 
        return "images/test.png"
        
    except Exception as e:
        print(f"\n----\nError:\n{e}\n---")
        return False

def useFile():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",
                                              filetypes = (("png files","*.png*"),("jpg files","*.jpg*")))
    return filename

def Authentication ():
    #ID dictionaries
    res ={"name":"Unknown","confidence":0}
    name={0:"master"}
    
    #Ask if the user wants to use an existing image
    if str(input("Do you want to use a picture? y/n: ")).lower()=="y":
        data = useFile()#If so then tkinter will return the route of the image
    else: data = takePicture() #Otherwise the programm wil take a picture and save it
    if data == False:#If no image location is returned then the method is terminated
        return False
    try:
        data = cv2.imread(data)#Read the image with cv2 in an object
        faces_detected, grey_img=data = tr.faceDetection(data)#Use HaarCascade to detect faces it return the image in grey and location of the face
    except:
        print("Error: no face detected")
        return False
        
    print("Success... analizing")#Inditate that it did find a face and will compare it with the references
    faces,faceID=tr.labels_training('images/0')#uses this file as reference
    face_rec=tr.train_clasifier(faces,faceID)#Match ID with references
    
    #predict the ID of the image and returns an ID with % of confidence
    label= None
    for faces in faces_detected:
        (x,y,w,h)=faces
        roi_grey=grey_img[y:y+h,x:x+w]
        label,confidence=face_rec.predict(roi_grey)
        print(f"confidence:{confidence}")
        print(f"label:{label}")

        predicted_name=name[label]
        #print(predicted_name)
    
    if label == 0:#If the ID found is the same as in the dictionary it will return it
        res["name"]=predicted_name
        res["confidence"]=confidence
        os.system("cls")
    return res


print(Authentication())