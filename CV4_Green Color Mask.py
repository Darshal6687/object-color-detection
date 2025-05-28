import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Proper unpacking

    if not ret:
        print("Failed to grab frame")
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define green color range in HSV
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])

    # Create mask for green color
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)

    # Apply mask to original frame
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

    # Show original and green-filtegreen frames
    cv2.imshow("Frame", frame)
    cv2.imshow("green", green)

    key = cv2.waitKey(1)
    if key == 27:  # ESC key
        break

# cap.release()
# cv2.destroyAllWindows()
