#dropbox.com/s/th0u3mpsl71fxit/CertificateTemplate.jpg

from PIL import Image, ImageDraw, ImageFont
img= Image.open("apis/CertificateTemplate.jpg")

import matplotlib.pyplot as plt 
import numpy as np 

def print_image(img):
  plt.imshow(np.array(img))             #every pixel's rgb value is stored in an array
  plt.show()

import cv2                #computer vision. used in image editing

img=cv2.imread("apis/CertificateTemplate.jpg")

def generate_certificate(img, name="Enter Name"):
  generate_image=img.copy()         #copies the image
  font=cv2.FONT_HERSHEY_SIMPLEX
  cordinates=(700,750)
  font_size=3.5
  font_color=(51,51,51)
  font_thickness= 10
  cv2.putText(generate_image,name,cordinates,font,font_size,font_color,font_thickness)         #order is same for the function putText which puts text in the image
  return generate_image

def save_image(img,name):
  path="./certi_{}.jpg".format(name)
  print(cv2.imwrite(path,img))

name=input("Enter the name you want on certificate: ")

generated_image=generate_certificate(img,name)
save_image(generated_image,name)
