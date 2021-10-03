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

###Desplazamientos:  

     [0.00000000e+00  0.00000000e+00  0.00000000e+00  0.00000000e+00
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
     -2.44526637e-03 -4.77675691e-03 -4.02487016e-01  4.49692883e-03]
     
 ###Factor de Utilización:

     [0.00000000e+00 1.24728227e-01 9.69331652e-01 6.51334521e-01
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
     4.26168916e-01 3.90682231e-01 1.10341841e-01]
     
![fu](https://github.com/RobertoVergaraC/MCOC2021-P1/blob/main/FOTOS/PRIMERO/Factor%20Utilizaci%C3%B3n.jpg)


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

Obteniendo deformaciones y factores de utilización de:

     DESPLAZAMIENTOS: [ 0.00000000e+00  0.00000000e+00  0.00000000e+00  0.00000000e+00
       0.00000000e+00  0.00000000e+00 -5.98534463e-03 -8.74324537e-03
      -4.52713325e-02 -1.14009477e-02  3.86758856e-04 -9.80331838e-02
      -1.45519357e-02 -4.87371846e-03 -1.53936543e-01 -1.60498531e-02
       2.40155387e-03 -2.09494954e-01 -1.57851744e-02 -1.75457724e-03
      -2.61363444e-01 -1.43694442e-02  3.66556338e-03 -3.07059595e-01
      -1.16931370e-02  6.13378641e-04 -3.44242471e-01 -8.36779723e-03
       4.17798773e-03 -3.71433693e-01 -4.01468272e-03  2.63317467e-03
      -3.85194212e-01  3.46951655e-04  3.73030933e-03 -3.87964034e-01
       4.82805878e-03  3.17343677e-03 -3.79806865e-01  8.84197815e-03
       2.56900683e-03 -3.61056670e-01  1.24687345e-02  3.07070116e-03
      -3.32590098e-01  1.51720718e-02  7.22560457e-04 -2.95382499e-01
       1.62757847e-02  1.14811131e-03 -2.45935443e-01  1.57694446e-02
      -2.15539857e-03 -1.91119917e-01  1.37625768e-02 -6.27812593e-04
      -1.33975713e-01  9.64363687e-03 -5.78876526e-03 -7.76841050e-02
       3.52215034e-03 -3.15954398e-03 -2.62889221e-02  0.00000000e+00
       0.00000000e+00  0.00000000e+00  0.00000000e+00  0.00000000e+00
       0.00000000e+00  1.84222370e-02  1.15342458e-01  4.73865389e-03
       2.32601142e-02  2.19552616e-02 -2.46090981e-03  2.70440028e-02
       1.13764777e-01 -4.74812328e-02  2.87434958e-02  1.88327480e-02
      -9.99920746e-02  2.86096028e-02  1.11019467e-01 -1.55644425e-01
       2.68933333e-02  1.64645540e-02 -2.10951826e-01  2.38456968e-02
       1.09028301e-01 -2.62569307e-01  1.97177028e-02  1.48503279e-02
      -3.08014447e-01  1.47603608e-02  1.07790927e-01 -3.44946314e-01
       9.22468030e-03  1.39897182e-02 -3.71617310e-01  3.63088763e-03
       1.07710819e-01 -3.84996096e-01 -2.17771812e-03  1.36746555e-02
      -3.87790468e-01 -7.94870003e-03  1.07774436e-01 -3.79631539e-01
      -1.34061646e-02  1.41520665e-02 -3.60884199e-01 -1.83286031e-02
       1.08583992e-01 -3.32374695e-01 -2.23897174e-02  1.54508797e-02
      -2.95834607e-01 -2.61242289e-02  1.09080464e-01 -2.47239676e-01
      -2.86800123e-02  1.72251744e-02 -1.92675160e-01 -2.98060581e-02
       1.11230820e-01 -1.35781965e-01 -2.92513568e-02  1.97515038e-02
      -7.97413664e-02 -2.67648988e-02  1.14133035e-01 -2.85971930e-02
      -2.40550818e-02  1.83838613e-02 -2.55928043e-03 -1.54212632e-02
       1.30162849e-01  4.15844760e-03  0.00000000e+00  0.00000000e+00
       0.00000000e+00  0.00000000e+00  0.00000000e+00  0.00000000e+00
      -5.98582457e-03  8.74409019e-03 -4.52705122e-02 -1.14019681e-02
      -3.83538651e-04 -9.80318245e-02 -1.45534298e-02  4.88083539e-03
      -1.53934889e-01 -1.60517544e-02 -2.38921879e-03 -2.09493212e-01
      -1.57874162e-02  1.77325199e-03 -2.61361783e-01 -1.43719599e-02
      -3.63962737e-03 -3.07058146e-01 -1.16958599e-02 -5.79459675e-04
      -3.44241330e-01 -8.37066081e-03 -4.13556403e-03 -3.71432916e-01
      -4.01762777e-03 -2.58191313e-03 -3.85193878e-01  3.43986455e-04
      -3.67005751e-03 -3.87964175e-01  4.82513462e-03 -3.22161179e-03
      -3.79807475e-01  8.83915621e-03 -2.60843780e-03 -3.61057704e-01
       1.24660760e-02 -3.10178661e-03 -3.32591473e-01  1.51696373e-02
      -7.45881466e-04 -2.95384104e-01  1.62736467e-02 -1.16444861e-03
      -2.45937215e-01  1.57676698e-02  2.14505533e-03 -1.91121711e-01
       1.37612318e-02  6.22273850e-04 -1.33977346e-01  9.64278840e-03
       5.78664154e-03 -7.76853574e-02  3.52186499e-03  3.15924589e-03
      -2.62895358e-02  0.00000000e+00  0.00000000e+00  0.00000000e+00
       0.00000000e+00  0.00000000e+00  0.00000000e+00  1.84213641e-02
       1.46971365e-02  4.73842589e-03  2.32590133e-02  1.08087293e-01
      -2.46088052e-03  2.70426428e-02  1.62814686e-02 -4.74803832e-02
       2.87419061e-02  1.11217922e-01 -9.99906860e-02  2.86078126e-02
       1.90362729e-02 -1.55642741e-01  2.68913719e-02  1.13596814e-01
      -2.10950054e-01  2.38435934e-02  2.10391638e-02 -2.62567616e-01
       1.97154868e-02  1.15223616e-01 -3.08012969e-01  1.47580614e-02
       2.22897899e-02 -3.44945144e-01  9.22232692e-03  1.16097978e-01
      -3.71616511e-01  3.62850200e-03  2.23839856e-02 -3.84995754e-01
      -2.18011203e-03  1.16427318e-01 -3.87790612e-01 -7.95107838e-03
       2.23346958e-02 -3.79632161e-01 -1.34085035e-02  1.15964142e-01
      -3.60885257e-01 -1.83308787e-02  2.15391377e-02 -3.32376106e-01
      -2.23919066e-02  1.14678948e-01 -2.95836247e-01 -2.61262964e-02
       2.10557483e-02 -2.47241477e-01 -2.86819288e-02  1.12917014e-01
      -1.92676983e-01 -2.98077943e-02  1.89168474e-02 -1.35783628e-01
      -2.92528834e-02  1.10401058e-01 -7.97426481e-02 -2.67661865e-02
       1.60237484e-02 -2.85978360e-02 -2.40562139e-02  1.11775029e-01
      -2.55930973e-03 -1.54219905e-02 -0.00000000e+00  4.15864848e-03]

     FACTOR DE UTILIZACIÓN: [0.00000000e+00 8.67351843e-01 7.84919189e-01 4.56846105e-01
      2.17349793e-01 3.80699073e-02 2.04912836e-01 3.87679152e-01
      4.81868697e-01 6.31090967e-01 6.32474329e-01 6.49886639e-01
      5.82183248e-01 5.25982687e-01 3.92014902e-01 1.59928175e-01
      7.35297113e-02 2.91064211e-01 5.97175481e-01 8.87363364e-01
      8.79616916e-01 0.00000000e+00 7.01065833e-01 5.48456203e-01
      2.46500670e-01 1.91281706e-02 2.48430320e-01 4.41405777e-01
      5.98054542e-01 7.18376615e-01 8.02371997e-01 8.10879903e-01
      8.42168916e-01 8.36819894e-01 7.91387472e-01 7.13753277e-01
      5.88777060e-01 5.41362142e-01 3.70363476e-01 1.63038117e-01
      8.06139328e-02 3.60592675e-01 6.76898109e-01 8.81487868e-01
      6.86739624e-01 3.56485288e-01 3.20118879e-01 2.83792187e-01
      2.47465495e-01 2.11138803e-01 1.74812111e-01 1.38485419e-01
      1.02158727e-01 2.66712520e-02 2.87148703e-02 2.51501995e-02
      2.54477968e-02 2.49916915e-02 3.12202130e-02 6.55782640e-02
      1.89162012e-01 2.25488704e-01 2.61815396e-01 2.98142088e-01
      3.34413634e-01 3.70681566e-01 6.02751844e-01 6.86715623e-01
      3.56486528e-01 3.20120119e-01 2.83793427e-01 2.47466735e-01
      2.11140043e-01 1.74813352e-01 1.38486660e-01 1.02159968e-01
      2.66703673e-02 2.87137767e-02 2.51919799e-02 2.54038096e-02
      2.49907634e-02 3.12144151e-02 6.55810255e-02 1.89160772e-01
      2.25487464e-01 2.61814156e-01 2.98140848e-01 3.34412394e-01
      3.70680325e-01 6.02776646e-01 0.00000000e+00 8.67438607e-01
      7.85012715e-01 4.56923414e-01 2.17410883e-01 3.80250346e-02
      2.04884181e-01 3.87666715e-01 4.81872478e-01 6.31113091e-01
      6.32508568e-01 6.49894218e-01 5.82164154e-01 5.25975908e-01
      3.92023374e-01 1.59956868e-01 7.34848010e-02 2.91003083e-01
      5.97098135e-01 8.87269800e-01 8.79533019e-01 0.00000000e+00
      7.01041832e-01 5.48424604e-01 2.46467831e-01 1.91622502e-02
      2.48465640e-01 4.41442337e-01 5.98092343e-01 7.18415656e-01
      8.02412278e-01 8.10919300e-01 8.42213656e-01 8.36818897e-01
      7.91340752e-01 7.13711701e-01 5.88737690e-01 5.41320011e-01
      3.70322585e-01 1.62998467e-01 8.06523432e-02 3.60629845e-01
      6.76934039e-01 8.81523078e-01 0.00000000e+00 0.00000000e+00
      1.56946948e-02 1.57036952e-02 1.56946948e-02 1.57036952e-02
      1.56946948e-02 1.57036952e-02 1.56946948e-02 1.57036952e-02
      1.57036952e-02 1.56946948e-02 1.56946948e-02 1.57036952e-02
      1.57036952e-02 1.56946948e-02 1.56946948e-02 1.57036952e-02
      1.57036952e-02 1.56946948e-02 1.56946948e-02 1.57036952e-02
      7.85184761e-03 1.56946948e-02 7.85184761e-03 1.56946948e-02
      1.57036952e-02 1.57036952e-02 1.56946948e-02 1.56946948e-02
      1.57036952e-02 1.57036952e-02 1.56946948e-02 1.56946948e-02
      1.57036952e-02 1.57036952e-02 1.56946948e-02 1.56946948e-02
      1.57036952e-02 1.57036952e-02 1.56946948e-02 1.15425001e-02
      1.15491194e-02 0.00000000e+00 0.00000000e+00 6.16521888e-15
      4.88762643e-15 1.70557797e-15 5.75851331e-15 6.07850806e-15
      3.29660220e-15 6.63138898e-15 6.08328113e-15 1.37305391e-15
      6.63138898e-15 5.85496916e-15 1.17894895e-15 1.17815344e-15
      4.11120660e-15 1.66739339e-15 1.78910674e-15 3.97437852e-15
      7.63691629e-17 5.85496916e-15 3.97915159e-15 4.62749396e-15
      4.18757577e-15 3.41115594e-15 4.41668325e-15 6.49694743e-15
      2.59655154e-15 7.44599338e-15 7.11028727e-15 6.84697276e-15
      5.74041541e-15 2.40562863e-15 6.65764088e-15 5.34265935e-15
      2.48199779e-15 3.29660220e-15 4.33394999e-15 3.91471511e-15
      7.63691629e-17 1.52738326e-16 3.90994204e-15 1.65497415e-15
      2.42296869e-15 3.23819263e-15 7.82116178e-16 9.91456810e-01
      9.82496704e-01 8.76939074e-01 7.71439118e-01 6.65939161e-01
      5.60439205e-01 4.54939249e-01 3.49439292e-01 2.43939336e-01
      2.47086557e-02 2.27117815e-02 7.07376042e-02 1.29374838e-01
      1.75472712e-01 2.53262481e-01 1.13581315e-01 5.52029771e-02
      2.56997478e-03 4.99924701e-02 1.09693370e-01 1.37702376e-01
      4.96614223e-01 6.02114179e-01 7.07614136e-01 8.13114092e-01
      9.18614048e-01 8.37019592e-01 8.52436852e-01 9.91422867e-01
      9.82500306e-01 8.76942676e-01 7.71442720e-01 6.65942764e-01
      5.60442807e-01 4.54942851e-01 3.49442894e-01 2.43942938e-01
      2.47060864e-02 2.27024341e-02 7.08646880e-02 1.29377359e-01
      1.75463894e-01 2.53250859e-01 1.13587486e-01 5.51972318e-02
      2.70024335e-03 4.99863469e-02 1.09698587e-01 1.37710396e-01
      4.96610621e-01 6.02110577e-01 7.07610534e-01 8.13110490e-01
      9.18610446e-01 8.37016647e-01 8.52470902e-01]
  
 
![fu](https://github.com/RobertoVergaraC/MCOC2021-P1/blob/main/FOTOS/%C3%9ALTIMO/Factor%20de%20Utilizaci%C3%B3n.jpg)



