import numpy as np
import matplotlib.pyplot as plt

// test

class Line:
  def __init__(self, length, angle):
    self.length = length
    self.angle = angle
    self.radianAngle = np.deg2rad(angle)

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def plot_lines(lines):
    start = Point(0,0)
    for line in lines:
        #length, angle = line
        #angle_rad = np.deg2rad(line.angle)
        x = start.x + line.length * np.cos(line.radianAngle)
        y = start.y + line.length * np.sin(line.radianAngle)
        end = Point(x,y)
        plt.plot([start.x, end.x], [start.y, end.y], label=f'Length: {line.length}, Angle: {line.angle} degrees')
        start = end
    plt.plot([0,end.x],[0,end.y])


# Define lines as arrays [length, angle] where angle is in degrees
line1 = Line(3, 70)  # Line 1 with length 3 and angle 30 degrees
line2 = Line( length=3,angle=10)  # Line 2 with length 4 and angle 120 degrees

# Plot lines
plt.figure()
plot_lines([line1, line2])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Simple robot')
plt.legend()
plt.grid()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
