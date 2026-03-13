import matplotlib.pyplot as plt
import numpy as np

img = plt.imread("image.png")
fig, ax = plt.subplots()
ax.imshow(img, extent=[0, 640, 0, 640])


def circle(R, x0, y0, starst, stop, step):
    t=np.arange(starst, stop, step)
    x = x0 + R * np.cos(t)
    y = y0 + R * np.sin(t)
    return x, y


plt.plot([235, 380], [300, 625], lw=2, color='w')
plt.savefig('slide_2_paint_image.png')

coords = circle(125, 375, 500, 0, np.pi/2, 0.1)
plt.plot(coords[0], coords[1], lw=2, color='w')
plt.savefig('slide_2_paint_image.png')

plt.plot([380+120, 440], [625-125, 400], lw=2, color='w')
plt.savefig('slide_2_paint_image.png')

coords = circle(75, 625-125-135, 400, 3 * np.pi / 2 + np.pi / 16, np.pi * 2, 0.1)
plt.plot(coords[0], coords[1], lw=2, color='w')
plt.savefig('slide_2_paint_image.png')

coords = circle(75, 625-125-190, 400-95, np.pi, 2 * np.pi + np.pi / 9, 0.2)
plt.plot(coords[0], coords[1], lw=2, color='w')
plt.savefig('slide_2_paint_image.png')

# plt.plot([240, 150], [290, 230], lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')


# plt.plot([180, 280], [175, 220], lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(150, 300, 370, np.pi+np.pi/2.15, 2*np.pi-np.pi/6, 0.1)
# plt.plot(coords[0], coords[1], lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(120, 320, 345, 2*np.pi-np.pi/6, 2*np.pi+np.pi/1.27, 0.1)
# plt.plot(coords[0], coords[1], lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')

