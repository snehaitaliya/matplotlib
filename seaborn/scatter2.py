import matplotlib.pyplot as plt

height = [150, 155, 160, 165, 170, 175, 180]
weight = [45, 50, 55, 60, 65, 70, 75]

plt.scatter(height, weight, color="red", marker="o")
plt.title("Height vs Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.grid(True)
plt.show()