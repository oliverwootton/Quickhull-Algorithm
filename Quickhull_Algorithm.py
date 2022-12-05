def findSide(p1, p2, p):
	val = (p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0])
	if (val > 0):
		return 1
	if (val < 0):
		return -1
	return 0;

def lineDist(p1, p2, p):
	return abs((p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0]))

def quickHull(a, n, p1, p2, side):
    ind = -1;
    max_dist = 0;

    for i in range(n):
        temp = lineDist(p1, p2, a[i])
        if ((findSide(p1, p2, a[i]) == side) and (temp > max_dist)):
            ind = i
            max_dist = temp

    if (ind == -1):
        if p1 not in hull:
            hull.append(p1)
        elif p2 not in hull:
            hull.append(p2)
        return

    quickHull(a, n, a[ind], p1, -findSide(a[ind], p1, p2))
    quickHull(a, n, a[ind], p2, -findSide(a[ind], p2, p1))


def printHull(a, n):
    if (n < 3):
        console.log("Convex hull not possible")
        return
    min_x = 0
    max_x = 0
    for i in range(n):
        if (a[i][0] < a[min_x][0]):
            min_x = i
        if (a[i][0] > a[max_x][0]):
            max_x = i
            
    quickHull(a, n, a[min_x], a[max_x], 1)
    
    quickHull(a, n, a[min_x], a[max_x], -1)

    print("The points in Convex Hull are:")
 
    for point in hull:
        print(point)
    

hull = [];

a = [[0, 3], [1, 1], [2, 2], [4, 4], [0, 0], [1, 2], [3, 1], [3, 3]]
n = len(a);
printHull(a, n);
