from cvzone.HandTrackingModule import HandDetector
import cv2
from cvzone.SerialModule import SerialObject
import math


#Prebacuje dobivenu vrijednost u broj izmedju 0 i 9 pomocu kojega kontroliramo servo
def numToAngle(diff):
    if diff<0:
        return 0
    if diff<9:
        return math.floor(diff)
    else:
        return 9
    
 
def HandGesture():
    #Postavljamo kameru i detektor te početne vrijednosti variabli, uključujući i serijsku komunikaciju
    cap = cv2.VideoCapture(0)
    detector = HandDetector(maxHands=1,detectionCon=0.7)
    serial = SerialObject("/dev/ttyACM0",9600,1)
    palac_max,kaziprst_max,srednjak_max,prstenjak_max,mali_max,scale_max = 0,0,0,0,0,0
    
    window_word = "Calibration"    
    
    #Glavna petlja u kojoj se vrši detekcija ruke i prstiju i prenošenje podataka na Arduino
    while True:
        success, img = cap.read()
        hands,img = detector.findHands(img)
        #Postavljanje prozora ovisno o tome u kojem smo modu (kalibracija ili kontrola ruke)
        if(window_word == "Calibration"):
            cv2.putText(img,'SPREAD YOUR FINGERS AND PRESS Q TO CALIBRATE',(520, 990),  
                    cv2.FONT_HERSHEY_SIMPLEX, 1,(255, 255, 255),4,cv2.LINE_8)
            
        elif(window_word != "Calibration"):
            cv2.putText(img,'YOU ARE NOW CONTROLLING THE HAND!',(650, 990),  
                    cv2.FONT_HERSHEY_SIMPLEX, 1,(255, 255, 255),4,cv2.LINE_8)
            
        k = cv2.waitKey(1) & 0xFF
        
        #Kalibracija - pritiskom na tipku 'q' spremamo maksimalne vrijednosti udaljenosti prstiju
        if(k == ord('q')):
            if palac_max < int(palac)//10: palac_max = int(palac)//10
            if kaziprst_max < int(kaziprst)//10: kaziprst_max = int(kaziprst)//10
            if srednjak_max < int(srednjak)//10: srednjak_max = int(srednjak)//10
            if prstenjak_max < int(prstenjak)//10: prstenjak_max = int(prstenjak)//10
            if mali_max < int(mali)//10: mali_max = int(mali)//10
            scale_max = scale
            window_word = "Hand Control"
            cv2.destroyWindow("Calibration")
        
        #Izlaz iz programa pritiskom na tipku 'e'
        if(k == ord('e')):
            cv2.destroyAllWindows()
            break
            
        #Ako je ruka detektirana, računamo udaljenosti prstiju i skaliramo ih u odnosu na početne vrijednosti
        #Nakon toga šaljemo podatke Arduinu
        if hands:
            fingers = detector.fingersUp(hands[0])
            landmarks = hands[0]["lmList"]
            palac, info, img = detector.findDistance(landmarks[4][0:2], landmarks[17][0:2], img, color=(0, 0, 255),scale=6)
            kaziprst, info, img = detector.findDistance(landmarks[5][0:2], landmarks[8][0:2], img, color=(0, 255, 0),scale=10)
            srednjak, info, img = detector.findDistance(landmarks[9][0:2], landmarks[12][0:2], img, color=(255, 0, 0),scale=10)
            prstenjak, info, img = detector.findDistance(landmarks[13][0:2], landmarks[16][0:2], img, color=(0, 255, 255),scale=10)
            mali, info, img = detector.findDistance(landmarks[17][0:2], landmarks[20][0:2], img, color=(255, 255, 0),scale=10)
            scale,info,img = detector.findDistance(landmarks[1][0:2], landmarks[2][0:2], img, color=(255, 255, 255),scale=1)
            data = [numToAngle(palac_max - int(palac*(scale_max/scale))//10),numToAngle(kaziprst_max - int(kaziprst*(scale_max/scale))//10),numToAngle(srednjak_max - int(srednjak*(scale_max/scale))//10),numToAngle(prstenjak_max - int(prstenjak*(scale_max/scale))//10),numToAngle(mali_max - int(mali*(scale_max/scale))//10)]
            print(data)
            serial.sendData(data)

        #Prikaz slike
        cv2.imshow(window_word,img)
        cv2.waitKey(1)
        
HandGesture()
 
