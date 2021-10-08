from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from constantes import *
from math import sqrt
from secciones import SeccionICHA

L = 6.*m_
H = 6.*m_
B = 4.*m_
L_TOTAL = 117.48*m_
q = 400*kgf_/m_**2

F = B*L_TOTAL*q

nodos_apoyo=open("posibles-apoyos-2021.txt","r")

x = []
z = []


for i in nodos_apoyo:
    valor=i.split(" ")
    valor[0]=x.append(float(valor[0]))
    valor[1]=z.append(float(valor[1]))





#Inicializar modelo
ret = Reticulado()

#Nodos

#TABLERO 											---- Parte Baja y = 0
ret.agregar_nodo(x[7]*m_		- L		,0, z[7]) # 0 
ret.agregar_nodo(x[7]*m_	     		,0, z[7]) # 1
ret.agregar_nodo(x[7]*m_	 	+ L		,0, z[7]) # 2
ret.agregar_nodo(x[7]*m_	 + 2*L   	,0, z[7]) # 3
ret.agregar_nodo(x[7]*m_	 + 3*L   	,0, z[7]) # 4
ret.agregar_nodo(x[7]*m_	 + 4*L   	,0, z[7]) # 5
ret.agregar_nodo(x[7]*m_	 + 5*L   	,0, z[7]) # 6
ret.agregar_nodo(x[7]*m_	 + 6*L   	,0, z[7]) # 7
ret.agregar_nodo(x[7]*m_	 + 7*L   	,0, z[7]) # 8
ret.agregar_nodo(x[7]*m_	 + 8*L   	,0, z[7]) # 9
ret.agregar_nodo(x[7]*m_	 + 9*L   	,0, z[7]) # 10
ret.agregar_nodo(x[7]*m_	 + 10*L   	,0, z[7]) # 11
ret.agregar_nodo(x[7]*m_	 + 11*L   	,0, z[7]) # 12
ret.agregar_nodo(x[7]*m_	 + 12*L   	,0, z[7]) # 13
ret.agregar_nodo(x[7]*m_	 + 13*L   	,0, z[7]) # 14
ret.agregar_nodo(x[7]*m_	 + 14*L   	,0, z[7]) # 15
ret.agregar_nodo(x[7]*m_	 + 15*L   	,0, z[7]) # 16
ret.agregar_nodo(x[7]*m_	 + 16*L   	,0, z[7]) # 17
ret.agregar_nodo(x[7]*m_	 + 17*L   	,0, z[7]) # 18
ret.agregar_nodo(x[7]*m_	 + 18*L   	,0, z[7]) # 19
ret.agregar_nodo(x[7]*m_	 + 19*L   	,0, z[7]) # 20
ret.agregar_nodo(x[28]*m_			 	,0, z[7]) # 21
ret.agregar_nodo(x[7]*m_	 + 21*L   	,0, z[7]) # 22

# TABLERO 											---- Parte Alta y = 0
ret.agregar_nodo(x[7]*m_	 - L		,0, z[7] + H) # 23 
ret.agregar_nodo(x[7]*m_	     		,0, z[7] + H) # 24
ret.agregar_nodo(x[7]*m_	 + L		,0, z[7] + H) # 25
ret.agregar_nodo(x[7]*m_	 + 2*L   	,0, z[7] + H) # 26
ret.agregar_nodo(x[7]*m_	 + 3*L   	,0, z[7] + H) # 27
ret.agregar_nodo(x[7]*m_	 + 4*L   	,0, z[7] + H) # 28
ret.agregar_nodo(x[7]*m_	 + 5*L   	,0, z[7] + H) # 29
ret.agregar_nodo(x[7]*m_	 + 6*L   	,0, z[7] + H) # 30
ret.agregar_nodo(x[7]*m_	 + 7*L   	,0, z[7] + H) # 31
ret.agregar_nodo(x[7]*m_	 + 8*L   	,0, z[7] + H) # 32
ret.agregar_nodo(x[7]*m_	 + 9*L   	,0, z[7] + H) # 33
ret.agregar_nodo(x[7]*m_	 + 10*L   	,0, z[7] + H) # 34
ret.agregar_nodo(x[7]*m_	 + 11*L   	,0, z[7] + H) # 35
ret.agregar_nodo(x[7]*m_	 + 12*L   	,0, z[7] + H) # 36
ret.agregar_nodo(x[7]*m_	 + 13*L   	,0, z[7] + H) # 37
ret.agregar_nodo(x[7]*m_	 + 14*L   	,0, z[7] + H) # 38
ret.agregar_nodo(x[7]*m_	 + 15*L   	,0, z[7] + H) # 39
ret.agregar_nodo(x[7]*m_	 + 16*L   	,0, z[7] + H) # 40
ret.agregar_nodo(x[7]*m_	 + 17*L   	,0, z[7] + H) # 41
ret.agregar_nodo(x[7]*m_	 + 18*L   	,0, z[7] + H) # 42
ret.agregar_nodo(x[7]*m_	 + 19*L   	,0, z[7] + H) # 43
ret.agregar_nodo(x[28]*m_  		 		,0, z[7] + H) # 44
ret.agregar_nodo(x[7]*m_	 + 21*L   	,0, z[7] + H) # 45


