import cv2
from ultralytics import YOLO
import pyttsx3

model = YOLO("yolo26n.pt")
engine = pyttsx3.init()

cap = cv2.VideoCapture(0)

roi_x1 = 150
roi_y1 = 100
roi_x2 = 490
roi_y2 = 400

alert_triggered = False

while True:
    ret,frame = cap.read()

    if not ret:
        break

    results = model.track(frame,conf=0.5,persist=True)
    result = results[0]
    ids = result.boxes.id
    print(ids)
    annotated_frame = result.plot()
    cv2.rectangle(
        annotated_frame,
        (roi_x1, roi_y1),
        (roi_x2, roi_y2),
        (255, 0, 0),
        2
    )

    status = "No Person Detected"
    person_inside = False
    person_detected = False
    person_count=0

    for i in range(len(result.boxes)):
        cls = int(result.boxes.cls[i])
        if cls != 0 :
            continue
        if ids is None:
            continue

        track_id = int(result.boxes.id[i])
            
        person_detected=True
        person_count+=1

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
            person_inside = True
            person_status = "DANGER"
        else:
            person_status="Safe"

        label = f"ID {track_id}: {person_status}"

        if person_status == "DANGER" and not alert_triggered:
            print("Alert: Person ID", track_id, "is in danger zone")

            engine.say(
                f"Person ID {track_id} is in the danger zone"
            )

            engine.runAndWait()

            alert_triggered = True

        cv2.circle(
            annotated_frame,
            (center_x, center_y),
            5,
            (0, 0, 255),
            -1
        )

    if person_detected:
        if person_inside:
            status = "DANGER"
        else:
            status = "SAFE"

    if person_detected and not person_inside:
        alert_triggered = False

    cv2.putText(
        annotated_frame,
        f"Status : {status}, Count : {person_count}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        annotated_frame,
        label,
        (x1, y1 - 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2
    )

    # print("Person Id",track_id,status)

    cv2.imshow("webcam",annotated_frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()