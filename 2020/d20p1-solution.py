import numpy as np

with open("d20-input.txt") as fp:
    lines = fp.read().split("\n\n")

dm = lambda inp: (inp.split(":\n")[0], inp.split(":\n")[1].split("\n")) 
tiles = {int(dm(i)[0].split(" ")[1]): np.array([inp for ip in np.array(dm(i)[1]) for inp in ip]).reshape(10, 10) for i in lines}

tiles[3301]