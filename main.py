import cv2
import os

face_cascade = cv2.CascadeClassifier(r"haarcascade\haarcascade_frontalface_default.xml")

user_id = input("Enter User ID: ")

if not os.path.exists("dataset"):
    os.makedirs("dataset")

cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        count += 1
        cv2.imwrite(f"dataset/User.{user_id}.{count}.jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Face Attendance", frame)

    if cv2.waitKey(1) == 27 or count >= 100:
        break

cap.release()
cv2.destroyAllWindows()