# TABLERO 											---- Parte Baja y = 4 m
ret.agregar_nodo(x[7]*m_	 - L		,B, z[7]) # 46
ret.agregar_nodo(x[7]*m_	     		,B, z[7]) # 47
ret.agregar_nodo(x[7]*m_	 + L		,B, z[7]) # 48
ret.agregar_nodo(x[7]*m_	 + 2*L   	,B, z[7]) # 49
ret.agregar_nodo(x[7]*m_	 + 3*L   	,B, z[7]) # 50
ret.agregar_nodo(x[7]*m_	 + 4*L   	,B, z[7]) # 51
ret.agregar_nodo(x[7]*m_	 + 5*L   	,B, z[7]) # 52
ret.agregar_nodo(x[7]*m_	 + 6*L   	,B, z[7]) # 53
ret.agregar_nodo(x[7]*m_	 + 7*L   	,B, z[7]) # 54
ret.agregar_nodo(x[7]*m_	 + 8*L   	,B, z[7]) # 55
ret.agregar_nodo(x[7]*m_	 + 9*L   	,B, z[7]) # 56
ret.agregar_nodo(x[7]*m_	 + 10*L   	,B, z[7]) # 57
ret.agregar_nodo(x[7]*m_	 + 11*L   	,B, z[7]) # 58
ret.agregar_nodo(x[7]*m_	 + 12*L   	,B, z[7]) # 59
ret.agregar_nodo(x[7]*m_	 + 13*L   	,B, z[7]) # 60
ret.agregar_nodo(x[7]*m_	 + 14*L   	,B, z[7]) # 61
ret.agregar_nodo(x[7]*m_	 + 15*L   	,B, z[7]) # 62
ret.agregar_nodo(x[7]*m_	 + 16*L   	,B, z[7]) # 63
ret.agregar_nodo(x[7]*m_	 + 17*L   	,B, z[7]) # 64
ret.agregar_nodo(x[7]*m_	 + 18*L   	,B, z[7]) # 65
ret.agregar_nodo(x[7]*m_	 + 19*L   	,B, z[7]) # 66
ret.agregar_nodo(x[28]*m_			 	,B, z[7]) # 67
ret.agregar_nodo(x[7]*m_	 + 21*L   	,B, z[7]) # 68

