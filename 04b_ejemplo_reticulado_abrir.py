from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from constantes import *
from math import sqrt
from secciones import SeccionICHA

#Inicializar modelo
ret = Reticulado()

ret.abrir("04a_ejemplo_reticulado_guardar.h5")

#Visualizar y comprobar las secciones
opciones_barras = {
	"ver_secciones_en_barras": True,
	"color_barras_por_seccion": True,
}
ver_reticulado_3d(ret,opciones_barras=opciones_barras)

