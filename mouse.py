import cv2
import numpy as np
import pyautogui
cap = cv2.VideoCapture(0)  # Use 0 for the default camera, or specify the camera index if multiple are available
while True:
    ret, frame = cap.read()  # Read a frame from the camera

    # Apply image processing techniques to detect and track the hand

    # Extract hand movements and calculate the desired cursor movement

    # Control the virtual mouse based on the cursor movement

    # Display the frame with overlays (e.g., hand tracking markers)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