# TABLERO 											---- Parte Alta y = 4 m
ret.agregar_nodo(x[7]*m_	 - L		,B, z[7] + H) # 69
ret.agregar_nodo(x[7]*m_	     		,B, z[7] + H) # 70
ret.agregar_nodo(x[7]*m_	 + L		,B, z[7] + H) # 71
ret.agregar_nodo(x[7]*m_	 + 2*L   	,B, z[7] + H) # 72
ret.agregar_nodo(x[7]*m_	 + 3*L   	,B, z[7] + H) # 73
ret.agregar_nodo(x[7]*m_	 + 4*L   	,B, z[7] + H) # 74
ret.agregar_nodo(x[7]*m_	 + 5*L   	,B, z[7] + H) # 75
ret.agregar_nodo(x[7]*m_	 + 6*L   	,B, z[7] + H) # 76
ret.agregar_nodo(x[7]*m_	 + 7*L   	,B, z[7] + H) # 77
ret.agregar_nodo(x[7]*m_	 + 8*L   	,B, z[7] + H) # 78
ret.agregar_nodo(x[7]*m_	 + 9*L   	,B, z[7] + H) # 79
ret.agregar_nodo(x[7]*m_	 + 10*L   	,B, z[7] + H) # 80
ret.agregar_nodo(x[7]*m_	 + 11*L   	,B, z[7] + H) # 81
ret.agregar_nodo(x[7]*m_	 + 12*L   	,B, z[7] + H) # 82
ret.agregar_nodo(x[7]*m_	 + 13*L   	,B, z[7] + H) # 83
ret.agregar_nodo(x[7]*m_	 + 14*L   	,B, z[7] + H) # 84
ret.agregar_nodo(x[7]*m_	 + 15*L   	,B, z[7] + H) # 85
ret.agregar_nodo(x[7]*m_	 + 16*L   	,B, z[7] + H) # 86
ret.agregar_nodo(x[7]*m_	 + 17*L   	,B, z[7] + H) # 87
ret.agregar_nodo(x[7]*m_	 + 18*L   	,B, z[7] + H) # 88
ret.agregar_nodo(x[7]*m_	 + 19*L   	,B, z[7] + H) # 89
ret.agregar_nodo(x[28]*m_  		 		,B, z[7] + H) # 90
ret.agregar_nodo(x[7]*m_	 + 21*L   	,B, z[7] + H) # 91


#Secciones de las barras
seccion_grande = SeccionICHA("O310x300x5", color="#3A8431")#, debug=True) #O310x300x5
seccion_chica = SeccionICHA("[]300x100x18.3", color="#A3500B")   #300x100x18.3
seccion_extra = SeccionICHA("H400x150x47.6", color="pink")     #H400x150x47.6
seccion_chica_2 = SeccionICHA("[]12x12x0.3", color="blue")
seccion_chica_3 = SeccionICHA("[]100x50x8.5", color="black")

#Crear y agregar las barras


#HORIZONTALES
ret.agregar_barra(Barra(0, 1, seccion_grande)) #0
ret.agregar_barra(Barra(1, 2, seccion_extra)) #1
ret.agregar_barra(Barra(2, 3, seccion_grande)) #2
ret.agregar_barra(Barra(3, 4, seccion_grande)) #3
ret.agregar_barra(Barra(4, 5, seccion_grande)) #4
ret.agregar_barra(Barra(5, 6, seccion_grande)) #5
ret.agregar_barra(Barra(6, 7, seccion_grande)) #6
ret.agregar_barra(Barra(7, 8, seccion_grande)) #7
ret.agregar_barra(Barra(8, 9, seccion_grande)) #8
ret.agregar_barra(Barra(9, 10, seccion_grande)) #9
ret.agregar_barra(Barra(10, 11, seccion_grande)) #10
ret.agregar_barra(Barra(11, 12, seccion_grande)) #11
ret.agregar_barra(Barra(12, 13, seccion_grande)) #12
ret.agregar_barra(Barra(13, 14, seccion_grande)) #13
ret.agregar_barra(Barra(14, 15, seccion_grande)) #14
ret.agregar_barra(Barra(15, 16, seccion_grande)) #15
ret.agregar_barra(Barra(16, 17, seccion_grande)) #16
ret.agregar_barra(Barra(17, 18, seccion_grande)) #17
ret.agregar_barra(Barra(18, 19, seccion_grande)) #18
ret.agregar_barra(Barra(19, 20, seccion_grande)) #19
ret.agregar_barra(Barra(20, 21, seccion_extra)) #20
ret.agregar_barra(Barra(21, 22, seccion_grande)) #21
ret.agregar_barra(Barra(23, 24, seccion_extra)) #22
ret.agregar_barra(Barra(24, 25, seccion_grande)) #23
ret.agregar_barra(Barra(25, 26, seccion_grande)) #24
ret.agregar_barra(Barra(26, 27, seccion_grande)) #25
ret.agregar_barra(Barra(27, 28, seccion_grande)) #26
ret.agregar_barra(Barra(28, 29, seccion_grande)) #27
ret.agregar_barra(Barra(29, 30, seccion_grande)) #28
ret.agregar_barra(Barra(30, 31, seccion_grande)) #29
ret.agregar_barra(Barra(31, 32, seccion_grande)) #30
ret.agregar_barra(Barra(32, 33, seccion_grande)) #31
ret.agregar_barra(Barra(33, 34, seccion_grande)) #32
ret.agregar_barra(Barra(34, 35, seccion_grande)) #33
ret.agregar_barra(Barra(35, 36, seccion_grande)) #34
ret.agregar_barra(Barra(36, 37, seccion_grande)) #35
ret.agregar_barra(Barra(37, 38, seccion_grande)) #36
ret.agregar_barra(Barra(38, 39, seccion_grande)) #37
ret.agregar_barra(Barra(39, 40, seccion_grande)) #38
ret.agregar_barra(Barra(40, 41, seccion_grande)) #39
ret.agregar_barra(Barra(41, 42, seccion_grande)) #40
ret.agregar_barra(Barra(42, 43, seccion_grande)) #41
ret.agregar_barra(Barra(43, 44, seccion_grande)) #42
ret.agregar_barra(Barra(44, 45, seccion_grande)) #43

