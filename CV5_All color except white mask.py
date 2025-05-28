import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Proper unpacking

    if not ret:
        print("Failed to grab frame")
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define  color range in HSV
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])

    # Create mask for  color
    _mask = cv2.inRange(hsv_frame, low, high)

    # Apply mask to original frame
    result = cv2.bitwise_and(frame, frame, mask=_mask)

    # Show original and -filte frames
    cv2.imshow("Frame", frame)
    cv2.imshow("Result",result )

    key = cv2.waitKey(1)
    if key == 27:  # ESC key
        break

# cap.release()
# cv2.destroyAllWindows()
