import cv2
from PIL import Image

image_path = "wiscreenboc.jpeg"
face = cv2.CascadeClassifier('haarcascade_frontalface_extended.xml')

image = cv2.imread(image_path)
dog = face.detectMultiScale(image)

new_dog = Image.open(image_path).convert("RGBA")
oneye = Image.open('pngtree-pirate-hat-clipart-blue-eye-patch-png-image_2716448-removebg-preview.png').convert("RGBA")


for (x, y, w, h) in dog:
  cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
  oneye = oneye.resize((w, int(h/2)))
  new_dog.paste(oneye, (x, int(y+h/4)), oneye)
  new_dog.save("dog_with_oneye.png")

cv2.imshow('Dog', image)
cv2.waitKey()