from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from constantes import *
from math import sqrt
from secciones import SeccionICHA

#Inicializar modelo
ret = Reticulado()

ret.abrir("04a_ejemplo_reticulado_guardar.h5")

coordenadas_nodos=ret.fid["xyz"]
secciones=ret.fid["secciones"]
barras=ret.fid["barras"]
restricciones=ret.fid["restricciones"]
restricciones_val=ret.fid["restricciones_val"]
cargas=ret.fid["cargas"]
cargas_val=ret.fid["cargas_val"]
c1="#3A8431"
c2="#A3500B"
colores=[c2,c2,c1,c1,c2,c2,c1,c2,c2,c1,c2,c2,c1,c2,c2,c2,c2,c2,c2,c2]

#Nodos
#print(coordenadas_nodos[:,:])
for i in coordenadas_nodos:
	x=i[0]
	#print(x)
	y=i[1]
	#print(y)
	z=i[2]
	#print(z)
	ret.agregar_nodo(x=x,y=y,z=z)

#Crear y agregar las barras
cont1=0
for seccion in secciones:
	print(f"seccion{seccion}")
	sec=[]
	sec.append(str(seccion[cont1]))
	sec.append(str(colores[cont1]))
	a=SeccionICHA(sec[0],sec[1])
	ret.agregar_barra(Barra(barras[cont1][0], barras[cont1][1], a))
	cont1+=1


#Crear restricciones
cont2=0
for i in restricciones:
	#print(f"restricciones={i}")
	nodo=i[0]
	gdl=i[1]
	valor=restricciones_val[cont2]
	ret.agregar_restriccion(nodo, gdl, valor)
	cont2+=1

#Agregar carga puntual
cont3=0
for i in cargas:
	nodo=i[0]
	gdl=[1]
	valor= cargas_val[cont3]
	cont3+=1

#ret.agregar_nodo()

#Visualizar y comprobar las secciones
opciones_barras = {
	"ver_secciones_en_barras": True,
	"color_barras_por_seccion": True,
}
ver_reticulado_3d(ret,opciones_barras=opciones_barras)

