import math
from graphs import showGraph

def partition(x1, x2, v):
    """
    Partition the coordinates to be below the line x1-x2
    
    Args:
        x1:         First coordinate of the line
        x2:         Second coordinate of the line
        v:          list of coordinates
        
    Returns:
        2 lists:    First list are the coordinates above the line,
                    Second list are the coordinates below the line
    """
    above = []
    below = []
    
    # Line is vertical so there are no points above or below it
    if x2[0] - x1[0] == 0:
        return above, below

    # Calculate m and c for y = mx + c    
    m = (x2[1] - x1[1]) / (x2[0] - x1[0])
    c = -m * x1[0] + x1[1]
    
    # Iterate over the coordinates to put them in the correct list
    for coord in v:
        # y > mx + c is above the line
        if coord[1] > m * (coord[0]) + c:
            above.append(coord)
        # y < mx + c is below the line
        elif coord[1] < m * (coord[0]) + c:
            below.append(coord)
    return above, below

def findDistance(x1, x2, x3):
    """
    Find the distance between the line x1-x2 and a point x3
    
    Args:
        x1:         First coordinate on the line
        x2:         Second coordinate on the line
        x3:         Point to measure the distance from
        
    Returns:
        return:     Distance between the line and the point
    """
    
    # Using ax + by + c = 0
    a = x1[1] - x2[1]
    b = x2[0] - x1[0]
    c = x1[0] * x2[1] - x2[0] * x1[1]
    # Dot product to find the distance between the line and a point
    return abs(a*x3[0] + b*x3[1] + c)/math.sqrt(a*a + b*b)

def quickHull2(x1, x2, region, side):
    """
    Recursivly calculates the point furthest away adds point to the 
    hull and repeats on the new region not in the hull
    
    Args:
        x1, x2: 
        region: 
        side:       Determines the whether the points are above 
                    or below the line
        
    Returns:
        list: Coordinates of the convex hull
    """
    
    # Exit for the recursion
    if region == [] or x1 is None or x2 is None:
        return []
    
    convexHull = []
    
    # Calculate the distance of everypoint from the line to find the furthest point
    furthestDistance = -1
    furthestPoint = None
    for point in region:
        distance = findDistance(x1, x2, point)
        if distance > furthestDistance:
            furthestDistance = distance
            furthestPoint = point
            
            
    convexHull += [furthestPoint]
    
    # Remove the point that is now apart of the convex hull
    region.remove(furthestPoint)
    
    # determine the partition formed from two line x1-furthestPoint and x2-furthestPoint
    point1above, point1below = partition(x1, furthestPoint, region)
    point2above, point2below = partition(x2, furthestPoint, region)
    
    # Only use the partition in the same direction (opposite direction is contained in the convex hull)
    if side == "above":
        convexHull += quickHull2(x1, furthestPoint, point1above, side)
        convexHull += quickHull2(furthestPoint, x2, point2above, side)
    else:
        convexHull += quickHull2(x1, furthestPoint, point1below, side)
        convexHull += quickHull2(furthestPoint, x2, point2below, side)
        
    return convexHull
    
def quickHull(vertices):
    """
    Calculate the convex hull of the set of vertices:
    
    Args:
        vertices (integers):    2D array of coordinates (x, y)
        
    Returns:
        list:                   Coordinates of the convex hull
    """
    
    N = len(vertices)
    if (N <= 2):
        print("Convex hull not possible")
        return
    convexHull = []
    
    # Finds the nearest and furthest away points on the x-axis
    sortedPoints = sorted(vertices, key=lambda x: x[0])
    x1 = sortedPoints[0]
    x2 = sortedPoints[-1]
    
    # Adds the points to the convex hull
    convexHull += [x1, x2]
    
    # Removes points that are now apart of the convex hull
    sortedPoints.pop(0)
    sortedPoints.pop(-1)
    
    # Determine the points located above and below the line
    above, below = partition(x1, x2, sortedPoints)
    convexHull += quickHull2(x1, x2, above, "above")
    convexHull += quickHull2(x1, x2, below, "below")
    
    return convexHull
    

# vertices = [[0, 3], [1, 1], [2, 2], 
#             [4, 4], [0, 0], [1, 2], 
#             [3, 1], [3, 3],
#             ]

vertices = [[1, 0], [2, 1], [3, 2], 
            [4, 4], [0, 0], [0, 2], 
            [4, 5], [6, 3], [5, 1],
            [6, 4], [4, 2], [2, 5]
            ]

convexHull = sorted(quickHull(vertices), key=lambda x: x[0])
showGraph(vertices, convexHull)
