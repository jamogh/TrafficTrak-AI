import cv2
import numpy as np
from time import sleep

min_width = 80  # Minimum width of the rectangle
min_height = 80  # Minimum height of the rectangle

offset = 6  # Allowed error between pixels

line_position = 550  # Position of the counting line

delay = 60  # FPS of the video

detections = []
car_count = 0


def get_center(x, y, w, h):
    x_center = int(w / 2)
    y_center = int(h / 2)
    cx = x + x_center
    cy = y + y_center
    return cx, cy


cap = cv2.VideoCapture('C:\\Users\\kushal\\Downloads\\Counting Cars\\video.mp4')
background_subtractor = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    time = float(1 / delay)
    sleep(time)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 5)
    img_sub = background_subtractor.apply(blur)
    dilate = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilated = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)
    dilated = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame, (25, line_position), (1200, line_position), (255, 127, 0), 3)

    for (i, c) in enumerate(contours):
        (x, y, w, h) = cv2.boundingRect(c)
        valid_contour = (w >= min_width) and (h >= min_height)
        if not valid_contour:
            continue

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        center = get_center(x, y, w, h)
        detections.append(center)
        cv2.circle(frame, center, 4, (0, 0, 255), -1)

        for (cx, cy) in detections:
            if line_position - offset < cy < line_position + offset:
                car_count += 1
                cv2.line(frame, (25, line_position), (1200, line_position), (0, 127, 255), 3)
                detections.remove((cx, cy))
                print("Car is detected: " + str(car_count))

    cv2.putText(frame, "VEHICLE COUNT: " + str(car_count), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
    cv2.imshow("Original Video", frame)
    cv2.imshow("Detection", dilated)

    if cv2.waitKey(1) == 27:  # ESC key to exit
        break

cv2.destroyAllWindows()
cap.release()
