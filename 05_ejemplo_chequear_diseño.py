from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from constantes import *
from math import sqrt
from secciones import SeccionICHA

L = 6.*m_
H = 6.*m_
B = 4.*m_

q = 400*kgf_/m_**2

F = B*L*q

nodos_apoyo=open("posibles-apoyos-2021.txt","r")

x = []
z = []


for i in nodos_apoyo:
    valor=i.split(" ")
    valor[0]=x.append(float(valor[0]))
    valor[1]=z.append(float(valor[1]))


xsum = 0 

for n in range(len(x)):
    print(f"coordenada x {n} = {x[n]}  -  z {n} = {z[n]}")

    if n >= 7 and n <= 28:
        xsum += x[n]







#Inicializar modelo
ret = Reticulado()

#Nodos

#TABLERO 											---- Parte Baja y = 0
ret.agregar_nodo(x[7]*m_		- L		,0, z[7])
ret.agregar_nodo(x[7]*m_	     		,0, z[7])
ret.agregar_nodo(x[7]*m_	 	+ L		,0, z[7])
ret.agregar_nodo(x[7]*m_	 + 2*L   	,0, z[7])
ret.agregar_nodo(x[7]*m_	 + 3*L   	,0, z[7])
ret.agregar_nodo(x[7]*m_	 + 4*L   	,0, z[7])
ret.agregar_nodo(x[7]*m_	 + 5*L   	,0, z[7])
ret.agregar_nodo(x[7]*m_	 + 6*L   	,0, z[7])
ret.agregar_nodo(x[7]*m_	 + 7*L   	,0, z[7])
ret.agregar_nodo(x[7]*m_	 + 8*L   	,0, z[7])
ret.agregar_nodo(x[7]*m_	 + 9*L   	,0, z[7])
ret.agregar_nodo(x[7]*m_	 + 10*L   	,0, z[7])
ret.agregar_nodo(x[7]*m_	 + 11*L   	,0, z[7])
ret.agregar_nodo(x[7]*m_	 + 12*L   	,0, z[7])
ret.agregar_nodo(x[7]*m_	 + 13*L   	,0, z[7])
ret.agregar_nodo(x[7]*m_	 + 14*L   	,0, z[7])
ret.agregar_nodo(x[7]*m_	 + 15*L   	,0, z[7])
ret.agregar_nodo(x[7]*m_	 + 16*L   	,0, z[7])
ret.agregar_nodo(x[7]*m_	 + 17*L   	,0, z[7])
ret.agregar_nodo(x[7]*m_	 + 18*L   	,0, z[7])
ret.agregar_nodo(x[7]*m_	 + 19*L   	,0, z[7])
ret.agregar_nodo(x[7]*m_	 + 20*L   	,0, z[7])
ret.agregar_nodo(x[28]*m_			 	,0, z[7])
ret.agregar_nodo(x[7]*m_	 + 22*L   	,0, z[7])

#TABLERO 											---- Parte Alta y = 0
ret.agregar_nodo(x[7]*m_	 - L		,0, z[7] + H)
ret.agregar_nodo(x[7]*m_	     		,0, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + L		,0, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 2*L   	,0, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 3*L   	,0, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 4*L   	,0, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 5*L   	,0, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 6*L   	,0, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 7*L   	,0, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 8*L   	,0, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 9*L   	,0, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 10*L   	,0, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 11*L   	,0, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 12*L   	,0, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 13*L   	,0, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 14*L   	,0, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 15*L   	,0, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 16*L   	,0, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 17*L   	,0, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 18*L   	,0, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 19*L   	,0, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 20*L   	,0, z[7] + H)
ret.agregar_nodo(x[28]*m_  		 		,0, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 22*L   	,0, z[7] + H)


