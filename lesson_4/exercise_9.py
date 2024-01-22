# 9.Line Segment
# You are given four real numbers - the coordinates of two points on a
# plane. The first two numbers are the x and y coordinates of the first point,
# and the last two numbers are the x and y coordinates of the second point.
# Output the length of the line segment bounded by the two points.

import math

x1, y1 = map(float, input("Enter the coordinates of the first point (x1 y1): ").split())
x2, y2 = map(float, input("Enter the coordinates of the second point (x2 y2): ").split())

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Length of the line segment:", distance)
