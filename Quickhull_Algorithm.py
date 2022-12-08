import math
from graphs import showGraph

def createRegion(x1, x2, v):
    above = []
    below = []
    
    if x2[0] - x1[0] == 0:
        return above, below
    
    m = (x2[1] - x1[1]) / (x2[0] - x1[0])
    c = -m * x1[0] + x1[1]
    
    for coord in v:
        if coord[1] > m * (coord[0]) + c:
            above.append(coord)
        elif coord[1] < m * (coord[0]) + c:
            below.append(coord)
    
    return above, below

def findDistance(x1, x2, x3):
    
    a = x1[1] - x2[1]
    b = x2[0] - x1[0]
    c = x1[0] * x2[1] - x2[0] * x1[1]  
    
    return abs(a*x3[0] + b*x3[1] + c)/math.sqrt(a*a + b*b)


# Calculate the convex hull of a set of vertices v
# 
def quickHull2(x1, x2, region, side):
    if region == [] or x1 is None or x2 is None:
        return []
    
    convexHull = []
    
    furthestDistance = -1
    furthestPoint = None
    
    for point in region:
        distance = findDistance(x1, x2, point)
        if distance > furthestDistance:
            furthestDistance = distance
            furthestPoint = point
            
            
    convexHull += [furthestPoint]
    region.remove(furthestPoint)
    
    point1above, point1below = createRegion(x1, furthestPoint, region)
    point2above, point2below = createRegion(x2, furthestPoint, region)
    
    if side == "above":
        convexHull += quickHull2(x1, furthestPoint, point1above, side)
        convexHull += quickHull2(furthestPoint, x2, point2above, side)
    else:
        convexHull += quickHull2(x1, furthestPoint, point1below, side)
        convexHull += quickHull2(furthestPoint, x2, point2below, side)
        
    return convexHull


def quickHull(vertices):
    N = len(vertices)
    if (N <= 2):
        print("Convex hull not possible")
        return
    convexHull = []
    
    # Finds the nearest and furthest away points on the x-axis
    sortedPoints = sorted(vertices, key=lambda x: x[0])
    x1 = sortedPoints[0]
    x2 = sortedPoints[-1]
    
    convexHull += [x1, x2]
    
    sortedPoints.pop(0)
    sortedPoints.pop(-1)
    
    # Determine the points located above and below the line
    above, below = createRegion(x1, x2, sortedPoints)
    convexHull += quickHull2(x1, x2, above, "above")
    convexHull += quickHull2(x1, x2, below, "below")
    
    sortedHull = sorted(convexHull, key=lambda x: x[0])
    
    return sortedHull
    

vertices = [[0, 3], [1, 1], [2, 2], [4, 4], [0, 0], [1, 2], [3, 1], [3, 3]]

showGraph(vertices, quickHull(vertices))
