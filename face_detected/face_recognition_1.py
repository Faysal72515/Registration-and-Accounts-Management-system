import cv2
import matplotlib.pyplot as plt
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture("video1.mp4")

while cap.isOpened():
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)

    # display the output
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

#====================================================
if cap.isOpened():
    ret, frame =cap.read()
    print(ret)
    print(frame)

else:
    ret=False

img1 = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)


plt.imshow(img1)
plt.title("Camera Image-1")
plt.xticks([])
plt.yticks([])
plt.show()
cap.release()