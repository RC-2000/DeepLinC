import os
import numpy as np
from griddata import Grid




"""
list = []
deltas = []
values = []

filter = {""}

for line in reader:
    line = line.rstrip()
    words = line.split(" ")
    words = [word for word in words]
    if words[0] == "origin":
        x_org = float(words[1])
        y_org = float(words[2])
        z_org = float(words[3])
    elif words[0] == "delta":
        deltas.append([float(delta) for delta in words[1:]])

reader.close()
"""

#print("The origin is " + str((x_org, y_org, z_org)))
#print(deltas)

def get_coordinate(x, y, z, origin, deltas):
    zipped = zip(origin, [x * delta for delta in deltas[0]], [y * delta for delta in deltas[1]], [z * delta for delta in deltas[2]])
    return  tuple([sum(i) for i in zipped])

for item in os.listdir("DX Files"):
    path = "DX Files/" + item
    list = []
    deltas = []
    values = []

    filter = {""}

    reader = open(path)

    for line in reader:
        line = line.rstrip()
        words = line.split(" ")
        words = [word for word in words]
        if words[0] == "origin":
            x_org = float(words[1])
            y_org = float(words[2])
            z_org = float(words[3])
            origin = [x_org, y_org, z_org]
        elif words[0] == "delta":
            deltas.append([float(delta) for delta in words[1:]])
            print(deltas)

    reader.close()

    g = Grid(path)
    grid = g.grid

    cloud = []

    lst = grid.tolist()

    x, y, z = grid.shape
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if lst[i][j][k] != 0:
                    cloud.append(get_coordinate(i, j, k, origin, deltas))

    output = open("Coordinates/" + item + ".coords", "w")
    output.write(str(cloud))
    output.close()

    deltas = [[0.5, 0.0, 0.0], [0.0, 0.5, 0.0], [0.0, 0.0, 0.5]]
