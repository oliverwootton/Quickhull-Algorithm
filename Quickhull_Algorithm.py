import math
from Plot_Graphs import oneGraph, showGraph
import random

def findSide(x1, x2, x3):
    """
    Partition the coordinates to be below the line x1-x2
    Args:
        x1:         First coordinate of the line
        x2:         Second coordinate of the line
        v:          List of vertices
    Returns:
        2 lists:    First list are the coordinates above the line,
                    Second list are the coordinates below the line
    """
    val = (x3[1] - x1[1]) * (x2[0] - x1[0]) - (x2[1] - x1[1]) * (x3[0] - x1[0])
 
    if (val > 0):
        return 1
    if (val < 0):
        return -1
    return 0

def findDistance(x1, x2, x3):
    """
    Find the distance between the line x1-x2 and a point x3
    Args:
        x1:         First coordinate of the line
        x2:         Second coordinate of the line
        x3:         Point to measure the distance from  
    Returns:
        return:     Distance between the line and the point
    """
    return abs((x3[1] - x1[1]) * (x2[0] - x1[0]) - (x2[1] - x1[1]) * (x3[0] - x1[0]))
 

def findHull(a, n, x1, x2, side):
    """
    Recursivly calculates the point furthest away adds point to the 
    hull and repeats on the new region not in the hull
    Args:
        x1:         First coordinate of the line
        x2:         Second coordinate of the line
        region:     The points that remain outside the convex hull 
                    on the outside of the line
        side:       Determines the whether the points are above or
                    below the line
    Returns:
        list: Coordinates of the convex hull
    """
    ind = -1
    max_dist = 0
    
    for i in range(n):
        temp = findDistance(x1, x2, a[i])
        if ((findSide(x1, x2, a[i]) == side) and (temp > max_dist)):
            ind = i
            max_dist = temp
    
    convexHull = []
    
    if (ind == -1):
        convexHull.append(x1)
        convexHull.append(x2)
        return convexHull
    print(convexHull)
 
    # Recur for the two parts divided by a[ind]
    convexHull += findHull(a, n, a[ind], x1, -findSide(a[ind], x1, x2))
    convexHull += findHull(a, n, a[ind], x2, -findSide(a[ind], x2, x1))
    return convexHull

    
def quickHull(vertices):
    """
    Calculate the convex hull of the set of vertices:
    Args:
        vertices (integers):    2D array of coordinates (x, y) 
    Returns:
        list:                   Coordinates of the convex hull
    """
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
    # one side of line joining a[min_x] and
    # a[max_x]
    convexHull += findHull(vertices, n, x1, x2, 1)
 
    # Recursively find convex hull points on
    # other side of line joining a[min_x] and
    # a[max_x]
    convexHull += findHull(vertices, n, x1, x2, -1) 
    return convexHull

vertices = [[0, 3], [1, 1], [2, 2], 
            [4, 4], [0, 0], [1, 2], 
            [3, 1], [3, 3],
            ]

# vertices = [[1, 0], [2, 1], [3, 2], 
#             [4, 4], [0, 0], [0, 2], 
#             [4, 5], [6, 3], [5, 1],
#             [6, 4], [4, 2], [2, 5]
#             ]

vertices = [[random.randint(0, 6), random.randint(0, 6)] for _ in range(10)]
vertices = list(map(list,{*map(tuple, vertices)}))

convexHull = quickHull(vertices)
convexHull = list(map(list,{*map(tuple,convexHull)}))
convexHull = sorted(convexHull, key=lambda x: x[0])

print(vertices)
print(convexHull)

showGraph(vertices, convexHull)
