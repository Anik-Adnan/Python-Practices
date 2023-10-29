# sin, sinh,asin, hypot , degrees , redians function
import math
a,b= 1 , 2
print(math.cos(a))
print(math.degrees(math.acos(.5))) # returns the sine of 'a' in radians
print(math.degrees(math.asin(.5))) # asin(.05) =  30 degree
print(math.cosh(b)) # returns the inverse hyperbolic cosine of 'b' in radians
print(math.atan(1)) # returns the arc tangent of 'pi' in radians

# hypot 
"""
Note that math.hypot(x, y) is also the length of the vector (or Euclidean distance) from the origin (0, 0)
to the point (x, y).
To compute the Euclidean distance between two points (x1, y1) & (x2, y2) you can use math.hypot as
follows
"""
print(math.hypot(a,b ))
x1,x2,y1,y2= 4, 2 ,6, 8 
print(math.hypot(x2 - x1, y2 - y1))
# degrees , redians 
print(math.pi) # 3.141592653589793
print(math.degrees(1))
print(math.radians(57.29577951308232))
