#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import os
from PIL import Image
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class AppIcon:
    ios_lists = [{'name': 'app_store.png', 'size': 1024}, 
        {'name': 'iphone_app@3x.png', 'size': 180}, 
        {'name': 'iphone_app@2x.png', 'size': 120}, 
        {'name': 'iphone_settings@3x.png', 'size': 87}, 
        {'name': 'iphone_settings@2x.png', 'size': 58}, 
        {'name': 'iphone_notification@3x.png', 'size': 60}, 
        {'name': 'iphone_notification@2x.png', 'size': 40}, 
        {'name': 'iphone_spotlight@3x.png', 'size': 120}, 
        {'name': 'iphone_spotlight@2x.png', 'size': 80}]

    ios_ipad_lists = [
        {'name': 'ipad_app@2x.png', 'size': 152}, 
        {'name': 'ipad_app.png', 'size': 76}, 
        {'name': 'ipad_settings@2x.png', 'size': 58}, 
        {'name': 'ipad_settings.png', 'size': 29}, 
        {'name': 'ipad_notification@2x.png', 'size': 40}, 
        {'name': 'ipad_notification.png', 'size': 20}, 
        {'name': 'ipad_spotlight@2x.png', 'size': 80}, 
        {'name': 'ipad_spotlight.png', 'size': 40},
        {'name': 'ipad_pro@2x.png', 'size': 167}]

    def creatImages(self):
        path = './AppIcon.appiconset/app_store.png'
        has = os.path.exists(path)
        if bool(has):
            img = Image.open(path)
            for icon in self.ios_lists:
                name = icon['name']
                size = icon['size']
                out = img.resize((size, size),Image.ANTIALIAS)
                out.save('./AppIcon.appiconset/' + name, 'png')
                print(name,size)
        else:
            print('no 1024.png')
            
if __name__ == '__main__':

    icon = AppIcon()
    icon.creatImages()

