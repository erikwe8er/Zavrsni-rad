from cvzone.HandTrackingModule import HandDetector
import cv2
from cvzone.SerialModule import SerialObject
import math

def numToAngle(diff):
    if diff<9:
        return math.floor(diff)
    else:
        return 9
    
 
def HandGesture():
    cap = cv2.VideoCapture(0)
    detector = HandDetector(maxHands=1,detectionCon=0.7)
    serial = SerialObject("/dev/ttyACM0",9600,1)
 
    palac_max,kaziprst_max,srednjak_max,prstenjak_max,mali_max = 0,0,0,0,0
    window_word = "Calibration"
    data = [0,0,0]
    
 
    while True:
        success, img = cap.read()
        hands,img = detector.findHands(img)
        if(window_word == "Calibration"):
            cv2.putText(img,'SPREAD YOUR FINGERS AND PRESS Q TO CALIBRATE',(520, 990),  
                    cv2.FONT_HERSHEY_SIMPLEX, 1,(255, 255, 255),4,cv2.LINE_8)
            
        elif(window_word != "Calibration"):
            cv2.putText(img,'YOU ARE NOW CONTROLLING THE HAND!',(650, 990),  
                    cv2.FONT_HERSHEY_SIMPLEX, 1,(255, 255, 255),4,cv2.LINE_8)
            
        k = cv2.waitKey(1) & 0xFF
        
        if(k == ord('q')):
            if palac_max < int(palac)//10: palac_max = int(palac)//10
            if kaziprst_max < int(kaziprst)//10: kaziprst_max = int(kaziprst)//10
            if srednjak_max < int(srednjak)//10: srednjak_max = int(srednjak)//10
            if prstenjak_max < int(prstenjak)//10: prstenjak_max = int(prstenjak)//10
            if mali_max < int(mali)//10: mali_max = int(mali)//10
            window_word = "Hand Control"
            cv2.destroyWindow("Calibration")
            
        if(k == ord('e')):
            cv2.destroyAllWindows()
            break
            
        
        if hands:
            fingers = detector.fingersUp(hands[0])
            landmarks = hands[0]["lmList"]
            palac, info, img = detector.findDistance(landmarks[4][0:2], landmarks[17][0:2], img, color=(0, 0, 255),scale=10)
            kaziprst, info, img = detector.findDistance(landmarks[5][0:2], landmarks[8][0:2], img, color=(0, 255, 0),scale=10)
            srednjak, info, img = detector.findDistance(landmarks[9][0:2], landmarks[12][0:2], img, color=(255, 0, 0),scale=10)
            prstenjak, info, img = detector.findDistance(landmarks[13][0:2], landmarks[16][0:2], img, color=(0, 255, 255),scale=10)
            mali, info, img = detector.findDistance(landmarks[17][0:2], landmarks[20][0:2], img, color=(255, 255, 0),scale=10)
            data = [numToAngle(palac_max - int(palac)//10),numToAngle(kaziprst_max - int(kaziprst)//10),numToAngle(srednjak_max - int(srednjak)//10),numToAngle(prstenjak_max - int(prstenjak)//10),numToAngle(mali_max - int(mali)//10)]
            serial.sendData(data)
            
 
        cv2.imshow(window_word,img)
        cv2.waitKey(1)
        
HandGesture()
 
