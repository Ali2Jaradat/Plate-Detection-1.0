import cv2
from PIL import Image

pcc = cv2.CascadeClassifier('Cascade Classifire.xml')

cap = cv2.VideoCapture('Samples/Sample.mp4')
  
while True: 
  
    ret, img = cap.read() 
  
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plates = pcc.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in plates:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) 
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        cv2.imwrite('detection.jpg', roi_color)
    Detection_Read = cv2.imread('detection.jpg')
    cv2.imshow('detection', Detection_Read)  

        
    cv2.imshow('before',img)


   

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
  
     

cap.release()  
cv2.destroyAllWindows() 