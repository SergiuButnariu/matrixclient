import matplotlib.pyplot as plt
import numpy as np 

import PIL 
from PIL import Image 

im = Image.open('face.png')
im2 = Image.open('face.png')



data = np.asarray(im)
data2 = np.asarray(im2)

print(data)

data2 = data2 * 2.0

# for i in range(768):
#     for j in range(1024):
#         for k in range(3):
#             if data2[i, j , k] > 255:
#                 data2[i, j, k] = 255
#                 print("limitare")

data2 = data2.astype(np.uint8)
# indices = np.where(data2 > 255)


data3 = np.concatenate((data, data2), axis=0)

data3 = Image.fromarray(data3)

data3.save('face2.png')