#TABLERO 											---- Parte Baja y = 4 m
ret.agregar_nodo(x[7]*m_	     		,B, z[7])
ret.agregar_nodo(x[7]*m_	 - L		,B, z[7])
ret.agregar_nodo(x[7]*m_	 + L		,B, z[7])
ret.agregar_nodo(x[7]*m_	 + 2*L   	,B, z[7])
ret.agregar_nodo(x[7]*m_	 + 3*L   	,B, z[7])
ret.agregar_nodo(x[7]*m_	 + 4*L   	,B, z[7])
ret.agregar_nodo(x[7]*m_	 + 5*L   	,B, z[7])
ret.agregar_nodo(x[7]*m_	 + 6*L   	,B, z[7])
ret.agregar_nodo(x[7]*m_	 + 7*L   	,B, z[7])
ret.agregar_nodo(x[7]*m_	 + 8*L   	,B, z[7])
ret.agregar_nodo(x[7]*m_	 + 9*L   	,B, z[7])
ret.agregar_nodo(x[7]*m_	 + 10*L   	,B, z[7])
ret.agregar_nodo(x[7]*m_	 + 11*L   	,B, z[7])
ret.agregar_nodo(x[7]*m_	 + 12*L   	,B, z[7])
ret.agregar_nodo(x[7]*m_	 + 13*L   	,B, z[7])
ret.agregar_nodo(x[7]*m_	 + 14*L   	,B, z[7])
ret.agregar_nodo(x[7]*m_	 + 15*L   	,B, z[7])
ret.agregar_nodo(x[7]*m_	 + 16*L   	,B, z[7])
ret.agregar_nodo(x[7]*m_	 + 17*L   	,B, z[7])
ret.agregar_nodo(x[7]*m_	 + 18*L   	,B, z[7])
ret.agregar_nodo(x[7]*m_	 + 19*L   	,B, z[7])
ret.agregar_nodo(x[7]*m_	 + 20*L   	,B, z[7])
ret.agregar_nodo(x[28]*m_			 	,B, z[7])
ret.agregar_nodo(x[7]*m_	 + 22*L   	,B, z[7])

#TABLERO 											---- Parte Alta y = 4 m
ret.agregar_nodo(x[7]*m_	 - L		,B, z[7] + H)
ret.agregar_nodo(x[7]*m_	     		,B, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + L		,B, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 2*L   	,B, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 3*L   	,B, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 4*L   	,B, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 5*L   	,B, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 6*L   	,B, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 7*L   	,B, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 8*L   	,B, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 9*L   	,B, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 10*L   	,B, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 11*L   	,B, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 12*L   	,B, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 13*L   	,B, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 14*L   	,B, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 15*L   	,B, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 16*L   	,B, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 17*L   	,B, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 18*L   	,B, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 19*L   	,B, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 20*L   	,B, z[7] + H)
ret.agregar_nodo(x[28]*m_  		 		,B, z[7] + H)
ret.agregar_nodo(x[7]*m_	 + 22*L   	,B, z[7] + H)


#Secciones de las barras
seccion_grande = SeccionICHA("[]350x150x37.8", color="#3A8431")#, debug=True)
seccion_chica = SeccionICHA("[]80x40x8", color="#A3500B")

#Crear y agregar las barras



ret.agregar_barra(Barra(0, 1, seccion_chica)) #0
ret.agregar_barra(Barra(1, 2, seccion_chica)) #1
ret.agregar_barra(Barra(3, 4, seccion_grande)) #2
ret.agregar_barra(Barra(0, 3, seccion_grande)) #3
ret.agregar_barra(Barra(3, 1, seccion_chica)) #4
ret.agregar_barra(Barra(1, 4, seccion_chica)) #5
ret.agregar_barra(Barra(4, 2, seccion_grande)) #6
ret.agregar_barra(Barra(5, 6, seccion_chica)) #7
ret.agregar_barra(Barra(6, 7, seccion_chica)) #8
ret.agregar_barra(Barra(5, 3, seccion_grande)) #9
ret.agregar_barra(Barra(3, 6, seccion_chica)) #10
ret.agregar_barra(Barra(6, 4, seccion_chica)) #11
ret.agregar_barra(Barra(4, 7, seccion_grande)) #12
ret.agregar_barra(Barra(0, 5, seccion_chica)) #13
ret.agregar_barra(Barra(1, 6, seccion_chica)) #14
ret.agregar_barra(Barra(2, 7, seccion_chica)) #15
ret.agregar_barra(Barra(0, 6, seccion_chica)) #15
ret.agregar_barra(Barra(1, 5, seccion_chica)) #15
ret.agregar_barra(Barra(6, 2, seccion_chica)) #15
ret.agregar_barra(Barra(1, 7, seccion_chica)) #15