#VERTICALES
ret.agregar_barra(Barra(0, 23, seccion_extra)) #44
ret.agregar_barra(Barra(1, 24, seccion_grande)) #45
ret.agregar_barra(Barra(2, 25, seccion_grande)) #46
ret.agregar_barra(Barra(3, 26, seccion_grande)) #47
ret.agregar_barra(Barra(4, 27, seccion_grande)) #48
ret.agregar_barra(Barra(5, 28, seccion_grande)) #49
ret.agregar_barra(Barra(6, 29, seccion_grande)) #50
ret.agregar_barra(Barra(7, 30, seccion_grande)) #51
ret.agregar_barra(Barra(8, 31, seccion_grande)) #52
ret.agregar_barra(Barra(9, 32, seccion_grande)) #53
ret.agregar_barra(Barra(10, 33, seccion_grande)) #54
ret.agregar_barra(Barra(11, 34, seccion_grande)) #55
ret.agregar_barra(Barra(12, 35, seccion_grande)) #56
ret.agregar_barra(Barra(13, 36, seccion_grande)) #57
ret.agregar_barra(Barra(14, 37, seccion_grande)) #58
ret.agregar_barra(Barra(15, 38, seccion_grande)) #59
ret.agregar_barra(Barra(16, 39, seccion_grande)) #60
ret.agregar_barra(Barra(17, 40, seccion_grande)) #61
ret.agregar_barra(Barra(18, 41, seccion_grande)) #62
ret.agregar_barra(Barra(19, 42, seccion_grande)) #63
ret.agregar_barra(Barra(20, 43, seccion_grande)) #64
ret.agregar_barra(Barra(21, 44, seccion_grande)) #65
ret.agregar_barra(Barra(22, 45, seccion_grande)) #66

#VERTICALES
ret.agregar_barra(Barra(46, 69, seccion_extra)) #67
ret.agregar_barra(Barra(47, 70, seccion_grande)) #68
ret.agregar_barra(Barra(48, 71, seccion_grande)) #69
ret.agregar_barra(Barra(49, 72, seccion_grande)) #70
ret.agregar_barra(Barra(50, 73, seccion_grande)) #71
ret.agregar_barra(Barra(51, 74, seccion_grande)) #72
ret.agregar_barra(Barra(52, 75, seccion_grande)) #73
ret.agregar_barra(Barra(53, 76, seccion_grande)) #74
ret.agregar_barra(Barra(54, 77, seccion_grande)) #75
ret.agregar_barra(Barra(55, 78, seccion_grande)) #76
ret.agregar_barra(Barra(56, 79, seccion_grande)) #77
ret.agregar_barra(Barra(57, 80, seccion_grande)) #78
ret.agregar_barra(Barra(58, 81, seccion_grande)) #79
ret.agregar_barra(Barra(59, 82, seccion_grande)) #80
ret.agregar_barra(Barra(60, 83, seccion_grande)) #81
ret.agregar_barra(Barra(61, 84, seccion_grande)) #82
ret.agregar_barra(Barra(62, 85, seccion_grande)) #83
ret.agregar_barra(Barra(63, 86, seccion_grande)) #84
ret.agregar_barra(Barra(64, 87, seccion_grande)) #85
ret.agregar_barra(Barra(65, 88, seccion_grande)) #86
ret.agregar_barra(Barra(66, 89, seccion_grande)) #87
ret.agregar_barra(Barra(67, 90, seccion_grande)) #88
ret.agregar_barra(Barra(68, 91, seccion_grande)) #89

