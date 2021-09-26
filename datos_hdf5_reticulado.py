import h5py
from matplotlib.pylab import *

f = h5py.File("ejemplo_reticulado.h5", "w")



t = linspace(0, 10, 1000)				#	divide tiempo entre 0 y 10, dando 1000 valores

y = sin(t)
y2 = 2*cos(t)
y3 = 10*tan(t)


f["t"] = t
f["y"] = y


f["datos_finales/y2"] = y2
f["datos_finales/y3"] = y3

figure(1)
plot(t, y)

show()