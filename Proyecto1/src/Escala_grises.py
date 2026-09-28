import cv2

def convertir_a_grises(imagen_color):
    
    imagen_gris = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2GRAY)
    return imagen_gris