import matplotlib.pyplot as hadi
import numpy as np

hadi.rcParams["font.family"] = "Book Antiqua"
hadi.rcParams.update({'font.size': 11.5})

x1 = [3, 2, 1, 0, -1, -2, -3]      
y1 = [107.044, 107.063, 107.124, 107, -64.147, -235.436, -406.638]

x2 = [3, 2, 1, 0, -1, -2, -3]      
y2 = [430.225, 751.858, 598.677, 428.000, 256.908, 85.701, -85.484]

x3 = [3, 2, 1, 0, -1, -2, -3]      
y3 = [1475.779, 1305.088, 1134.084, 963.000, 791.904, 620.679, 449.567]

x4 = [3, 2, 1, 0, -1, -2, -3]      
y4 = [2225.402, 2054.262, 1883.146, 1712.000, 1540.825, 1369.673, 1198.477]

hadi.xlabel(r'$E$ (V/nm)')
hadi.ylabel(r'$K$$_{s}$ (µJ/m²)')

hadi.plot(x1, y1, marker="o", color="red")
hadi.plot(x2, y2, marker="o", color="orange")
hadi.plot(x3, y3, marker="o", color="blue")
hadi.plot(x4, y4, marker="o", color="green")

hadi.legend([r"$t$$_{free}$ = 0.5 nm", r"$t$$_{free}$ = 1 nm", r"$t$$_{free}$ = 1.5 nm", r"$t$$_{free}$ = 2 nm"])
hadi.show()
