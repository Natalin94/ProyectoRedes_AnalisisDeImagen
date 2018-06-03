import numpy as np
import cv2

# Cargamos la imagen
original=cv2.imread("a3.jpg")
#cv2.imshow("original", original)

# Convertimos a escala de grises
gris=cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

# Aplicar suavizado Gaussiano
gauss=cv2.GaussianBlur(gris, (5, 5), 0)

#cv2.imshow("suavizado", gauss)

# Detectamos los bordes con Canny
canny=cv2.Canny(gauss, 50, 150)

#Quitar comentario para ver imagen y contornos
cv2.imshow("canny", canny)

# Buscamos los contornos
(_, contornos, _)=cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
total=""
totalCir=0

for c in contornos:
    # approximate the contour
    shape="indefinido"
    peri=cv2.arcLength(c, True)
    approx=cv2.approxPolyDP(c, 0.04 * peri, True)

    if len(approx) == 3:
        shape="triangle"

    elif len(approx) == 4:
        (x, y, w, h)=cv2.boundingRect(approx)
        ar=w / float(h)

        shape="square" if ar >= 0.95 and ar <= 1.05 else "rectangle"

    elif len(approx) == 5:
        shape="pentagon"

    else:
        shape="circle"

    print(shape)

print("He encontrado {} objetos".format(len(contornos)))
# print "I found {0} books in that image".format(total)
# print "I found {0} books in that image".format(totalCir)

# cv2.rectangle(original,(384,0),(510,128),(0,255,0),3)
cv2.drawContours(original, contornos, -1, (0, 0, 255), 2)
#cv2.imshow("contornos", original)

cv2.waitKey(0)
