import matplotlib.pyplot as plt
import numpy as np
from Point import Point

def showCurve(P : Point,curve_points):
    plt.clf()
    plt.scatter([point.x for point in P], [point.y for point in P], color='red', label='Control Points')
    plt.plot([point.x for point in curve_points], [point.y for point in curve_points], label='Quadratic Bezier Curve')
    plt.scatter([point.x for point in curve_points], [point.y for point in curve_points], color='blue', label='Points on Bezier Curve', alpha=0.5)

    for i in range(len(P)-1):
        plt.plot([P[i].x, P[i+1].x], [P[i].y, P[i+1].y], color='green', linestyle='--')

    

    plt.legend()
    plt.pause(1)