#Crear restricciones
for nodo in [0,5]:
	ret.agregar_restriccion(nodo, 0, 0)
	ret.agregar_restriccion(nodo, 1, 0)
	ret.agregar_restriccion(nodo, 2, 0)

for nodo in [2,7]:
	ret.agregar_restriccion(nodo, 1, 0)
	ret.agregar_restriccion(nodo, 2, 0)




#Visualizar y comprobar las secciones
opciones_barras = {
	# "ver_secciones_en_barras": True,
	"color_barras_por_seccion": True,
}
ver_reticulado_3d(ret,opciones_barras=opciones_barras)

# exit(0)



#Resolver el problema peso_propio
ret.ensamblar_sistema(factor_peso_propio=[0.,0.,-1.], factor_cargas=0.0)
ret.resolver_sistema()
f_D = ret.obtener_fuerzas()


#Agregar fuerzas tablero
ret.agregar_fuerza(0, 2, -F/4)
ret.agregar_fuerza(5, 2, -F/4)
ret.agregar_fuerza(2, 2, -F/4)
ret.agregar_fuerza(7, 2, -F/4)
ret.agregar_fuerza(1, 2, -F/2)
ret.agregar_fuerza(6, 2, -F/2)

#Resolver el problema peso_propio
ret.ensamblar_sistema(factor_peso_propio=[0.,0.,0], factor_cargas=1.0)
ret.resolver_sistema()
f_L = ret.obtener_fuerzas()



#Visualizar f_L en el reticulado
opciones_nodos = {
	"usar_posicion_deformada": False,
}

opciones_barras = {
	"color_barras_por_dato": True,
	"ver_dato_en_barras" : True,
	"dato":f_L
}

ver_reticulado_3d(ret, 
	opciones_nodos=opciones_nodos, 
	opciones_barras=opciones_barras,
	titulo="Carga Viva")


#Visualizar f_L en el reticulado
opciones_nodos = {
	"usar_posicion_deformada": False,
}

opciones_barras = {
	"color_barras_por_dato": True,
	"ver_dato_en_barras" : True,
	"dato":f_D
}

ver_reticulado_3d(ret, 
	opciones_nodos=opciones_nodos, 
	opciones_barras=opciones_barras,
	titulo="Carga Muerta")


#Calcular carga ultima (con factores de mayoracion)
fu = 1.2*f_D + 1.6*f_L



#Visualizar combinacion en el reticulado
opciones_nodos = {
	"usar_posicion_deformada": False,
}

opciones_barras = {
	"color_barras_por_dato": True,
	"ver_dato_en_barras" : True,
	"dato":fu
}

ver_reticulado_3d(ret, 
	opciones_nodos=opciones_nodos, 
	opciones_barras=opciones_barras,
	titulo="1.2D + 1.6L")





cumple = ret.chequear_diseño(fu, ϕ=0.9)

if cumple:
	print(":)  El reticulado cumple todos los requisitos")
else:
	print(":(  El reticulado NO cumple todos los requisitos")

#Calcular factor de utilizacion para las barras
factores_de_utilizacion = ret.obtener_factores_de_utilizacion(fu, ϕ=0.9)


#Visualizar FU en el reticulado
opciones_nodos = {
	"usar_posicion_deformada": False,
	# "factor_amplificacion_deformada": 1.,
}

opciones_barras = {
	"color_barras_por_dato": True,
	"ver_dato_en_barras" : True,
	"dato":factores_de_utilizacion
}


ver_reticulado_3d(ret, 
	opciones_nodos=opciones_nodos, 
	opciones_barras=opciones_barras,
	titulo="Factor Utilizacion")


ret.guardar("05_ejemplo_chequear_diseño.h5")