#HORIZONATALES
ret.agregar_barra(Barra(46, 47, seccion_grande)) #90
ret.agregar_barra(Barra(47, 48, seccion_extra)) #91
ret.agregar_barra(Barra(48, 49, seccion_grande)) #92
ret.agregar_barra(Barra(49, 50, seccion_grande)) #93
ret.agregar_barra(Barra(50, 51, seccion_grande)) #94
ret.agregar_barra(Barra(51, 52, seccion_grande)) #95
ret.agregar_barra(Barra(52, 53, seccion_grande)) #96
ret.agregar_barra(Barra(53, 54, seccion_grande)) #97
ret.agregar_barra(Barra(54, 55, seccion_grande)) #98
ret.agregar_barra(Barra(55, 56, seccion_grande)) #99
ret.agregar_barra(Barra(56, 57, seccion_grande)) #100
ret.agregar_barra(Barra(57, 58, seccion_grande)) #101
ret.agregar_barra(Barra(58, 59, seccion_grande)) #102
ret.agregar_barra(Barra(59, 60, seccion_grande)) #103
ret.agregar_barra(Barra(60, 61, seccion_grande)) #104
ret.agregar_barra(Barra(61, 62, seccion_grande)) #105
ret.agregar_barra(Barra(62, 63, seccion_grande)) #106
ret.agregar_barra(Barra(63, 64, seccion_grande)) #107
ret.agregar_barra(Barra(64, 65, seccion_grande)) #108
ret.agregar_barra(Barra(65, 66, seccion_grande)) #109
ret.agregar_barra(Barra(66, 67, seccion_extra)) #110
ret.agregar_barra(Barra(67, 68, seccion_grande)) #111
ret.agregar_barra(Barra(69, 70, seccion_extra)) #112
ret.agregar_barra(Barra(70, 71, seccion_grande)) #113
ret.agregar_barra(Barra(71, 72, seccion_grande)) #114
ret.agregar_barra(Barra(72, 73, seccion_grande)) #115
ret.agregar_barra(Barra(73, 74, seccion_grande)) #116
ret.agregar_barra(Barra(74, 75, seccion_grande)) #117
ret.agregar_barra(Barra(75, 76, seccion_grande)) #118
ret.agregar_barra(Barra(76, 77, seccion_grande)) #119
ret.agregar_barra(Barra(77, 78, seccion_grande)) #120
ret.agregar_barra(Barra(78, 79, seccion_grande)) #121
ret.agregar_barra(Barra(79, 80, seccion_grande)) #122
ret.agregar_barra(Barra(80, 81, seccion_grande)) #123
ret.agregar_barra(Barra(81, 82, seccion_grande)) #124
ret.agregar_barra(Barra(82, 83, seccion_grande)) #125
ret.agregar_barra(Barra(83, 84, seccion_grande)) #126
ret.agregar_barra(Barra(84, 85, seccion_grande)) #127
ret.agregar_barra(Barra(85, 86, seccion_grande)) #128
ret.agregar_barra(Barra(86, 87, seccion_grande)) #129
ret.agregar_barra(Barra(87, 88, seccion_grande)) #130
ret.agregar_barra(Barra(88, 89, seccion_grande)) #131
ret.agregar_barra(Barra(89, 90, seccion_grande)) #132
ret.agregar_barra(Barra(90, 91, seccion_grande)) #133

