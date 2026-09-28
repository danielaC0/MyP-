import cv2
import numpy as np

def cargar_imagen(ruta_imagen):
    """
    Carga una imagen desde la ruta especificada.
    """
    # cv2.imread lee la imagen. El segundo parámetro (1) indica que se cargue a color.
    imagen = cv2.imread(ruta_imagen, 1)
    
    # Verificamos si la imagen se cargó correctamente
    if imagen is None:
        raise FileNotFoundError(f"Error: No se pudo cargar la imagen en la ruta '{ruta_imagen}'. Verifica que la ruta sea correcta y el archivo sea .bmp")
    
    return imagen
    imagen = cargar_imagen("mi_imagen.bmp")