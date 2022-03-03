import cv2
import os
from cv2 import cvtColor
import numpy as np
#Cargar la librería para detectar caras
#REGRESA: caras detectadas (posicion) y la imagen en gris
def faceDetection(test_img):
    #delete all color in am image
    grey_img = cvtColor(test_img, cv2.COLOR_BGR2GRAY)
    #Cargar el algoritmo para detectar rostros de cv2
    face_haar_cascade=cv2.CascadeClassifier('haarCascade/haarcascade_frontalface_default.xml')
    #Proceso para detectar rostros con múltiples capas de neuronas a cierta escala
    faces = face_haar_cascade.detectMultiScale(grey_img,scaleFactor=1.32,minNeighbors=10)
    return faces, grey_img
#Entrenar la red neuronal para detectar un rostro
def labels_training(directory):
    #Consjunto de caras
    faces=[]
    #Conjunto de identificadores
    faceID=[]
    #Recorrer todas las carpetas y subcarpetas en una ubicación especifica
    for path ,sudirnames, filenames in os.walk(directory):
        #recorrer los archivos del los folders
        for filename in filenames:
            #recorrer subdirectorios
            if filename.startswith("."):
                print("Skipping system files")
                continue
            id=os.path.basename(path)#clasificar las imagnes de la carpeta con el nombre de la carpeta
            img_path= os.path.join(path,filename)
            #Imprimir la ubicación de la imagen junto con la ubicación
            print("img_path: ",img_path)
            print("id: ",id)
            #Cargar la imagen de la ubicación
            test_img=cv2.imread(img_path)
            #mostrar una alerta si no se pudo cargar la imagen
            if test_img is None:
                print("image not loaded propperly")
                continue
            #guardar la cara detectada y la imagen en gris
            faces_rect,grey_img=faceDetection(test_img)
            #Salir si no encientra ninguna imagen
            if len(faces_rect)!=1:
                continue
            #Obtener posicion x,y de la imagen junto con las dimenciones
            (x,y,w,h)=faces_rect[0]
            #Recortar la imagen gris para solo tener la cara
            roi_grey=grey_img[y:y+w,x:x+h]
            #Agregar la cara a lista de caras
            faces.append(roi_grey)
            #Agregar la identificación (0) a la lista
            faceID.append(int(id))
    return faces,faceID

#Asosiar las imagenes con el ID proporcionado y entrenar a la red neuronal con la librería 
def train_clasifier(faces,faceID):
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(faces,np.array(faceID))
    return face_recognizer
#------------------------------------------------------
#Estetica

#Dibujar un rectangulo en la imagen que se esta analizando
def draw_rect(test_img,face):
    (x,y,w,h)=face
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=5)

#escribir un texto  encima de la imagen con el ID de la persona si es que la identifica
def put_text(test_img,text,x,y):
    cv2.putText(test_img,text,(x,y),cv2.FONT_HERSHEY_DUPLEX,5,(255,0,0),6)
#------------------------------------------------------