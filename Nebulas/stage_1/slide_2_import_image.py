import matplotlib.pyplot as plt
import numpy as np

img = plt.imread("Barnard_68_nebula.jpg") #

fig, ax = plt.subplots()
# ax.imshow(img) #
ax.imshow(img, extent=[0, 640, 0, 640]) #

plt.xlim(0, 640)
plt.ylim(0, 640)

plt.savefig('slide_1_import_image.png')

