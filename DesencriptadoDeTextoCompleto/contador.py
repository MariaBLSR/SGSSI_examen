from collections import Counter

# Solicitar la ruta del archivo de texto al usuario
ruta_archivo = input("Ingresa la ruta del archivo .txt: ")

# Leer el contenido del archivo
with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()

# Contar las apariciones de cada letra (respetando mayúsculas y minúsculas)
contador_letras = Counter(c for c in contenido if c.isalpha())

# Ordenar las letras por número de apariciones (de mayor a menor)
letras_ordenadas = sorted(contador_letras.items(), key=lambda x: x[1], reverse=True)

# Crear el nuevo archivo de salida
ruta_salida = "letras_ordenadas.txt"
with open(ruta_salida, 'w', encoding='utf-8') as salida:
    for letra, cantidad in letras_ordenadas:
        salida.write(f"{letra}: {cantidad}\n")

print(f"Archivo creado con éxito: {ruta_salida}")

