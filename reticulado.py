import numpy as np
from scipy.linalg import solve
import scipy.linalg as lin

class Reticulado(object):
    """Define un reticulado"""
    __NNodosInit__ = 100

    #constructor
    def __init__(self): 
        super(Reticulado, self).__init__()
        
        #print("Constructor de Reticulado")
        
        self.xyz = np.zeros((Reticulado.__NNodosInit__,3), dtype=np.double)
        self.Nnodos = 0
        self.barras = []
        self.cargas = {}
        self.restricciones = {}
        """Implementar"""	
        
        

    def agregar_nodo(self, x, y, z=0):

        #print(f"Quiero agregar un nodo en ({x} {y} {z})")
        numero_de_nodo_actual = self.Nnodos

        self.xyz[numero_de_nodo_actual,:] = [x, y, z]

        self.Nnodos += 1

        return 0

    def agregar_barra(self, barra):

        self.barras.append(barra)	

        return 0

    def obtener_coordenada_nodal(self, n):

        if n>= self.Nnodos:
            return
        return self.xyz[n, :]
    	
    def calcular_peso_total(self):
        peso=0
        for b in self.barras:
            peso+=b.calcular_peso(self)	 
        return peso

    def obtener_nodos(self):
        
        return self.xyz

      
    def obtener_barras(self):	
        
        return self.barras



    def agregar_restriccion(self, nodo, gdl, valor=0.0):
        #agrego restricción y consulto en el nodo
        
        if nodo in self.restricciones: 
        
            self.restricciones[nodo]

        else:
            self.restricciones[nodo]=(gdl, valor)
        
        return 0

    def agregar_fuerza(self, nodo, gdl, valor):
        if nodo in self.cargas:

            self.cargas[nodo]
        
        else:
            self.cargas[nodo]=(gdl, valor)	
        
        return 0



    def ensamblar_sistema(self, factor_peso_propio=0):
        #Ensambar riguidez y vector de cargas
        n=self.Nnodos*3 + 2
        self.k= np.zeros((n,n))
        self.υ=np.zeros(n)
        self.f=np.zeros(n)
        
        for e in self.barras: #aquí recorremos todas las barras
        #ni, nj nodos i y j consultamos a las barras
            ni= e.ni
            nj= e.nj
            k_e=e.obtener_rigidez(self)
            fe=e.obtener_vector_de_cargas(self)
            d= [3*ni, 3*ni+1, 3*ni+2, 3*nj, 3*nj+1, 3*nj+2]	

        #Método de riguidez directa
        for i in range(6):
            p=d[i]
            for j in range(6):
                q= d[j]
                k[p,q]+=k_e[i,j]
            f[p]+=f_e[i]

        #Agregamos cargas puntuales

        for node in cargas:
            print(node)
            Ncargas= len(cargas[node])
            print(Ncargas)
       
        return 0

    def resolver_sistema(self):
        #Cómo particionamos una matriz?
        
        km1=lin.inv(k)

        #F DEBE SER DEL TAMAÑO DE LOS GRADOS DE LIBERTAD DEL SISTEMA
        F=np.zeros(5)
        F[1]=f
        #ARMAMOS GDL FIJOS SEGÚN DICCIONARIOS DE RESTRICCIONES
        #LUEGO, USANDO np.setdiff1d  obtenemos los gld_libres
        gdl_libres=[]
        gdl_fijos=[]

        kff= k[np.ix_(gdl_libres, gdl_libres)]
        kcc= k[np.ix_(gdl_fijos, gdl_fijos)]
        kff= k[np.ix_(gdl_fijos, gdl_libres)]
        kff= k[np.ix_(gdl_libres, gdl_fijos)]
        print(f"k={k}")
        print(f"kff={kff}")
        print(f"kcc={kcc}")
        print(f"kcf={kcf}")
        print(f"kfc={kfc}")

        #U DEBE SER DEL TAMAÑO DE LOS GRADOS DE LIBERTAD DEL SISTEMA (MODIFICAR EL 5)
        # Si es que hay restricciones distintas de 0, se deben agregar en u

        u=np.zeros(5)
        uc=u[gld_fijos]
        Ff=F[gdl_libres]- Kfc @ uc

        u[gdl_libres]= lin.solve(kff,Ff)
        R= Kcf @  u[gdl_libres] + Kcc @ uc - F[gdl_fijos]
        
        print(f"u={u}")
        print(f"R={R}")
        self.kff
        self.Fc
        self.Kcc
        self.Kff
        self.Kfc
        self.kcf
        self.u
        self.uf
        self.uc
        self.R













        """Implementar"""

        
        return 0

    def obtener_desplazamiento_nodal(self, n):
        """Implementar"""	
        
        return 0


    def obtener_fuerzas(self):
        """Implementar"""	
        
        return 0


    def obtener_factores_de_utilizacion(self, f):
        """Implementar"""	
        
        return 0

    def rediseñar(self, Fu, ϕ=0.9):
        """Implementar"""	
        
        return 0



    def chequear_diseño(self, Fu, ϕ=0.9):
        """Implementar"""	
        
        return 0


    def __str__(self):

        s = "nodos: \n"

        for i in range(len(self.xyz[0: self.Nnodos,:])):
            s += "  " + str(i) + ": " + "(" + str(self.xyz[i,0]) + ", " + str(self.xyz[i,1]) + ", " + str(self.xyz[i,2]) + ")"
            s+= "\n"
        #parte en 0 y llega hasta Nnodos tomando todos los valores que estan ahí (:)

        s += "\n"
        s += "\n"

        s+= "barras: \n"

        for i in range(len(self.barras)):
            s += "  " + str(i) + ": " + "[ " + str(self.barras[i].ni) + " " + str(self.barras[i].nj) + " ]"
            s += "\n"

        return s
