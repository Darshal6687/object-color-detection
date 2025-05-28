import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Proper unpacking

    if not ret:
        print("Failed to grab frame")
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define red color range in HSV
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])

    # Create mask for red color
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)

    # Apply mask to original frame
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

    # Show original and red-filtered frames
    cv2.imshow("Frame", frame)
    cv2.imshow("Red", red)

    key = cv2.waitKey(1)
    if key == 27:  # ESC key
        break

# cap.release()
# cv2.destroyAllWindows()
