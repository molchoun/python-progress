from fileinput import filename
import sys
import os
from PIL import Image
import re


folders = sys.argv[1:]


def jpegtopng(folder1='images\\', folder2='new\\'):
    dir1 = f".\\{folders[0]}"
    dir2 = f".\\{folders[1]}"
    isdir = os.path.isdir(dir2)
    if not isdir:
        os.makedirs(dir2)
    for filename in os.listdir(dir1):
        img = Image.open(f'{dir1}{filename}')
        clean_name = os.path.splitext(filename)[0]
        img.save(f'{dir2}{clean_name}.png', 'png')
        print('All done!')


jpegtopng()
