import cv2
from cvzone.HandTrackingModule import HandDetector
import math

cv2.namedWindow("image", cv2.WINDOW_NORMAL)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)
color=(255,0,0)
cx,cy,w,h=100,100,150,150
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    
    
    # Find hands
    hands, _ = detector.findHands(img)
    if hands:
        
        
        # Get landmarks of the first detected hand (assuming only one hand)
        hand_landmarks = hands[0]["lmList"]
        
        # Get the position of the tip of the index finger (landmark 8)
        index_finger_tip = hand_landmarks[8]
        middel_finger=hand_landmarks[12]
        index_finger_pip=hand_landmarks[6]
        distence2=(index_finger_pip[0]-index_finger_tip[0])**2+(index_finger_pip[1]-index_finger_tip[1])**2
        result_distance2=math.sqrt(float(distence2))
        distence=(index_finger_tip[0]-middel_finger[0])**2+(index_finger_tip[1]-middel_finger[1])**2
        result_distance=math.sqrt(float(distence))
        real_result=int(distence)/int(distence2)

        if real_result<1.1:
          
            
        
          if cx-w//2<index_finger_tip[0]<cx+w and cy-h//2<index_finger_tip[1]<cy+h//2:
              color=0,255,0
              
              cx,cy=index_finger_tip[0],index_finger_tip[1]
          else:
              color=255,0,0
        
        
    # Draw a rectangle on the image
    cv2.rectangle(img, (cx-w//2,cy-h//2), (cx+w//2,cy+h//2), color, cv2.FILLED)
    cv2.imshow("image", img)
    cv2.resizeWindow("image", 800, 600)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(1) & 0xFF == ord('s'):
# press 's' key to save image
            filepath = "C:\\Users\\PC\\OneDrive\\Pictures\\img.png"
            cv2.imwrite(filepath, img)
            print("image saved")

cap.release()
cv2.destroyAllWindows()
    