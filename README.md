# MCOC2021-P1
Optimización estructural de un puente reticular

# Entrega 7 - Diseño Puente

*¿Cual fue su diseño inicial? 

El diseño inicial fue realizado tras consultar a un profesional, el cual nos aconsejo en la forma y distribución de diagonales y perfiles en general en todo el puente. Con eso llegamos a que el puente debía optmizar la repartición de cargas lo mejor posible, y para eso se debía ntentar conseguir secciones de reticulado cuadradas, dentro de lo posible.

El diseño resultante es el siguiente:



Usando 3 tipos de secciones en su estructura:

- seccion_grande = SeccionICHA("[]350x150x37.8", color="#3A8431")             [Verde]
- seccion_chica = SeccionICHA("[]350x150x37.8", color="#A3500B")              [Naranja]
- seccion_extra = SeccionICHA("H1100x350x400.4", color="pink")                [Rosado]


Su peso fue de : 

*¿Como eran los factores de utilización y las deformaciones?




*Cambios y Ajustes al diseño:

1° Se buscaron secciones que generaran la resistencia del puente correctamente al peso vivo predeterminado para el diseño. 
2° Una vez conseguido el soporte de las cargas distribuidas en el puente diseñado con 3 tipos de secciones, se fue buscando secciones para el mismo diseño pero con menor pesos propios, consiguiendo un puente que cumpliera con las solicitaciones de cargas, y se optimizara el uso de acero.

El Diseño final es el siguiente:



el cual esta compuesto por las secciones:

- seccion_grande = SeccionICHA("O310x300x5", color="#3A8431")#, debug=True) #O310x300x5     [Verde]
- seccion_chica = SeccionICHA("[]300x100x18.3", color="#A3500B")   #300x100x18.3            [Naranja]
- seccion_extra = SeccionICHA("H400x150x47.6", color="pink")     #H400x150x47.6             [Rosado]



Con un peso final de :





