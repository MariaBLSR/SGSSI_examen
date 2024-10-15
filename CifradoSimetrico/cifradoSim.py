import os
import subprocess

def cifrar_archivo(ruta_archivo):
    # Comando para cifrar el archivo
    comando = ['gpg', '-c', ruta_archivo]

    # Ejecutar el comando de cifrado
    try:
        subprocess.run(comando, check=True)
        print(f'Archivo cifrado: {ruta_archivo}.gpg')
        print('El archivo está listo para ser enviado.')
    except subprocess.CalledProcessError as e:
        print(f'Error al cifrar el archivo: {e}')

def main():
    ruta_archivo = input('Introduce la ruta del archivo a cifrar: ')
    if not os.path.isfile(ruta_archivo):
        print('El archivo no existe. Por favor, verifica la ruta.')
        return
    cifrar_archivo(ruta_archivo)

if __name__ == '__main__':
    main()
