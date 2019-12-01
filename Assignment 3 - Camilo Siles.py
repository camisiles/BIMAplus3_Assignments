#Iport the required libraries
import math

#Define the variables
n = int(input("Enter number of corners:"))   
ax = 0.0
sx = 0.0
sy = 0.0
ix = 0.0
iy = 0.0
ixy = 0.0
xt = 0.0
yt = 0.0
ixt = 0.0
iyt = 0.0
ixyt = 0.0

#Define lists for coordinates input 
x = []
y = []

#Input coordinates 
for i in range (n):
    x.append(float(input(f"Enter value for x{i+1}:")))
    y.append(float(input(f"Enter value for y{i+1}:")))

#Print coordinates list
print()
print(f"Point {'x':>6} {'y':>12}")
print("-" * 25)
for i in range (n):
    print(f"{i+1} {x[i]:10.2} {y[i]:10.2}")

#Calculate area of polygon

x.append(x[0])
y.append(y[0])

for i in range (n):
    ax = ((x[i+1]*y[i])-(x[i]*y[i+1])) + ax
ax = abs(ax/2)


#Calculate Sx of polygon
for i in range (n):
    sx = ((x[i+1] - x[i])*(y[i+1]**2 + y[i] * y[i+1] + y[i]**2)) + sx
sx = -(sx/6)

#Calculate Sy of polygon
for i in range (n):
    sy = ((y[i+1] - y[i])*(x[i+1]**2 + x[i] * x[i+1] + x[i]**2)) + sy
sy = (sy/6)

#Calculate Ix of polygon
for i in range (n):
    ix = ((x[i+1] - x[i])*(y[i+1]**3 + y[i+1]**2 * y[i] + y[i+1] * y[i]**2 + y[i]**3)) + ix
ix = -(ix/12)

#Calculate Iy of polygon
for i in range (n):
    iy = ((y[i+1] - y[i])*(x[i+1]**3 + x[i+1]**2 * x[i] + x[i+1] * x[i]**2 + x[i]**3)) + iy
iy = (iy/12)

#Calculate Ixy of polygon
for i in range (n):
    ixy = ((y[i+1] - y[i])*((y[i+1]*(3 * x[i+1]**2 + 2 * x[i+1] * x[i] + x[i]**2)) + y[i]*(3 * x[i]**2 + 2 * x[i+1] * x[i] + x[i+1]**2))) + ixy
ixy = -(ixy/24)

#Calculate xt of polygon
xt = sy/ax

#Calculate yt of polygon
yt = sx/ax

#Calculate ixt of polygon
ixt = ix - yt**2 * ax

#Calculate iyt of polygon
iyt = iy - xt**2 * ax

#Calculate ixyt of polygon
ixyt = ixy + xt * yt * ax

#Print results
print()
print(f"Area of the polygon (Ax): {ax:>18.2f}")
print(f"First moment of the polygon (Sx): {sx:>10.2f}")
print(f"First moment of the polygon (Sy): {sy:>10.2f}")
print(f"Second moment of the polygon (Ix): {ix:>9.2f}")
print(f"Second moment of the polygon (Iy): {iy:>9.2f}")
print(f"Second moment of the polygon (Ixy): {ixy:>8.2f}")
print(f"Coordinates of the centroid (xt): {xt:>10.2f}")
print(f"Coordinates of the centroid (yt): {yt:>10.2f}")
print(f"Moment of inertia (Ixt): {ixt:>19.2f}")
print(f"Moment of inertia (Iyt): {iyt:>19.2f}")
print(f"Moment of inertia (Ixyt): {ixyt:>18.2f}")