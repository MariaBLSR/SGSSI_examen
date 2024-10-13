# Solicitar la ruta del archivo letras_ordenadas.txt
ruta_letras_ordenadas = input("Ingresa la ruta del archivo letras_ordenadas.txt: ")

# Solicitar la ruta del archivo frecuencias.txt
ruta_frecuencias = input("Ingresa la ruta del archivo frecuencias.txt: ")

# Solicitar la ruta del archivo original a modificar
ruta_archivo_original = input("Ingresa la ruta del archivo de texto original: ")

# Leer las dos primeras letras de letras_ordenadas.txt
with open(ruta_letras_ordenadas, 'r', encoding='utf-8') as archivo_letras:
    letras = []
    for linea in archivo_letras:
        letra = linea.split(":")[0].strip()  # Extraer la letra antes de los dos puntos
        letras.append(letra)
        if len(letras) == 2:
            break

# Leer las dos primeras letras de frecuencias.txt (ignorando las frecuencias)
with open(ruta_frecuencias, 'r', encoding='utf-8') as archivo_frecuencias:
    letras_frecuencias = []
    for linea in archivo_frecuencias:
        letra = linea.split()[0].strip()  # Extraer la letra antes del valor de frecuencia
        letras_frecuencias.append(letra)
        if len(letras_frecuencias) == 2:
            break

# Asegurarnos de que tenemos dos letras en ambos archivos
if len(letras) < 2 or len(letras_frecuencias) < 2:
    print("No hay suficientes letras en los archivos para realizar la sustitución.")
    exit()

# Asignar las letras
letra_1_original = letras[0]
letra_2_original = letras[1]

letra_1_nueva = letras_frecuencias[0]
letra_2_nueva = letras_frecuencias[1]

# Leer el contenido del archivo original
with open(ruta_archivo_original, 'r', encoding='utf-8') as archivo_original:
    contenido_original = archivo_original.read()

# Realizar las sustituciones en el texto original
contenido_modificado = contenido_original.replace(letra_1_original, letra_1_nueva)
contenido_modificado = contenido_modificado.replace(letra_2_original, letra_2_nueva)

# Guardar el nuevo contenido en un archivo de salida
ruta_archivo_modificado = "texto_modificado.txt"
with open(ruta_archivo_modificado, 'w', encoding='utf-8') as archivo_modificado:
    archivo_modificado.write(contenido_modificado)

print(f"Sustituciones completadas. Archivo modificado guardado como {ruta_archivo_modificado}")

