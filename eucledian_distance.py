import math
x1=float(input("Enter x1 value"))
x2=float(input("Enter x2 value"))
y1=float(input("Enter y1 value"))
y2=float(input("Enter y2 value"))
x=[x1,y1]
y=[x2,y2]
ed=(math.dist(x,y),2)
print("Euclidean distance for x, y is ",ed)