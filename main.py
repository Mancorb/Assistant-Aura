import F_FaceRec as face_rec
import hashlib
import os


def AdminCheck():
    recognition=face_rec.Authentication()
    if recognition:
        if recognition[0]=="master" and recognition[1]>55:
            print("Administrator recognized")
            password = input("Enter your password:")
            return encriptAndCheck(password.encode())
        else:
            return False
    else: return False

def encriptAndCheck(password):
    hash_object = hashlib.sha1(password)
    hex_dig = hash_object.hexdigest()

    with open('AuraLogo.jpg', 'rb') as f:
        content = f.read()
        offset=content.index(bytes.fromhex('FFD9'))
        f.seek(offset+2)
        f = f.read().decode()

    if f == hex_dig: return True
    else: return False

def checkID():
    scan = input("Would you like to access as Administrator? (y/n): ")
    if scan == "y":
        try:
            if AdminCheck():
                print("Administrator accepted")
                return True
                os.remove("images/test.png")

            else:
                return False 
                print("Administrator rejected")
        except:
            os.system("cls")
            print("Ups looks like there was a problem\nCheck you hardware and try again later...")


def bootUp():
    AdminAccess = False
    

    #For testing purposes ONLY
    # elif scan == "Overide":
    #     temp = input("Enter your password:")
    #     if encriptAndCheck(temp.encode()): AdminAccess = True
    

if __name__ == '__main__':
    bootUp()