import cv2
cap = cv2.VideoCapture(0)  # 0 represents the default camera index
while True:
    ret, frame = cap.read()
    cv2.imshow("Web Camera", frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFBBF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
