# Función para mostrar todas las palabras del texto
def mostrar_todas_palabras(texto):
    palabras = texto.split()  # Dividimos el texto en palabras por espacios
    print("Todas las palabras en el texto:")
    print(", ".join(palabras))

# Función para realizar un cambio de letras en el texto
def cambiar_letra(texto):
    letra_a_cambiar = input("¿Qué letra quiere cambiar? ").strip()
    letra_nueva = input("¿Qué letra quiere poner a cambio? ").strip()

    if letra_a_cambiar and letra_nueva:
        texto_modificado = texto.replace(letra_a_cambiar, letra_nueva)
        print(f"Cambio realizado: {letra_a_cambiar} por {letra_nueva}")
        return texto_modificado
    else:
        print("No se realizó ningún cambio.")
        return texto

# Leer el contenido de texto_modificado.txt
ruta_archivo_modificado = "texto_modificado.txt"
with open(ruta_archivo_modificado, 'r', encoding='utf-8') as archivo:
    contenido_texto = archivo.read()

# Mostrar todas las palabras del texto
mostrar_todas_palabras(contenido_texto)

# Bucle para realizar cambios de letras hasta que el usuario decida parar
while True:
    respuesta = input("¿Quiere cambiar alguna letra? s/n: ").strip().lower()
    
    if respuesta == 's':
        contenido_texto = cambiar_letra(contenido_texto)
        mostrar_todas_palabras(contenido_texto)  # Mostrar todas las palabras nuevamente tras el cambio
    elif respuesta == 'n':
        break
    else:
        print("Respuesta no válida. Por favor, elija 's' o 'n'.")

# Guardar el texto modificado
try:
    with open(ruta_archivo_modificado, 'w', encoding='utf-8') as archivo:
        archivo.write(contenido_texto)
    print(f"Texto final guardado en {ruta_archivo_modificado}")
except IOError as e:
    print(f"Error al guardar el archivo: {e}")

