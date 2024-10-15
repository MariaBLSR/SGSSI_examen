import subprocess
import sys

def descifrar_archivo(archivo_encriptado, archivo_descifrado):
    try:
        print(f"Descifrando {archivo_encriptado}...")
        subprocess.run(['gpg', '--output', archivo_descifrado, '--decrypt', archivo_encriptado], check=True)
        print(f"El archivo ha sido descifrado y guardado como {archivo_descifrado}.")
    except subprocess.CalledProcessError as e:
        print(f"Error al descifrar el archivo: {e}")
        sys.exit(1)

if __name__ == "__main__":
    archivo_encriptado = input("Introduce el nombre del archivo encriptado (por ejemplo, documento_encriptado_firmado.gpg): ")
    archivo_descifrado = input("Introduce el nombre que deseas para el archivo descifrado (por ejemplo, archivo_descifrado): ")

    descifrar_archivo(archivo_encriptado, archivo_descifrado)
