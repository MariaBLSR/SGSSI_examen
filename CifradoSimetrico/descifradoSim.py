import os
import subprocess

def descifrar_archivo(ruta_archivo_cifrado, nombre_nuevo):

    comando = ['gpg', '-d', ruta_archivo_cifrado]

    with open(nombre_nuevo, 'w') as archivo_destino:
        try:
            subprocess.run(comando, check=True, stdout=archivo_destino)
            print(f'Archivo descifrado y guardado como: {nombre_nuevo}')
        except subprocess.CalledProcessError as e:
            print(f'Error al descifrar el archivo: {e}')

def main():
    ruta_archivo_cifrado = input('Introduce la ruta del archivo cifrado: ') 
    if not os.path.isfile(ruta_archivo_cifrado):
        print('El archivo cifrado no existe. Por favor, verifica la ruta.')
        return

    nombre_nuevo = input('Introduce el nombre del nuevo archivo (ejemplo: nombre_nuevo.txt): ')
    ruta_destino = os.path.join(os.getcwd(), nombre_nuevo)
    descifrar_archivo(ruta_archivo_cifrado, ruta_destino)

if __name__ == '__main__':
    main()
