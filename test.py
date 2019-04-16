import cv2
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    _,frame = cap.read()
    cv2.imshow("output", frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
#释放资源
cap.release()
cv2.destroyAllWindows()