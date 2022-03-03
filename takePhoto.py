
# import the opencv library
import cv2
import os
  
def take_picture(name,first,last,loc):
    # define a video capture object
    vid = cv2.VideoCapture(0)
    state=False

    if first == None:
        first=1
    if last != None:
        last=1
        for i in range(int(first),int(last)):
            if vid.isOpened():
                ret, frame = vid.read()
                if ret:
                    img_name = f"{loc}/{name}{i}.png"
                    cv2.imwrite(img_name, frame)
                    os.system("cls")
                    print(f"image, {i} captured")
                    state=True
    else: 
        if vid.isOpened():
            ret, frame = vid.read()
            if ret:
                img_name = f"{loc}/{name}.png"
                cv2.imwrite(img_name, frame)
                os.system("cls")
                print(f"image, {i} captured")
                state=True

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    if state:
        return img_name
    else: return None

