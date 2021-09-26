import numpy as np
from constantes import g_, ρ_acero, E_acero


class Barra(object):

    """Constructor para una barra"""
    def __init__(self, ni, nj, seccion, color=np.random.rand(3)):
        super(Barra, self).__init__()
        self.ni = ni
        self.nj = nj
        self.seccion = seccion
        self.color = color


    def obtener_conectividad(self):
        return [self.ni, self.nj]

    def calcular_largo(self, reticulado):
        """Devuelve el largo de la barra. 
        xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
        xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
        """
       
        ni = self.ni
        nj = self.nj

        xi = reticulado.xyz[ni,:]
        xj = reticulado.xyz[nj,:]

        #print(f"Barra {ni} a {nj} xi = {xi} xj = {xj}")

        return np.linalg.norm(xj - xi)

    def calcular_area(self):
        return self.seccion.area()

    def calcular_peso(self, reticulado):
        return ((self.calcular_area())*(self.calcular_largo(reticulado))*(ρ_acero)*(g_))


    def obtener_rigidez(self, reticulado):

        L= self.calcular_largo(reticulado)
        ni=reticulado.obtener_coordenada_nodal(self.ni)
        nj=reticulado.obtener_coordenada_nodal(self.nj)
        Lx=(nj[0]-ni[0])
        Ly=(nj[1]-ni[1])
        Lz=(nj[2]-ni[2])
    
        cosθx=Lx/L
        cosθy=Ly/L
        cosθz=Lz/L
        T= np.array([[-cosθx], [-cosθy], [-cosθz], [cosθx], [cosθy], [cosθz]])
        ke=(self.seccion.area()*E_acero/L) * T * T.T
        return ke

    def obtener_vector_de_cargas(self, reticulado):
        W = self.calcular_peso(reticulado)
        return W/2 *np.array(reticulado.factor_modificado)
        #Si borro 1 de los ceros en cada trio, obtengo formato 2d

    def obtener_fuerza(self, reticulado):
        u_e = np.zeros(2*3)
        u_e[0:3] = reticulado.obtener_desplazamiento_nodal(self.ni)
        u_e[3:] = reticulado.obtener_desplazamiento_nodal(self.nj)
        L= self.calcular_largo(reticulado)
        ni=reticulado.obtener_coordenada_nodal(self.ni)
        nj=reticulado.obtener_coordenada_nodal(self.nj)
        Lx=(nj[0]-ni[0])
        Ly=(nj[1]-ni[1])
        Lz=(nj[2]-ni[2])
    
        cosθx=Lx/L
        cosθy=Ly/L
        cosθz=Lz/L
        T= np.array([-cosθx, -cosθy, -cosθz, cosθx, cosθy, cosθz])	
        
        se=self.calcular_area()*E_acero/L * T @ u_e
        return se


    def chequear_diseño(self, Fu, ret, ϕ=0.9):
<<<<<<< HEAD
        """Implementar"""	
        
        return 0

    def obtener_factor_utilizacion(self, Fu, ϕ=0.9):
        """Implementar"""	
=======
        
        area = self.seccion.area()
        peso = self.seccion.peso()
        inercia_xx = self.seccion.inercia_xx()
        inercia_yy = self.seccion.inercia_yy()
        nombre = self.seccion.nombre()
        
        #Resistencia nominal
        Fn = area * σy_acero

        #Revisar resistencia nominal
        if abs(Fu) > ϕ*Fn:
            print(f"Resistencia nominal Fu = {Fu} ϕ*Fn = {ϕ*Fn}")
            return False

        L = self.calcular_largo(ret)

        #Inercia es la minima
        I = min(inercia_xx, inercia_yy)
        i = np.sqrt(I/area)

        #Revisar radio de giro
        if Fu >= 0 and L/i > 300:
            print(f"Esbeltez Fu = {Fu} L/i = {L/i}")
            return False

        #Revisar carga critica de pandeo
        if Fu < 0:  #solo en traccion
            Pcr = np.pi**2*E_acero*I / L**2
            if abs(Fu) > Pcr:
                print(f"Pandeo Fu = {Fu} Pcr = {Pcr}")
                return False
        
        #Si pasa todas las pruebas, estamos bien
        return True
>>>>>>> cd8f38c631faf147be0d7e80fcbfed097661e03f
        


<<<<<<< HEAD
    def rediseñar(self, Fu, ret, ϕ=0.9):
        """Implementar"""	
        




    def obtener_factor_utilizacion(self, Fu, ϕ=0.9):
        A = self.seccion.area()
        Fn = A * σy_acero

=======
    def chequear_diseño(self, Fu, ret, ϕ=0.9):
        
        area = self.seccion.area()
        peso = self.seccion.peso()
        inercia_xx = self.seccion.inercia_xx()
        inercia_yy = self.seccion.inercia_yy()
        nombre = self.seccion.nombre()
        
        #Resistencia nominal
        Fn = area * σy_acero

        #Revisar resistencia nominal
        if abs(Fu) > ϕ*Fn:
            print(f"Resistencia nominal Fu = {Fu} ϕ*Fn = {ϕ*Fn}")
            return False

        L = self.calcular_largo(ret)

        #Inercia es la minima
        I = min(inercia_xx, inercia_yy)
        i = np.sqrt(I/area)

        #Revisar radio de giro
        if Fu >= 0 and L/i > 300:
            print(f"Esbeltez Fu = {Fu} L/i = {L/i}")
            return False

        #Revisar carga critica de pandeo
        if Fu < 0:  #solo en traccion
            Pcr = np.pi**2*E_acero*I / L**2
            if abs(Fu) > Pcr:
                print(f"Pandeo Fu = {Fu} Pcr = {Pcr}")
                return False
        
        #Si pasa todas las pruebas, estamos bien
        return True
        


    def rediseñar(self, Fu, ret, ϕ=0.9):
        
        """Implementar"""	
        




    def obtener_factor_utilizacion(self, Fu, ϕ=0.9):
        A = self.seccion.area()
        Fn = A * σy_acero

>>>>>>> cd8f38c631faf147be0d7e80fcbfed097661e03f
        return abs(Fu) / (ϕ*Fn)


