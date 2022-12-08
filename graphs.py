import matplotlib.pyplot as plt

# Splits the vertices into x and y values
def points(vertices):
    x = []
    y = []
    for coord in vertices:
        x.append(coord[0])
        y.append(coord[1])
    return x, y

def plotGraph(vertices, n, convexHull):
    # Splits the vertices into x and y values
    x, y = points(vertices)
    
    f = plt.figure(n)

    # Plotting the points
    if n == 0:
        plt.plot(x, y, marker='o', linestyle = 'none' ,markerfacecolor='green', markersize=6)
        # Giving a title to my graph
        plt.title('Graph of points without convex hull')
    else:
        x2, y2 = points(convexHull)
        # Joins the convex hull to itself to show the area covered
        x2.append(x2[0])
        y2.append(y2[0])
        plt.plot(x, y, marker='o', linestyle = 'none' ,markerfacecolor='green', markersize=6)
        plt.plot(x2, y2, marker='o', linestyle = 'dashed' ,markerfacecolor='red', markersize=6)
        # Giving a title to my graph
        plt.title('Graph of points with convex hull')
    
    # This sorts the y values from lowest to highest
    sortedY = sorted(y, key=lambda x: x)
    
    # setting x and y axis range
    plt.ylim(sortedY[0]-1, sortedY[-1]+1)
    plt.xlim(x[0]-1, x[-1]+1)

    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')
    
def showGraph(vertices, convexHull):
    # Function to display a before and after graph
    for i in range(2):
        plotGraph(sorted(vertices, key=lambda x: x[0]), i, convexHull)
        print(i)

    # function to show the plot
    plt.show()
    