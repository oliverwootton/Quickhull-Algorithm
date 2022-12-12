import matplotlib.pyplot as plt
import math

# Splits the vertices into x and y values
def points(vertices):
    x = []
    y = []
    for coord in vertices:
        x.append(coord[0])
        y.append(coord[1])
    return x, y

# Function to order the vertices to create a polygon 
def draw_polygon(points):
    out = [points[0]]
    current = points[0]

    swap = False
    while(len(out) < len(points)):
        next = None
        curr_dist = 0
        for point in points:
            if(point not in out):
                if(swap and point[1] <= current[1]):
                    if(next is None or dis(current, point) < curr_dist):
                        next = point
                        curr_dist = dis(current, point)
                elif(not swap and point[1] > current[1]):
                    if(next is None or dis(current, point) < curr_dist):
                        next = point
                        curr_dist = dis(current, point)
        if(next is None):
            swap = True
        else:
            out.append(next)
            current = next

    out.append(points[0])

    return out

# Function to calculate the distance
def dis(p1, p2):
    return math.sqrt(pow((p1[0]-p2[0]), 2)+pow((p1[1]-p2[1]), 2))

# Function to display a before and after gra
def plotGraph(vertices, convexHull):
    # Splits the vertices into x and y values
    x, y = points(vertices)
    
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 3))

    # Plotting the points
    for ax in (ax1, ax2):
        ax.plot(x, y, '.', color='k')
        if ax == ax1:
            ax.set_title('Given points')
        else:
            ax.set_title('Convex hull')
            x2, y2 = points(convexHull)
            ax.plot(x2, y2, 'o', mec='r', color='none', lw=1, markersize=10)
            
            # Uncomment for lines to be drawn around the convex hull
            # x2, y2 = points(draw_polygon(convexHull))
            # ax.plot(x2, y2, markersize=10)
            
        ax.set_xticks(range(x[-1] + 2))
        # This sorts the y values from lowest to highest
        sortedY = sorted(y, key=lambda x: x)
        ax.set_yticks(range(sortedY[-1] + 2))
    
def showGraph(vertices, convexHull):
    plotGraph(sorted(vertices, key=lambda x: x[0]), convexHull)
    plt.show()
 
# Function to output one graph   
def oneGraph(vertices):
    x, y = points(vertices)
    plt.plot(x, y, '.', color='k')
    plt.show()
