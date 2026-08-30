import cv2
from ultralytics import YOLO

model = YOLO("yolo26n.pt")

cap = cv2.VideoCapture(0)

roi_x1 = 150
roi_y1 = 100
roi_x2 = 490
roi_y2 = 400

while True:
    ret,frame = cap.read()

    if not ret:
        break

    results = model(frame,conf=0.5)
    result = results[0]
    annotated_frame = result.plot()
    cv2.rectangle(
        annotated_frame,
        (roi_x1, roi_y1),
        (roi_x2, roi_y2),
        (255, 0, 0),
        2
    )

    status = "No Person Detected"

    for i in range(len(result.boxes)):
        cls = int(result.boxes.cls[i])
        if cls != 0 :
            continue
        box = result.boxes.xyxy[i].cpu().numpy()

        x1,y1,x2,y2 = map(int,box)

        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2

        inside_roi = (
            roi_x1 <= center_x <= roi_x2
            and
            roi_y1 <= center_y <= roi_y2
        )

        if inside_roi:
            status = "SAFE"
        else:
            status = "DANGER"

        cv2.putText(
            annotated_frame,
            status,
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        print("Inside ROI:", inside_roi)

    cv2.circle(
        annotated_frame,
        (center_x, center_y),
        5,
        (0, 0, 255),
        -1
    )
    cv2.imshow("webcam",annotated_frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break
        

cap.release()
cv2.destroyAllWindows()