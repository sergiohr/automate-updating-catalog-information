#! /usr/bin/env python3

import os
import requests
import json

def catalog_data(url, descriptionDir):
    descriptionFiles = ['{}{}'.format(descriptionDir,n) for n in os.listdir(descriptionDir)]

    description = {}
    for descriptionFile in descriptionFiles:
        f = open(descriptionFile, 'r')
        lines = f.readlines()
        description['name'] = lines[0].rstrip('\n')
        description['weight'] = int(lines[1].rstrip('\n').strip(' lbs'))
        description['description'] = lines[2].rstrip('\n')
        description['image_name'] = descriptionFile.split('/')[-1].replace('txt','jpeg')
        
        response = requests.post(url, json=description)
        print(response.request.url)
        print(response.status_code)

if __name__ == '__main__':
    url = 'http://localhost/fruits/'
    user = os.getenv('USER')
    descriptionDirectory = '/home/{}/supplier-data/descriptions/'.format(user)
    catalog_data(url, descriptionDirectory)
