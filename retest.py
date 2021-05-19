#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import os
from PIL import Image
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def imageList():
    in_path = '/Users/lijiajian/Downloads/召唤头像和背景/头像补充'
    out_path = '/Users/lijiajian/Downloads/召唤头像和背景/thumb头像/'
    for root, dirs, files in os.walk(in_path):
        index = 1
        for file in files :
            path = root + '/' +  file
            ext =  out_path + 'accompany_avatar_' + str(index) + '@3x.png'
            index = index + 1
            print(path)
            resizeImage(path,ext)

def resizeImage(filein, fileout):
    img = Image.open(filein)
    width = 200
    scale = float(img.height)/img.width
    height = int(scale * width)
    out = img.resize((width, height),Image.ANTIALIAS)
    #resize image with high-quality
    out.save(fileout, 'png')
    print(out)

def fileList():
    in_path = '/Users/lijiajian/Downloads/Icon'
    names = []
    for root, dirs, files in os.walk(in_path):
        for file in files :
            # print file
            names.append(file)
    json_str = json.dumps(names)
    s = json_str.decode('unicode-escape')
    print(s)
    with open('name.txt', 'w') as f:
        f.write(s)
    # print(f.read())

# imageList()
fileList()

