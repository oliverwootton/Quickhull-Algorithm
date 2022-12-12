from Plot_Graphs import oneGraph, showGraph
import random

"""
Returns the side of point x3 with respect to the line x1-x2
"""
def findSide(x1, x2, x3):
    val = (x3[1] - x1[1]) * (x2[0] - x1[0]) - (x2[1] - x1[1]) * (x3[0] - x1[0])
    
    if (val > 0):
        return 1
    if (val < 0):
        return -1
    return 0

"""
Returns a value proportional to the distance
between the point x3 and the line x1-x2
"""
def findDistance(x1, x2, x3):
    return abs((x3[1] - x1[1]) * (x2[0] - x1[0]) - (x2[1] - x1[1]) * (x3[0] - x1[0]))
 
"""
Args:
    x1 and x2:  The vertices of each end of the line L.
    side:       Represents each side of the partition made by the line L.
Returns:        The points furthest away from the line created
"""
def findHull(a, n, x1, x2, side):
    ind = -1
    max_dist = 0
    
    # Finding the point with maximum distance from L 
    # and also on the specified side of L.
    for i in range(n):
        temp = findDistance(x1, x2, a[i])
        if ((findSide(x1, x2, a[i]) == side) and (temp > max_dist)):
            ind = i
            max_dist = temp
    
    convexHull = []
    
    # If no point is found, add the end points
    # of L to the convex hull.
    if (ind == -1):
        convexHull.append(x1)
        convexHull.append(x2)
        return convexHull
 
    # Recursion for the two parts divided by a[ind]
    convexHull += findHull(a, n, a[ind], x1, -findSide(a[ind], x1, x2))
    convexHull += findHull(a, n, a[ind], x2, -findSide(a[ind], x2, x1))
    return convexHull

"""
Returns the convex hull of the set of vertices input
"""    
def quickHull(vertices):
    n = len(vertices)
    
    if (n <= 2):
        print("Convex hull not possible")
        return
    convexHull = []
    
    # Finds the nearest and furthest away points on the x-axis
    vertices = sorted(vertices, key=lambda x: x[0])
    x1 = vertices[0]
    x2 = vertices[-1]
    
    # Recursively find convex hull points on
    # one side of line joining x1 and x2
    convexHull += findHull(vertices, n, x1, x2, 1)
 
    # Recursively find convex hull points on
    # other side of line joining x1 and x2
    convexHull += findHull(vertices, n, x1, x2, -1) 
    return convexHull


# Randomly generate a set of coordinates
vertices = [[random.randint(0, 6), random.randint(0, 6)] for _ in range(10)]

convexHull = quickHull(vertices)
# Removes any repeated values in convexHull
convexHull = list(map(list,{*map(tuple,convexHull)}))
showGraph(vertices, convexHull)
convexHull = sorted(convexHull, key=lambda x: x[0])

print(vertices)
print(convexHull)