#BARRAS DE INFERIORES
ret.agregar_barra(Barra(0, 47, seccion_chica_2)) #134
ret.agregar_barra(Barra(1, 46, seccion_chica_2)) #135
ret.agregar_barra(Barra(1, 48, seccion_chica_2)) #136
ret.agregar_barra(Barra(2, 47, seccion_chica_2)) #137
ret.agregar_barra(Barra(3, 48, seccion_chica_2)) #138
ret.agregar_barra(Barra(2, 49, seccion_chica_2)) #139
ret.agregar_barra(Barra(3, 50, seccion_chica_2)) #140
ret.agregar_barra(Barra(4, 49, seccion_chica_2)) #141
ret.agregar_barra(Barra(5, 50, seccion_chica_2)) #142
ret.agregar_barra(Barra(4, 51, seccion_chica_2)) #143
ret.agregar_barra(Barra(6, 51, seccion_chica_2)) #144
ret.agregar_barra(Barra(5, 52, seccion_chica_2)) #145
ret.agregar_barra(Barra(7, 52, seccion_chica_2)) #146
ret.agregar_barra(Barra(6, 53, seccion_chica_2)) #147
ret.agregar_barra(Barra(8, 53, seccion_chica_2)) #148
ret.agregar_barra(Barra(7, 54, seccion_chica_2)) #149
ret.agregar_barra(Barra(9, 54, seccion_chica_2)) #150
ret.agregar_barra(Barra(8, 55, seccion_chica_2)) #151
ret.agregar_barra(Barra(10, 55, seccion_chica_2)) #152
ret.agregar_barra(Barra(9, 56, seccion_chica_2)) #153
ret.agregar_barra(Barra(11, 56, seccion_chica_2)) #154
ret.agregar_barra(Barra(10, 57, seccion_chica_2)) #155
ret.agregar_barra(Barra(12, 57, seccion_chica_2)) #156

ret.agregar_barra(Barra(11, 58, seccion_chica_2)) #157
ret.agregar_barra(Barra(12, 57, seccion_chica_2)) #158
ret.agregar_barra(Barra(13, 58, seccion_chica_2)) #159
ret.agregar_barra(Barra(12, 59, seccion_chica_2)) #160
ret.agregar_barra(Barra(14, 59, seccion_chica_2)) #161
ret.agregar_barra(Barra(13, 60, seccion_chica_2)) #162
ret.agregar_barra(Barra(15, 60, seccion_chica_2)) #163
ret.agregar_barra(Barra(14, 61, seccion_chica_2)) #164
ret.agregar_barra(Barra(16, 61, seccion_chica_2)) #165
ret.agregar_barra(Barra(15, 62, seccion_chica_2)) #166
ret.agregar_barra(Barra(17, 62, seccion_chica_2)) #167
ret.agregar_barra(Barra(16, 63, seccion_chica_2)) #168
ret.agregar_barra(Barra(18, 63, seccion_chica_2)) #169
ret.agregar_barra(Barra(17, 64, seccion_chica_2)) #170
ret.agregar_barra(Barra(19, 64, seccion_chica_2)) #171
ret.agregar_barra(Barra(18, 65, seccion_chica_2)) #172
ret.agregar_barra(Barra(20, 65, seccion_chica_2)) #173
ret.agregar_barra(Barra(19, 66, seccion_chica_2)) #174
ret.agregar_barra(Barra(21, 66, seccion_chica_2)) #175
ret.agregar_barra(Barra(20, 67, seccion_chica_2)) #176
ret.agregar_barra(Barra(22, 67, seccion_chica_2)) #177
ret.agregar_barra(Barra(21, 68, seccion_chica_2)) #178

