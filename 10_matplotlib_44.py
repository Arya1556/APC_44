#line plot

"""import matplotlib.pyplot as plt
plt.plot ([1,2,3],[4,5,6])
plt.show()  

import matplotlib.pyplot as plt
plt.plot([1,2,3],[4,5,6],color="red")
plt.xlim(1,5)
plt.ylim(1,6)
plt.xlabel("x-axis")
plt.ylabel("y-axis")  
plt.show()                                                                                                  

#bar plot
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y = [10, 25, 15, 30, 20, 35, 40]

plt.bar(x, y, label="Bar")
plt.title("Bar Chart")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()
plt.show()

#scatter plot
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y = [10, 25, 15, 30, 20, 35, 40]

plt.scatter(x, y, color="red", label="Points")

plt.title("Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()
plt.show()


#pie plot
import matplotlib.pyplot as plt

x = [30, 25, 20, 15, 10]
labels = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

plt.pie(x, labels=labels, startangle=90)

plt.title("Fruit Pie Chart")
plt.show()


#histogram
import matplotlib.pyplot as plt

x = [12, 15, 18, 20, 22, 22, 25, 25, 28, 30,
     30, 32, 35, 35, 38, 40, 42, 45, 45, 50]

plt.hist(x, bins=5, color="skyblue", edgecolor="black")

plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.show()


#3D plot
import matplotlib.pyplot as plt

# Import 3D plotting tools
from mpl_toolkits.mplot3d import Axes3D

# Data points
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]
z = [5, 10, 15, 20, 25]

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.scatter(x, y, z, color="red", label="Points")

ax.set_title("3D Scatter Plot")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

ax.legend()
plt.show()


#subplot
import matplotlib.pyplot as plt

# First subplot: Line chart
plt.subplot(1, 2, 1)
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]
plt.plot(x, y)
plt.title("Line Plot")

# Second subplot: Bar chart
plt.subplot(1, 2, 2)
a = [1, 2, 3, 4, 5]
b = [5, 10, 15, 20, 25]
plt.bar(a, b)
plt.title("Bar Chart")

plt.tight_layout()
plt.show()"""