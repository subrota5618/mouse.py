
import cv2
import pyautogui
import numpy as np
import time

screen_resolution = (1920, 1080)  # Change this to match your screen resolution
output_filename = "record.mp4"  # Change this to your desired filename

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video_writer = cv2.VideoWriter(output_filename, fourcc, 20.0, screen_resolution)

duration = 8  # Change this to the desired duration of the recording (in seconds)
end_time = time.time() + duration

while time.time() < end_time:
    # Capture a screenshot of the screen
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)

    # Convert RGB image to BGR for video writing
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Write the frame to the video file
    video_writer.write(frame)


video_writer.release()
cv2.destroyAllWindows()


# pip install pyautogui
# pip install opencv-python

