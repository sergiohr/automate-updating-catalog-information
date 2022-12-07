#!/usr/bin/env python3

from PIL import Image
import os

homedir = os.getenv("HOME")
imagesdir = homedir + "/supplier-data/images/"
images = os.listdir(imagesdir)

for image in images:
    im = Image.open(imagesdir + image).convert("RGB")
    image = image.replace("tiff","jpeg")
    print(image)
    im.resize((600,400)).save(imagesdir + image, "JPEG")

