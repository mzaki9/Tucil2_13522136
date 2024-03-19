import numpy as np
import matplotlib.pyplot as plt
from Point import Point
from showCurve import showCurve
import time

# BRUTE FORCE  
def quadratic_bezier(p0: Point, p1: Point, p2: Point, t_values):
        return [Point((1 - t) * (1 - t) * p0.x + 2 * (1 - t) * t * p1.x + t * t * p2.x,
                    (1 - t) * (1 - t) * p0.y + 2 * (1 - t) * t * p1.y + t * t * p2.y) for t in t_values]

def bruteForce():
    P = []
    for i in range(3):
        while True:
            try:
                x, y = map(float, input("Masukkan koordinat x dan y titik ke-{} : ".format(i)).split())
                P.append(Point(x, y))
                break
            except ValueError:
                print("Invalid input. Please enter valid numerical values.")

    while(True):
        iterations = int(input("Masukkan jumlah iterasi: "))
        if iterations < 0:
            print("Iterasi tidak boleh negatif. Silakan input kembali.")
        else:
            break

    t_values = np.linspace(0, 1, 2**iterations + 1)
    start_time = time.perf_counter()
    curve_points = quadratic_bezier(P[0], P[1], P[2], t_values)
    # for point in curve_points:
    #     print(point.x, point.y)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print("Waktu eksekusi:", elapsed_time * 1000, "ms")
    showCurve(P, curve_points)
    plt.show()
    

# bruteForce()