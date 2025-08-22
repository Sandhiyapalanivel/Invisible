
import cv2
import time
import numpy as np


cap = cv2.VideoCapture(0)

time.sleep(2)  


for i in range(30):
    ret, background = cap.read()


background = np.flip(background, axis=1)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = np.flip(frame, axis=1)  


    

    
   
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])

    
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2


    
    inverse_mask = cv2.bitwise_not(mask)

    
    cloak_area = cv2.bitwise_and(background, background, mask=mask)
    current_area = cv2.bitwise_and(frame, frame, mask=inverse_mask)
    combined = cv2.add(cloak_area, current_area)

    
    cv2.imshow("Invisible Cloak", combined)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

