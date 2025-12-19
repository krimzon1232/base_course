import matplotlib.pyplot as plt

x=[3, 8, 5]
y=[7, 4, 9]

plt.title("Graphik")
plt.plot(x, y, color="r", label="asfdsfddf", marker=">", ms=7)
plt.plot(y, x, color="b", label="kgjgh", marker="o", ms=3)

plt.xlabel("X: ")
plt.ylabel("Y: ")
plt.legend()
plt.grid()

plt.savefig("img.jpg")