#BARRAS DE FRENTE SUPERIORES
ret.agregar_barra(Barra(69, 24, seccion_chica_2)) #179
ret.agregar_barra(Barra(70, 23, seccion_chica_2)) #180
ret.agregar_barra(Barra(70, 25, seccion_chica_2)) #181
ret.agregar_barra(Barra(71, 24, seccion_chica_2)) #182
ret.agregar_barra(Barra(71, 26, seccion_chica_2)) #183
ret.agregar_barra(Barra(72, 25, seccion_chica_2)) #184
ret.agregar_barra(Barra(72, 27, seccion_chica_2)) #185
ret.agregar_barra(Barra(73, 26, seccion_chica_2)) #186
ret.agregar_barra(Barra(73, 28, seccion_chica_2)) #187
ret.agregar_barra(Barra(74, 27, seccion_chica_2)) #188
ret.agregar_barra(Barra(74, 29, seccion_chica_2)) #189
ret.agregar_barra(Barra(75, 28, seccion_chica_2)) #190
ret.agregar_barra(Barra(75, 30, seccion_chica_2)) #191
ret.agregar_barra(Barra(76, 29, seccion_chica_2)) #192
ret.agregar_barra(Barra(76, 31, seccion_chica_2)) #193
ret.agregar_barra(Barra(77, 30, seccion_chica_2)) #194
ret.agregar_barra(Barra(77, 32, seccion_chica_2)) #195
ret.agregar_barra(Barra(78, 31, seccion_chica_2)) #196
ret.agregar_barra(Barra(78, 33, seccion_chica_2)) #197
ret.agregar_barra(Barra(79, 32, seccion_chica_2)) #198
ret.agregar_barra(Barra(79, 34, seccion_chica_2)) #199
ret.agregar_barra(Barra(80, 33, seccion_chica_2)) #200
ret.agregar_barra(Barra(80, 35, seccion_chica_2)) #201

ret.agregar_barra(Barra(81, 34, seccion_chica_2)) #202
ret.agregar_barra(Barra(81, 36, seccion_chica_2)) #203
ret.agregar_barra(Barra(82, 35, seccion_chica_2)) #204
ret.agregar_barra(Barra(82, 37, seccion_chica_2)) #205
ret.agregar_barra(Barra(83, 36, seccion_chica_2)) #206
ret.agregar_barra(Barra(83, 38, seccion_chica_2)) #207
ret.agregar_barra(Barra(84, 37, seccion_chica_2)) #208
ret.agregar_barra(Barra(84, 39, seccion_chica_2)) #209
ret.agregar_barra(Barra(85, 38, seccion_chica_2)) #210
ret.agregar_barra(Barra(85, 40, seccion_chica_2)) #211
ret.agregar_barra(Barra(86, 39, seccion_chica_2)) #212
ret.agregar_barra(Barra(86, 41, seccion_chica_2)) #213
ret.agregar_barra(Barra(87, 40, seccion_chica_2)) #214
ret.agregar_barra(Barra(87, 42, seccion_chica_2)) #215
ret.agregar_barra(Barra(88, 41, seccion_chica_2)) #216
ret.agregar_barra(Barra(88, 43, seccion_chica_2)) #217
ret.agregar_barra(Barra(89, 42, seccion_chica_2)) #218
ret.agregar_barra(Barra(89, 44, seccion_chica_2)) #219
ret.agregar_barra(Barra(90, 43, seccion_chica_2)) #220
ret.agregar_barra(Barra(90, 45, seccion_chica_2)) #221
ret.agregar_barra(Barra(91, 44, seccion_chica_2)) #222

