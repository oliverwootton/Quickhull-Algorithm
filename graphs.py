import matplotlib.pyplot as plt
import numpy as np

# Splits the vertices into x and y values
def points(vertices):
    x = []
    y = []
    for coord in vertices:
        x.append(coord[0])
        y.append(coord[1])
    return x, y

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
            # Joins the convex hull to itself to show the area covered
            x2.append(x2[0])
            y2.append(y2[0])
            ax.plot(x2, y2, 'o', mec='r', color='none', lw=1, markersize=10)
        ax.set_xticks(range(x[-1] + 2))
        # This sorts the y values from lowest to highest
        sortedY = sorted(y, key=lambda x: x)
        ax.set_yticks(range(sortedY[-1] + 2))
    
def showGraph(vertices, convexHull):
    # Function to display a before and after graph
    
    plotGraph(sorted(vertices, key=lambda x: x[0]), convexHull)

    # function to show the plot
    plt.show()
    