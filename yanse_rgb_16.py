#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import os
from PIL import Image
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class YSColor:
    def decodeToRGB(self, rgb):
        RGB = rgb.split(',')
        color = '#'
        for i in RGB:
            num = int(i)
            # 将R、G、B分别转化为16进制拼接转换并大写  hex() 函数用于将10进制整数转换成16进制，以字符串形式表示
            color += str(hex(num))[-2:].replace('x', '0').upper()
        print(rgb,color)
        return color

    def decodeTo16(self, hex):
        r = int(hex[1:3],16)
        g = int(hex[3:5],16)
        b = int(hex[5:7], 16)
        rgb = str(r)+', '+str(g)+', '+str(b)
        print(hex,rgb)
        return rgb
    
    def printStart(self):
        print('\033[0;37;40m') 
        print("/****RGB颜色值与十六进制颜色码转换工具****/")
    
    def printEnd(self):
        print('\033[0m')

    def printTest(self):
        print('\033[0m这是显示方式0')
        print('\033[1m这是显示方式1')
        print('\033[4m这是显示方式4')
        print('\033[5m这是显示方式5')
        print('\033[7m这是显示方式7')
        print('\033[8m这是显示方式8')
        print('\033[30m这是前景色0')
        print('\033[31m这是前景色1')
        print('\033[32m这是前景色2')
        print('\033[33m这是前景色3')
        print('\033[34m这是前景色4')
        print('\033[35m这是前景色5')
        print('\033[36m这是前景色6')
        print('\033[37m这是前景色7')
        print('\033[40m这是背景色0')
        print('\033[41m这是背景色1')
        print('\033[42m这是背景色2')
        print('\033[43m这是背景色3')
        print('\033[44m这是背景色4')
        print('\033[45m这是背景色5')
        print('\033[46m这是背景色6')
        print('\033[47m这是背景色7')




if __name__ == '__main__':

    color = YSColor()
    color.printStart()
    color.decodeToRGB("143, 132, 16")
    color.decodeTo16("#ED63A8")
    color.printEnd()

