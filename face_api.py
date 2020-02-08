import face_recognition
import cv2
import numpy as np
import sys

padding = 5
image = face_recognition.load_image_file("known_photos/johnny_depp.jpg")
print(image.shape)
face_locations = face_recognition.face_locations(image)
print(face_locations)
cv2.imshow('pic',image)
cropped = image[118 - padding:341 + padding,340 - padding:563 + padding,:]

cv2.imwrite('pic.jpg',cropped)

