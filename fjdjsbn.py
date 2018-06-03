import sys, os, glob
from PIL import Image

cont = 0

### Configuracion
diri = "C:\\Users\\keylo\\PycharmProjects\\ProyectoRedesEntregaFinal\\TareaRedes-KeylorGuevara-JeannetteRojas-NatalinViquez\\TareaRedes_v2\\"  # directorio donde tendremos nuestras imagenes
# directorio donde tendremos nuestras imagenes
qualityimg = 80  # calidad de salida de las imagenes
### termina configuracion
print
"comprimiendo..."
for img in glob.glob(diri + '*.jpg') + glob.glob(diri + '*.png'):
    try:
        namefile = os.path.basename(img)
        splitname = os.path.splitext(namefile)
        namefile = splitname[0]
        extens = splitname[1]
        i = Image.open(img)
        i.save(diri + "compress_" + namefile + extens, quality=qualityimg)
    except ValueError:
        print
        ValueError
        cont = cont + 1
if cont > 0:
    print
    "Algunos archivos no se puedieron comprimir"
else:
    print
    "todos los ficheros fueron comprimidos con exito"
