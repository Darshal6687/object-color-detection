# import cv2

# import numpy as np

# cap = cv2.VideoCapture(0)

# while True:
#     frame = cap.read()
#     hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

#     cv2.imshow("Frame" ,frame)

#     key = cv2.waitKey(1)
#     if key == 27:
#         break
    

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Correct unpacking

    if not ret:
        print("Failed to grab frame")
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:  # ESC key
        break

# cap.release()
# cv2.destroyAllWindows()