#DIAGONALES
ret.agregar_barra(Barra(23, 1, seccion_extra)) #223
ret.agregar_barra(Barra(24, 2, seccion_chica)) #224
ret.agregar_barra(Barra(25, 3, seccion_chica)) #225
ret.agregar_barra(Barra(26, 4, seccion_chica)) #226
ret.agregar_barra(Barra(27, 5, seccion_chica)) #227
ret.agregar_barra(Barra(28, 6, seccion_chica)) #228
ret.agregar_barra(Barra(29, 7, seccion_chica)) #229
ret.agregar_barra(Barra(30, 8, seccion_chica)) #230
ret.agregar_barra(Barra(31, 9, seccion_chica)) #231
# ret.agregar_barra(Barra(32, 10, seccion_chica_3)) #232
# ret.agregar_barra(Barra(33, 11, seccion_chica_3)) #233
# ret.agregar_barra(Barra(34, 12, seccion_chica_3)) #234
ret.agregar_barra(Barra(35, 13, seccion_chica_3)) #235
ret.agregar_barra(Barra(36, 14, seccion_chica_3)) #236
ret.agregar_barra(Barra(37, 15, seccion_chica_3)) #237
ret.agregar_barra(Barra(33, 9, seccion_chica_3)) #238
ret.agregar_barra(Barra(34, 10, seccion_chica_3)) #239
ret.agregar_barra(Barra(35, 11, seccion_chica_3)) #240
# ret.agregar_barra(Barra(36, 12, seccion_chica_3)) #241
# ret.agregar_barra(Barra(37, 13, seccion_chica_3)) #242
# ret.agregar_barra(Barra(38, 14, seccion_chica_3)) #243
ret.agregar_barra(Barra(39, 15, seccion_chica)) #244
ret.agregar_barra(Barra(40, 16, seccion_chica)) #245
ret.agregar_barra(Barra(41, 17, seccion_chica)) #246
ret.agregar_barra(Barra(42, 18, seccion_chica)) #247
ret.agregar_barra(Barra(43, 19, seccion_chica)) #248
ret.agregar_barra(Barra(44, 20, seccion_chica)) #249
ret.agregar_barra(Barra(45, 21, seccion_extra)) #250
ret.agregar_barra(Barra(69, 47, seccion_extra)) #251
ret.agregar_barra(Barra(70, 48, seccion_chica)) #252
ret.agregar_barra(Barra(71, 49, seccion_chica)) #253
ret.agregar_barra(Barra(72, 50, seccion_chica)) #254
ret.agregar_barra(Barra(73, 51, seccion_chica)) #255
ret.agregar_barra(Barra(74, 52, seccion_chica)) #256
ret.agregar_barra(Barra(75, 53, seccion_chica)) #257
ret.agregar_barra(Barra(76, 54, seccion_chica)) #258
ret.agregar_barra(Barra(77, 55, seccion_chica)) #259
# ret.agregar_barra(Barra(78, 56, seccion_chica_3)) #260
# ret.agregar_barra(Barra(79, 57, seccion_chica_3)) #261
# ret.agregar_barra(Barra(80, 58, seccion_chica_3)) #262
ret.agregar_barra(Barra(81, 59, seccion_chica_3)) #263
ret.agregar_barra(Barra(82, 60, seccion_chica_3)) #264
ret.agregar_barra(Barra(83, 61, seccion_chica_3)) #265
ret.agregar_barra(Barra(79, 55, seccion_chica_3)) #266
ret.agregar_barra(Barra(80, 56, seccion_chica_3)) #267
ret.agregar_barra(Barra(81, 57, seccion_chica_3)) #268
# ret.agregar_barra(Barra(82, 58, seccion_chica_3)) #269
# ret.agregar_barra(Barra(83, 59, seccion_chica_3)) #270
# ret.agregar_barra(Barra(84, 60, seccion_chica_3)) #271
ret.agregar_barra(Barra(85, 61, seccion_chica)) #272
ret.agregar_barra(Barra(86, 62, seccion_chica)) #273
ret.agregar_barra(Barra(87, 63, seccion_chica)) #274
ret.agregar_barra(Barra(88, 64, seccion_chica)) #275
ret.agregar_barra(Barra(89, 65, seccion_chica)) #276
ret.agregar_barra(Barra(90, 66, seccion_chica)) #277
ret.agregar_barra(Barra(91, 67, seccion_extra)) #278

#Crear restricciones
for nodo in [0, 1, 21, 22, 46, 47, 67, 68]:
	ret.agregar_restriccion(nodo, 0, 0)
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
total = ret.Nnodos
for i in range(ret.Nnodos):
    ret.agregar_fuerza(i, 2, -F/total)

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
	"ver_dato_en_barras" : False,
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
	"ver_dato_en_barras" : False,
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
	"ver_dato_en_barras" : False,
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
	"ver_dato_en_barras" : False,
	"dato":factores_de_utilizacion
}


ver_reticulado_3d(ret, 
	opciones_nodos=opciones_nodos, 
	opciones_barras=opciones_barras,
	titulo="Factor Utilizacion")


ret.guardar("GRUPO_10_FINAL.h5")

print(f"DESPLAZAMIENTOS: {ret.u}")
print(f"\nFACTOR DE UTILIZACIÓN: {factores_de_utilizacion}")