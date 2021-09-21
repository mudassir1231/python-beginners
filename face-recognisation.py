import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# if this does not work on vs code try writing the full path as shown below
# face_cascade = cv2.CascadeClassifier('C:\\python\\basic-projects\\face\\haarcascade_frontalface_default.xml')


# Read the input image
img = cv2.imread('test1.jpeg') # make sure u write wright extinsion like .jpj .jpeg .png .img

# if this does not work on vs code try writing the full path as shown below
# img = cv2.imread('C:\\python\\basic-projects\\face\\test1.jpeg')


# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 250, 0), 2)

# Display the output
cv2.imshow('img',img)
cv2.waitKey()
