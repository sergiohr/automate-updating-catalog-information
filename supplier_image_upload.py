#! /usr/bin/env python3

import requests
import os

homedir = os.getenv("HOME")
imagesdir = homedir + "/supplier-data/images/"
images = os.listdir(imagesdir)

url = "http://localhost/upload/"

for image in images:
    if os.path.splitext(image)[1] == ".jpeg":
        with open(imagesdir + image, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
