# -*- coding: utf-8 -*-
"""Code that contains the functions to generate the mosaic"""

import sys
from os import listdir, path
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2

PARAM = 25 #Number of Pixels of the each tile
TAR = 3000 #Number of Pixels of the output 

def create_mosaic(picture, path_database, param=PARAM):
    """Generate the mosaic"""

    pics, avgs = [], []
    for pic_name in listdir(path_database):
        pic = np.array(Image.open(path_database + "//" + pic_name))
        pic = cv2.resize(pic, (param, param), interpolation=cv2.INTER_AREA)
        pics.append(pic)
        avgs.append(np.mean(pic, axis=(0, 1)))

    source = resize(np.array(Image.open(picture)))
    height, width = source.shape[:2]
    output = np.zeros((height//param * param, width//param * param, 3))

    for i in range(height//param):
        for j in range(width//param):
            avg = np.mean(source[param*i:param*(i+1),
                                 param*j:param*(j+1)],
                          axis=(0, 1))
            deltas = np.linalg.norm(avgs-avg, axis=1)
            indice = np.unravel_index(np.argmin(deltas, axis=None), deltas.shape)[0]
            output[param*i: param*(i+1), param*j:param*(j+1)] = pics[indice]

    plt.imsave(f'./outputs/{path.basename(picture)} - mosaic.png', output.astype(np.uint8)/255)
    print("Image saved " + f'./outputs/{path.basename(picture)} - mosaic.png')


def resize(array):
    """Resize the image to match the target width and respect the picture ratio"""
    (height, width) = array.shape[:2]
    if height > width: #portrait mode
        dim = (int(width * TAR / float(height)), TAR)
    else:
        dim = (TAR, int(height * TAR / float(width)))
    return cv2.resize(array, dim, interpolation=cv2.INTER_AREA)


if __name__ == "__main__":
    
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        raise SyntaxError("Wrong number of arguments. Please provide :\n"
                          "  -picture path: path of the source picture \n"
                          "  -path database : path of the folder containing the database of pictures\n"
                          "  -pixel tile : optional, size in pixel of each square tile. Default 25\n")
                          
    elif len(sys.argv) == 3:
        create_mosaic(path.abspath(sys.argv[1]), sys.argv[2])

    else:
        create_mosaic(path.abspath(sys.argv[1]), sys.argv[2], int(sys.argv[3]))    
