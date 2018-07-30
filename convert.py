#!/usr/bin/env python3
import glob

from PIL import Image

def convert(wildcard):
    '''
    Convert every JPEG into PNG
    '''
    fnames = list(glob.glob(wildcard))

    for i, fname in enumerate(fnames):
        print(fname)

        im = Image.open(fname)
        im.save(fname + '.png')

if __name__ == "__main__" :

    convert("source/*.jpg")