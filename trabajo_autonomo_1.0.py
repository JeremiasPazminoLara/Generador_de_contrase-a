import random

print("=== GENERADOR DE CONTRASEÑAS $$$ ===")

# PEDIR LA LONGITUD DE LA CONTRASEÑA
longitud = int(input("Ingresa la longitud de la contraseña: "))

# VALORAR QUE LA LONGITUD SEA MAYOR A 0
while longitud <= 0:
    print(f"ERROR: LA LONGITUD {longitud} NO ES VÁLIDA (debe ser mayor a 0)")
    longitud = int(input("Ingresa de nuevo la longitud de la contraseña: "))