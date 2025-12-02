import random

print("=== GENERADOR DE CONTRASEÑAS $$$ ===")

# PEDIR LA LONGITUD DE LA CONTRASEÑA
longitud = int(input("Ingresa la longitud de la contraseña: "))

# VALORAR QUE LA LONGITUD SEA MAYOR A 0, WHILE GENERARA UN BUCLE DEL BLOQUE DE CODIGO QUE CONTENGA SI NO SE CUMPLEN LOS PARAMETROS 
while longitud <= 0:
    print(f"ERROR: LA LONGITUD {longitud} NO ES VÁLIDA (debe ser mayor a 0)")
    longitud = int(input("Ingresa de nuevo la longitud de la contraseña: "))

#-------------preguntas de configuracion de contraseña------------
#preguntar si va usar numeros 
#lower convierte el texto ingresado a minuscula (si pongo "SI"  devolvera "si")
respuesta_num=input("La contraseña usara numeros si/no : "). lower () 
while respuesta_num != "si" and respuesta_num!= "no":
    print ("Respuesta no valida, usa si/no : ")
    respuesta_num= input ("La contraseña usara numeros si/no : ").lower ()

#preguntar si va usar letras (Mayusculas) 
respuesta_mayus=input("La contraseña usara Letras si/no : "). lower ()
while respuesta_mayus != "si" and respuesta_mayus != "no":
    print ("Respuesta no valida, usa si/no : ")
    respuesta_mayus=input ("La contraseña usara letras si/no : "). lower ()

#preguntar si va usar símbolos
respuesta_espec=input ("La contraseña usara símbolos si/no : "). lower ()
while respuesta_espec != "si" and respuesta_espec != "no":
    print ("Respuesta no valida, usa si/no : ")
    respuesta_espec=input ("La contraseña usara símbolos si/no : "). lower ()
    

# vaidar que al menos un tipo sea elegido 
while respuesta_num == "no" and respuesta_mayus =="no" and respuesta_espec =="no":
    print ("Debes elegir al menos un tipo para conformar la contrasela")

    respuesta_num=input("La contraseña usara numeros si/no : "). lower () 
    while respuesta_num != "si" and respuesta_num!= "no":
        print ("Respuesta no valida, usa si/no : ")
        respuesta_num= input ("La contraseña usara numeros si/no : ").lower ()

#preguntar si va usar letras (Mayusculas) 
    respuesta_mayus=input("La contraseña usara Letras si/no : "). lower ()
    while respuesta_mayus != "si" and respuesta_mayus != "no":
        print ("Respuesta no valida, usa si/no : ")
        respuesta_mayus=input ("La contraseña usara letras si/no : "). lower ()

#preguntar si va usar símbolos
    respuesta_espec=input ("La contraseña usara símbolos si/no : "). lower ()
    while respuesta_espec != "si" and respuesta_espec != "no":
        print ("Respuesta no valida, usa si/no : ")
        respuesta_espec=input ("La contraseña usara símbolos si/no : "). lower ()



# -------------------GENERADOR DE LA CONTRASEÑA---------------------------
# se inicia el contenedor de la contraseña (password) y el contador (contador)

password = ""
contador = 0

# bucle principal que genera cada caracter de contraseña
while contador < longitud :
    # calculamos cuantos tipos de caracteres vamos a usar 
    num_tipos=0
    if respuesta_num == "si":
        num_tipos=num_tipos + 1
    if respuesta_mayus == "si":
        num_tipos=num_tipos + 1 
    if respuesta_espec == "si":
        num_tipos=num_tipos + 1 

    # asignamos la identificacion de los caracteres para que el codigo sepa cual es el escogido 

    # 0 = numero, 1 = letras, 2 = símbolos
    if num_tipos == 1: 
    # solo hay un tipo activo, aqui identificamos cual es el que esta activo  
       if    respuesta_num == "si":
           tipo = 0
       elif  respuesta_mayus == "si":
           tipo = 1
       else :
           tipo = 2

    # aqui hay dos tipos escogidos y segun los que esten escogidos generara la contraseña 
    elif num_tipos == 2:
        tipo_random = random.randint(0,1)
        if respuesta_num == "si" and respuesta_mayus == "si":
            if tipo_random == 0:
                tipo = 0
            else:
                tipo = 1
        elif respuesta_num == "si" and respuesta_espec == "si":
            if tipo_random == 0 :
                tipo = 0
            else :
                 tipo = 2
        else :
            if respuesta_mayus == "si" and respuesta_espec == "si" :
               if tipo_random == 0 :
                  tipo= 1 
               else :
                  tipo = 2
    # en este caso si esta escogido los 3 tipos 
    else :
        tipo= random.randint (0,2)

    # segu  el tipo se va calcular por el  codigo ASSCI 
    # esto aplica cuando se escoge un valor, 2 valores o 3 

    if tipo==0:
       codigo= 48 + random.randint (0,9)     # numeros de 0 al 9
    elif tipo ==1:
       codigo = 65 + random.randint (0,25)   # letras A HASTA LA Z
    else :
       codigo = 33 + random.randint (0,14) # simbolos ! " # $ % & ' ( ) * + , - . /   


    # convertimos el numero entregado a su caracter correspondiente en codigo ASCII
    #  se ingresa el caracter en la funcion (password)
    # se inicia el conteo del bucle hasta completar la longitud de la contraseña 

    caracter= chr(codigo)
    password= password + caracter  
    contador = contador + 1

#....................MOSTRAR CONTRASEÑA Y EVALUAR SEGURIDAD DE CONTRASEÑA Y COPIAR CONTRASEÑA ..................

if   num_tipos == 1:
     num_tipos = "DEBIL"
elif num_tipos == 2:
     num_tipos = "MEDIA"
else :
    num_tipos = "FUERTE"


copia=input ("Quieres copiar la contraseña si/no ? "). lower ()
if copia == "si":
    mensaje= "Contraseña copiada"
else:
    mensaje= "no se copio la contraseña"

while copia != "si" and copia!= "no":
    print ("elije una respuesta correcta si/no")
    copia=input ("Quieres copiar la contraseña si/no ? "). lower ()
    if copia == "si":
        mensaje= "Contraseña copiada"
    else:
        mensaje = "no se copio la contraseña"


print (f"La contraseña es;  {password},  tiene una seguridad {num_tipos}, {mensaje} ")



         
         
            




        







    
    
    







