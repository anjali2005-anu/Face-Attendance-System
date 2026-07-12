import cv2
import os
import numpy as np

dataset_path = "dataset"

faces = []
labels = []

for file in os.listdir(dataset_path):
    if file.endswith(".jpg"):
        path = os.path.join(dataset_path, file)

        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

        user_id = int(file.split(".")[1])

        faces.append(img)
        labels.append(user_id)

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.train(faces, np.array(labels))

recognizer.save("trainer.yml")

print("Model trained successfully!")