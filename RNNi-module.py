import numpy as np
import cv2
import time
from random import seed
from random import random
# Read the image
startt=time.process_time()
image = cv2.imread('leftImg8bit/train/1/1.png',
                        cv2.IMREAD_UNCHANGED)
# fs=[focus size, layers of focus, height, width, mode, # of looks per image, random angle offset range in degrees, brightness, contrast]
# focus size, i.e. for 2x2 enter 2, for 4x4 enter 4, etc.;
# height and width, i.e. the height and width of largest focus;
# lf= layers of focus
# mode for rbg color is 3 or 1 for grayscale
# brightness and contrast are randomized between +- range. enter integer max value 127.

fs = [8, 7, 1024, 2048, 3, 200, 5, 10, 10]
if fs[4] == 1:
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
z = 0
n = [np.int_, cv2.resize, np.isscalar, np.vstack, np.zeros, np.append, cv2.getRotationMatrix2D,
     cv2.warpAffine]
id = image[0:fs[2]:, 0:fs[3]:]
seed()
X=[]
y=[]
label=1
# number of looks per image
while z < fs[5]:

    b = [random(), random()]
    cf = [n[0](b[0] * fs[2] / 2), n[0](b[1] * fs[3] / 2)]
    br = n[0]([b[0] * 255, b[1] * 255])
    i = 0
    fi = 0
    rot = n[0]((fs[6] + 1) - random() * (fs[6] + 1) * 2)
    rotm = n[6]((fs[0] / 2, fs[0] / 2), rot, 1)
    while i < fs[1]:
        p = [n[0]((fs[2] - fs[0] * 2 ** i) / 2 + cf[0]), n[0]((fs[2] + fs[0] * 2 ** i) / 2 + cf[0]),
             n[0]((fs[3] - fs[0] * 2 ** i) / 2 + cf[1]), n[0]((fs[3] + fs[0] * 2 ** i) / 2 + cf[1])]
        if p[0] < 0:
            j = id[0:fs[2]:, 0:fs[3]:]
        else:
            j = id[p[0]:p[1]:, p[2]:p[3]:]
        j = n[7](n[1](j, (fs[0], fs[0]), interpolation=3), rotm, (fs[0], fs[0]))
        j = j.flatten()
        if n[2](fi):
            fi = j
        else:
            fi = n[3]((fi, j))
        if i == (fs[1] - 1):
            # random adjust brightness/contrast
            bt = n[0](random() * fs[7] - fs[7] / 2)
            ct = n[0](random() * fs[8] - fs[8] / 2)
            fi = n[0](fi * (ct / 127 + 1) - ct + bt)
            # add final row with coordinates
            k = n[4]((fs[4] * fs[0] ** 2 - 2, 1))
            k = n[5](k, br)
            fi = n[3]((fi, k))
        i += 1
    image = fi
    # And append it and a label to the lists
    X.append(image)
    y.append(label)
    z += 1

print(image)
endt=time.process_time()

totalt=endt-startt

print(totalt)
