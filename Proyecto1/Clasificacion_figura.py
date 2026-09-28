def clasificacion(puntas):
    if (puntas == 0):
        return "O"

    if (puntas == 4):
        return "C"

    if (puntas == 3):
        return "T"

    if (puntas <3 or puntas > 4):
        return "X"