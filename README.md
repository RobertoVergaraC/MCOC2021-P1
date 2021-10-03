# MCOC2021-P1
Optimización estructural de un puente reticular

# Entrega 7 - Diseño Puente

*¿Cual fue su diseño inicial? 

El diseño inicial fue realizado tras consultar a un profesional, el cual nos aconsejo en la forma y distribución de diagonales y perfiles en general en todo el puente. Con eso llegamos a que el puente debía optmizar la repartición de cargas lo mejor posible, y para eso se debía ntentar conseguir secciones de reticulado cuadradas, dentro de lo posible.

El diseño resultante es el siguiente:
| VISTA | GRÁFICO |
| ------------- | ------------- |
| GENERAL | ![general](https://github.com/RobertoVergaraC/MCOC2021-P1/blob/main/FOTOS/DISE%C3%91O%20PUENTE%20GENERAL.jpg) |
| HORIZONTAL | ![horizontal](https://github.com/RobertoVergaraC/MCOC2021-P1/blob/main/FOTOS/DISE%C3%91O%20PUENTE%20DE%20LADO.jpg) |
| VERTICAL | ![altura](https://github.com/RobertoVergaraC/MCOC2021-P1/blob/main/FOTOS/DISE%C3%91O%20PUENTE%20DESDE%20ARRIBA.jpg) |



Usando 3 tipos de secciones en su estructura:

- seccion_grande = SeccionICHA("[]350x150x37.8", color="#3A8431")             [Verde]
- seccion_chica = SeccionICHA("[]350x150x37.8", color="#A3500B")              [Naranja]
- seccion_extra = SeccionICHA("H1100x350x400.4", color="pink")                [Rosado]


Su peso fue de : 

![PESO PRIMERO](https://github.com/RobertoVergaraC/MCOC2021-P1/blob/main/FOTOS/PRIMERO/PESO%20FINAL.jpg)

*¿Como eran los factores de utilización y las deformaciones?

    ( 0.00000000e+00  0.00000000e+00  0.00000000e+00  0.00000000e+00
      0.00000000e+00  0.00000000e+00 -8.56604595e-04 -1.27190710e-03
     -1.41734838e-02 -7.51550792e-03 -8.72941748e-03 -4.02152840e-02
     -1.19882079e-02  2.03351834e-03 -7.37629711e-02 -1.45444765e-02
     -5.88053468e-03 -1.10973698e-01 -1.54141622e-02  4.58969142e-03
     -1.48484276e-01 -1.48670372e-02 -3.78093099e-03 -1.83451100e-01
     -1.31329497e-02  6.39655865e-03 -2.13510222e-01 -1.04816720e-02
     -2.43065987e-03 -2.36817276e-01 -6.84814337e-03  7.89643009e-03
     -2.50583610e-01 -2.96472438e-03 -2.08129313e-03 -2.55902765e-01
      9.84746330e-04  8.01552456e-03 -2.52649709e-01  4.72881306e-03
     -2.41486931e-03 -2.40940680e-01  8.02783854e-03  7.37445505e-03
     -2.21458399e-01  1.06883012e-02 -3.39823127e-03 -1.94997846e-01
      1.17737638e-02  5.03837719e-03 -1.60313955e-01  1.15281245e-02
     -5.42049903e-03 -1.22019584e-01  9.72153469e-03  2.72324738e-03
     -8.27669508e-02  6.08422239e-03 -8.19235054e-03 -4.56879342e-02
      3.86339083e-04 -3.41492927e-04 -1.44339948e-02  0.00000000e+00
      0.00000000e+00  0.00000000e+00  0.00000000e+00  0.00000000e+00
      0.00000000e+00  3.09306947e-03  1.96258964e-01  7.99211277e-04
      3.90407081e-03 -3.76902433e-01 -2.55094145e-03  1.00698642e-02
      2.04291192e-01 -1.64746150e-02  1.40594316e-02 -3.80166656e-01
     -4.22666049e-02  1.61225832e-02  2.01401753e-01 -7.55644818e-02
      1.65091292e-02 -3.82681318e-01 -1.12525398e-01  1.54688799e-02
      1.99261860e-01 -1.49786167e-01  1.32516455e-02 -3.84446451e-01
     -1.84503180e-01  1.01072364e-02  1.97871479e-01 -2.14312491e-01
      6.28546277e-03 -3.85462088e-01 -2.37074826e-01  2.33104388e-03
      1.97672941e-01 -2.50464120e-01 -1.96879847e-03 -3.85979779e-01
     -2.55822814e-01 -6.31824416e-03  1.97598987e-01 -2.52564971e-01
     -1.04691666e-02 -3.85681543e-01 -2.40862627e-01 -1.41815444e-02
      1.98257251e-01 -2.21320570e-01 -1.71293168e-02 -3.84534199e-01
     -1.95430578e-01 -1.97692622e-02  1.98719410e-01 -1.61510168e-01
     -2.13379004e-02 -3.82926848e-01 -1.23465607e-01 -2.15854210e-02
      2.00701440e-01 -8.44627837e-02 -2.02620138e-02 -3.80570147e-01
     -4.76335774e-02 -1.71178687e-02  2.03432805e-01 -1.66294482e-02
     -1.40914847e-02 -3.82651634e-01 -2.44526368e-03 -4.77673886e-03
      2.20633809e-01  4.49691168e-03  0.00000000e+00  0.00000000e+00
      0.00000000e+00  0.00000000e+00  0.00000000e+00  0.00000000e+00
     -8.56608453e-04  1.27192220e-03 -1.41734644e-02 -7.51554819e-03
      8.72950809e-03 -4.02152558e-02 -1.19882801e-02 -2.03324965e-03
     -7.37629430e-02 -1.45445762e-02  5.88107065e-03 -1.10973677e-01
     -1.54142850e-02 -4.58881233e-03 -1.48484268e-01 -1.48671785e-02
      3.78221565e-03 -1.83451108e-01 -1.31331053e-02 -6.39481932e-03
     -2.13510248e-01 -1.04818372e-02  2.43288960e-03 -2.36817320e-01
     -6.84831408e-03 -7.89368719e-03 -2.50583672e-01 -2.96489678e-03
      2.08456000e-03 -2.55902845e-01  9.84576080e-04 -8.01823430e-03
     -2.52649806e-01  4.72864880e-03  2.41267065e-03 -2.40940789e-01
      8.02768413e-03 -7.37616640e-03 -2.21458517e-01  1.06881603e-02
      3.39697214e-03 -1.94997965e-01  1.17736418e-02 -5.03923262e-03
     -1.60314075e-01  1.15280257e-02  5.41998415e-03 -1.22019697e-01
      9.72146363e-03 -2.72349819e-03 -8.27670494e-02  6.08418352e-03
      8.19227393e-03 -4.56880076e-02  3.86336852e-04  3.41487280e-04
     -1.44340309e-02  0.00000000e+00  0.00000000e+00  0.00000000e+00
      0.00000000e+00  0.00000000e+00  0.00000000e+00  3.09305919e-03
     -3.78118951e-01  7.99208591e-04  3.90405784e-03  1.95042482e-01
     -2.55093875e-03  1.00698255e-02 -3.86151065e-01 -1.64745929e-02
      1.40593698e-02  1.98306933e-01 -4.22665740e-02  1.61225010e-02
     -3.83261260e-01 -7.55644510e-02  1.65090293e-02  2.00822084e-01
     -1.12525375e-01  1.54687651e-02 -3.81120772e-01 -1.49786156e-01
      1.32515185e-02  2.02587902e-01 -1.84503185e-01  1.01070998e-02
     -3.79729633e-01 -2.14312515e-01  6.28531927e-03  2.03604354e-01
     -2.37074868e-01  2.33089591e-03 -3.79530238e-01 -2.50464181e-01
     -1.96894885e-03  2.04122930e-01 -2.55822894e-01 -6.31839486e-03
     -3.79455385e-01 -2.52565069e-01 -1.04693156e-02  2.03825595e-01
     -2.40862738e-01 -1.41816895e-02 -3.80112758e-01 -2.21320691e-01
     -1.71294561e-02  2.02679119e-01 -1.95430701e-01 -1.97693922e-02
     -3.80574086e-01 -1.61510290e-01 -2.13380184e-02  2.01072544e-01
     -1.23465723e-01 -2.15855243e-02 -3.82555412e-01 -8.44628850e-02
     -2.02620998e-02  1.98716458e-01 -4.76336535e-02 -1.71179345e-02
     -3.85286266e-01 -1.66294870e-02 -1.40915374e-02  2.00798276e-01
     -2.44526637e-03 -4.77675691e-03 -4.02487016e-01  4.49692883e-03)

| DEFORMACIONES | FACTORES DE UTILIZACIÓN |
| ------------- | ------------- |
|  | (0.00000000e+00 1.24728227e-01 9.69331652e-01 6.51334521e-01
 3.72532770e-01 1.27068259e-01 7.92008717e-02 2.52132763e-01
 3.85869274e-01 5.29369896e-01 5.65991552e-01 5.75768164e-01
 5.45854245e-01 4.80921994e-01 3.87694944e-01 1.57920011e-01
 3.60992363e-02 2.63455722e-01 5.30007589e-01 8.29896696e-01
 9.69559063e-02 0.00000000e+00 1.18092440e-01 8.97566059e-01
 5.81032599e-01 3.00765449e-01 5.67646093e-02 1.50969921e-01
 3.22438141e-01 4.57640051e-01 5.56575651e-01 5.76037832e-01
 6.26600017e-01 6.33980665e-01 6.05077247e-01 5.41075705e-01
 4.29484241e-01 3.84519839e-01 2.28232301e-01 3.56784538e-02
 1.93141704e-01 4.58228171e-01 7.59580949e-01 9.55686945e-01
 1.16165170e-01 3.72367629e-01 3.34666615e-01 2.98400305e-01
 2.62133995e-01 2.25867685e-01 1.89601375e-01 1.53335065e-01
 1.17068755e-01 3.75953365e-02 1.74016048e-02 1.16301864e-02
 1.23687200e-02 1.13540409e-02 2.00717579e-02 6.30975575e-02
 1.74420692e-01 2.10687002e-01 2.46953312e-01 2.83219622e-01
 3.19430773e-01 3.56023288e-01 6.53891164e-01 1.16166731e-01
 3.72373476e-01 3.34672462e-01 2.98406152e-01 2.62139842e-01
 2.25873532e-01 1.89607222e-01 1.53340912e-01 1.17074602e-01
 3.75973007e-02 1.73978129e-02 1.16702174e-02 1.23280170e-02
 1.13575234e-02 2.00699101e-02 6.30955730e-02 1.74414846e-01
 2.10681156e-01 2.46947466e-01 2.83213776e-01 3.19424926e-01
 3.56017441e-01 6.53885480e-01 0.00000000e+00 1.24731243e-01
 9.69356027e-01 6.51351321e-01 3.72541995e-01 1.27069909e-01
 7.92067965e-02 2.52146263e-01 3.85890348e-01 5.29402428e-01
 5.66025949e-01 5.75769792e-01 5.45823058e-01 4.80893081e-01
 3.87673577e-01 1.57910080e-01 3.61015913e-02 2.63450503e-01
 5.29994794e-01 8.29876326e-01 9.69535343e-02 0.00000000e+00
 1.18094001e-01 8.97576749e-01 5.81037442e-01 3.00764445e-01
 5.67577583e-02 1.50982619e-01 3.22456685e-01 4.57664442e-01
 5.56605889e-01 5.76070035e-01 6.26643776e-01 6.33980738e-01
 6.05033681e-01 5.41043286e-01 4.29457699e-01 3.84495281e-01
 2.28213590e-01 3.56655898e-02 1.93148721e-01 4.58229341e-01
 7.59576272e-01 9.55678875e-01 0.00000000e+00 0.00000000e+00
 8.79556923e-04 8.80595443e-04 8.79556923e-04 8.80595443e-04
 8.79556923e-04 8.80595443e-04 8.79556923e-04 8.80595443e-04
 8.80595443e-04 8.79556923e-04 8.79556923e-04 8.80595443e-04
 8.80595443e-04 8.79556923e-04 8.79556923e-04 8.80595443e-04
 8.80595443e-04 8.79556923e-04 8.79556923e-04 8.80595443e-04
 4.40297721e-04 8.79556923e-04 4.40297721e-04 8.79556923e-04
 8.80595443e-04 8.80595443e-04 8.79556923e-04 8.79556923e-04
 8.80595443e-04 8.80595443e-04 8.79556923e-04 8.79556923e-04
 8.80595443e-04 8.80595443e-04 8.79556923e-04 8.79556923e-04
 8.80595443e-04 8.80595443e-04 8.79556923e-04 6.46860995e-04
 6.47624763e-04 0.00000000e+00 0.00000000e+00 3.41115594e-15
 7.05141937e-15 1.37209929e-14 1.00807295e-14 1.72085180e-14
 8.75699735e-15 6.82231189e-15 2.07724123e-14 1.34918854e-14
 5.34584140e-15 6.89868105e-15 1.39501004e-14 7.63691629e-16
 6.74594272e-15 6.82231189e-15 6.97505021e-15 1.37973621e-14
 3.64026343e-15 0.00000000e+00 7.28052686e-15 1.39501004e-14
 1.40010132e-15 5.19310308e-15 1.39501004e-14 3.05476652e-16
 5.19310308e-15 0.00000000e+00 3.41115594e-15 6.66957356e-15
 3.25841762e-15 7.63691629e-17 6.82231189e-15 1.02334678e-14
 1.55283965e-15 1.40010132e-15 1.02334678e-14 6.82231189e-15
 1.47647048e-15 6.66957356e-15 6.66957356e-15 8.86114265e-15
 4.63825436e-15 3.74537942e-15 5.34496855e-15 1.67007930e-01
 4.99948709e-01 4.47645912e-01 3.96357605e-01 3.45069297e-01
 2.93780990e-01 2.42492682e-01 1.91204375e-01 1.39916067e-01
 2.75236810e-02 1.05512120e-02 1.59017358e-02 4.20806673e-02
 6.61813025e-02 1.05996816e-01 6.09545151e-02 2.63395490e-02
 1.20506182e-03 2.43305464e-02 5.18173462e-02 6.35892678e-02
 2.21023955e-01 2.72312262e-01 3.23600570e-01 3.74888877e-01
 4.26177185e-01 3.90688991e-01 1.10342773e-01 1.67010138e-01
 4.99956977e-01 4.47654181e-01 3.96365873e-01 3.45077566e-01
 2.93789258e-01 2.42500951e-01 1.91212643e-01 1.39924336e-01
 2.75264588e-02 1.05620655e-02 1.59609330e-02 4.20827434e-02
 6.61758829e-02 1.05991354e-01 6.09600059e-02 2.63369642e-02
 1.14542289e-03 2.43202017e-02 5.18144972e-02 6.35864613e-02
 2.21015686e-01 2.72303994e-01 3.23592301e-01 3.74880609e-01
 4.26168916e-01 3.90682231e-01 1.10341841e-01) |


*Cambios y Ajustes al diseño:

1° Se buscaron secciones que generaran la resistencia del puente correctamente al peso vivo predeterminado para el diseño. 
2° Una vez conseguido el soporte de las cargas distribuidas en el puente diseñado con 3 tipos de secciones, se fue buscando secciones para el mismo diseño pero con menor pesos propios, consiguiendo un puente que cumpliera con las solicitaciones de cargas, y se optimizara el uso de acero.

El Diseño final es el mismo inicial, pero con barras secciones diferentes;

el cual esta compuesto por las secciones:

- seccion_grande = SeccionICHA("O310x300x5", color="#3A8431")#, debug=True) #O310x300x5     [Verde]
- seccion_chica = SeccionICHA("[]300x100x18.3", color="#A3500B")   #300x100x18.3            [Naranja]
- seccion_extra = SeccionICHA("H400x150x47.6", color="pink")     #H400x150x47.6             [Rosado]



Con un peso final de :

![PESO PRIMERO](https://github.com/RobertoVergaraC/MCOC2021-P1/blob/main/FOTOS/%C3%9ALTIMO/PESO%20FINAL.jpg)




