import cv2
import sys
import numpy as np
from Lector import cargar_imagen
from Array import analizar_arreglo_figuras

def procesar_imagen(ruta_imagen):
    try:
        imagen = cargar_imagen(ruta_imagen)
    except FileNotFoundError as e:
        print(e)
        return

    #para los pixeles de los bordes de la imagen
    borde_sup = imagen[0, :]
    borde_inf = imagen[-1, :]
    borde_izq = imagen[:, 0]
    borde_der = imagen[:, -1]
    
    #enlazamos todos los pixeles del borde en un solo arreglo
    pixeles_borde = np.concatenate((borde_sup, borde_inf, borde_izq, borde_der), axis=0)
    
    #para el color más frecuente en el borde que será el fondo
    colores, conteos = np.unique(pixeles_borde, axis=0, return_counts=True)
    color_fondo = colores[np.argmax(conteos)]
    
    #una máscara que aisle el color del fondo
    mask_bg = cv2.inRange(imagen, color_fondo, color_fondo)
    
    #la invertimos 
    mask_figuras = cv2.bitwise_not(mask_bg)

    #para los contornos sobre la nueva máscara
    contornos, _ = cv2.findContours(mask_figuras, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    analizar_arreglo_figuras(contornos, imagen)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso incorrecto. Ejecuta:")
        print("python main.py ruta_de_la_imagen.bmp")
    else:
        ruta = sys.argv[1]
        procesar_imagen(ruta)
