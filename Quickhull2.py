import random
from Plot_Graphs import oneGraph, showGraph

# Stores the result (points of convex hull)
hull = [];
 
# Returns the side of point p with respect to line
# joining points p1 and p2.
def findSide(p1, p2, p):
    val = (p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0])
 
    if (val > 0):
        return 1
    if (val < 0):
        return -1
    return 0
 
# returns a value proportional to the distance
# between the point p and the line joining the
# points p1 and p2
def lineDist(p1, p2, p):
    return abs((p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0]))
 
# End points of line L are p1 and p2. side can have value
# 1 or -1 specifying each of the parts made by the line L
def quickHull(a, n, p1, p2, side):
    ind = -1
    max_dist = 0
 
    # finding the point with maximum distance
    # from L and also on the specified side of L.
    for i in range(n):
        temp = lineDist(p1, p2, a[i])
        if ((findSide(p1, p2, a[i]) == side) and (temp > max_dist)):
            ind = i
            max_dist = temp
 
    # If no point is found, add the end points
    # of L to the convex hull.
    if (ind == -1):
        hull.append(p1)
        hull.append(p2)
        return
 
    # Recur for the two parts divided by a[ind]
    quickHull(a, n, a[ind], p1, -findSide(a[ind], p1, p2))
    quickHull(a, n, a[ind], p2, -findSide(a[ind], p2, p1))

 
def printHull(a, n):
    # a[i].second -> y-coordinate of the ith point
    if (n < 3):
        print("Convex hull not possible")
        return
 
    # Finding the point with minimum and
    # maximum x-coordinate
    min_x = 0
    max_x = 0
    for i in range(n):
        if (a[i][0] < a[min_x][0]):
            min_x = i
        if (a[i][0] > a[max_x][0]):
            max_x = i
 
    # Recursively find convex hull points on
    # one side of line joining a[min_x] and
    # a[max_x]
    quickHull(a, n, a[min_x], a[max_x], 1)
 
    # Recursively find convex hull points on
    # other side of line joining a[min_x] and
    # a[max_x]
    quickHull(a, n, a[min_x], a[max_x], -1)
 
    return hull
 


a = [[0, 3], [1, 1], [2, 2], [4, 4],
        [0, 0], [1, 2], [3, 1], [3, 3]];


vertices = [[random.randint(0, 5), random.randint(0, 5)] for _ in range(10)]
vertices = list(map(list,{*map(tuple, vertices)}))

print(vertices)
n = len(vertices);
hull = printHull(vertices, n)

convex = list(map(list,{*map(tuple, hull)}))
print("The points in Convex Hull are:")
print(convex)

showGraph(vertices, convex)
