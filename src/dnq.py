import matplotlib.pyplot as plt
import numpy as np
from Point import Point
from showCurve import showCurve
import time

# DIVIDE AND CONQUER
def midpoint(p1: Point, p2: Point):
    return Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)
    
def bezierCurve(P1,P2,P3,currIteration):
    curvePoint = []
    if(currIteration < iterations):
        
        midPoint1 = midpoint(P1,P2)
        midPoint2 = midpoint(P2,P3)
        midPoint3 = midpoint(midPoint1,midPoint2)

        currIteration += 1
        curvePoint.extend(bezierCurve(P1,midPoint1,midPoint3,currIteration))
        curvePoint.append(midPoint3)
        curvePoint.extend(bezierCurve(midPoint3,midPoint2,P3,currIteration))
    else:
        curvePoint.append(P1)
        curvePoint.append(P3)
    
    return curvePoint

 

def divideandConquer():
    P = []

    # Masukkan
    for i in range(3):
        while True:
            try:
                x, y = map(float, input("Masukkan koordinat x dan y titik ke-{} : ".format(i)).split())
                P.append(Point(x, y))
                break
            except ValueError:
                print("Invalid input. Please enter valid numerical values.")

    global iterations
    iterations = int(input("Masukkan jumlah iterasi: "))
   
    curve_points = []
   

    total_time = 0  
    for i in range(0, iterations+1):
        start_time = time.perf_counter()
        curve_points = bezierCurve(P[0], P[1], P[2], iterations - i)
        end_time = time.perf_counter()
        iteration_time = end_time - start_time  
        total_time += iteration_time  
        showCurve(P, curve_points)

    plt.title(f'Iteration {i}')
    
    average_time = total_time / (iterations + 1)  
    print("Rata-rata waktu eksekusi:", average_time * 1000, "ms")
    
    # for point in curve_points:
    #     print(point.x, point.y)
        
    