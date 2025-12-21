markdown

# Generador de contraseñas 
Este proyecto genera contraseñas aleatorias en Python segun la longitud
y los tipos de caracteres selccionados por el usuario (numeros,Letras, Simbolos),
asi mismo permite evaluar el nivel de seguridad de la contraseña generada y copiarla

Para ejecutar el programa en la terminal:

```bash
python trabajo_autonomo_1.0.py


Descripción y funcionalidades del código

-El programa funciona mediante interacción por consola y cuenta con las siguientes funcionalidades principales:
-Solicita al usuario la longitud de la contraseña y valida que sea un número mayor a cero.
-Permite elegir si la contraseña incluirá:
-Números
-Letras mayúsculas
-Símbolos especiales
-Verifica que al menos un tipo de carácter haya sido seleccionado.
-Genera la contraseña de forma aleatoria utilizando la librería random y códigos ASCII.
-Construye la contraseña carácter por carácter hasta alcanzar la longitud solicitada.
-Evalúa el nivel de seguridad de la contraseña generada:
-Débil: un tipo de carácter
-Media: dos tipos de caracteres
-Fuerte: tres tipos de caracteres
-Muestra la contraseña generada junto con su nivel de seguridad.
-Ofrece la opción de copiar la contraseña (simulada).
