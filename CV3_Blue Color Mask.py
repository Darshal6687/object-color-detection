import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Proper unpacking

    if not ret:
        print("Failed to grab frame")
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define blue color range in HSV
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])

    # Create mask for blue color
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)

    # Apply mask to original frame
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # Show original and blue-filteblue frames
    cv2.imshow("Frame", frame)
    cv2.imshow("blue", blue)

    key = cv2.waitKey(1)
    if key == 27:  # ESC key
        break

# cap.release()
# cv2.destroyAllWindows()
