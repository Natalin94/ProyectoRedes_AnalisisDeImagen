from ctypes.wintypes import RGB
import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image
# image = cv2.imread('foto2.png')
#
# x = 240
# y = 178
#
# b = image.item(y, x, 0)
# g = image.item(y, x, 1)
# r = image.item(y, x, 2)
#
# print('pixel:', b, g, r)


# importamos el modulo pyplot, y lo llamamos plt

import numpy
#configuracion necesaria de pyplot para ver las imagenes en escala de grises
plt.rcParams['foto2.png'] = 'gray'


#tambien importamos numpy ya que lo usamos para crear y manipular matrices


#tamaño de las matrices a visualizar
size=(20,30)

# Una matriz de ceros.
imagen_negra = np.zeros(size)

#visualizamos la matriz
#Se ve como una imagen negra, ya que todos los elementos (pixeles) tienen intensidad 0
plt.imshow(imagen_negra,vmin=0,vmax=1)
# (es necesario indicar vmin y vmax para que pyplot sepa que el minimo es 0 y el maximo 1)
# (solo imagenes escala de grises)