import streamlit as st
import cv2
import numpy as np

st.set_page_config(layout="wide")
st.title("🎯 Real-Time Color Object Detection")

# Sidebar options
st.sidebar.header("Detection Settings")
detect_red = st.sidebar.checkbox("Detect Red", value=True)
detect_blue = st.sidebar.checkbox("Detect Blue", value=True)
detect_green = st.sidebar.checkbox("Detect Green", value=True)
detect_other = st.sidebar.checkbox("Detect All Except White", value=True)

FRAME_WINDOW = st.image([])

cap = cv2.VideoCapture(0)

def process_frame(frame):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = np.zeros(frame.shape[:2], dtype=np.uint8)

    if detect_red:
        low_red = np.array([161, 155, 84])
        high_red = np.array([179, 255, 255])
        mask |= cv2.inRange(hsv_frame, low_red, high_red)

    if detect_blue:
        low_blue = np.array([94, 80, 2])
        high_blue = np.array([126, 255, 255])
        mask |= cv2.inRange(hsv_frame, low_blue, high_blue)

    if detect_green:
        low_green = np.array([25, 52, 72])
        high_green = np.array([102, 255, 255])
        mask |= cv2.inRange(hsv_frame, low_green, high_green)

    if detect_other:
        low = np.array([0, 42, 0])
        high = np.array([179, 255, 255])
        mask |= cv2.inRange(hsv_frame, low, high)

    result = cv2.bitwise_and(frame, frame, mask=mask)
    return result

# Live stream loop
stframe = st.empty()
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        st.warning("Failed to access webcam.")
        break

    processed = process_frame(frame)
    processed = cv2.cvtColor(processed, cv2.COLOR_BGR2RGB)
    stframe.image(processed, channels="RGB")

# Cleanup (not used in Streamlit flow directly, as loop breaks on rerun or stop)
cap.release()
