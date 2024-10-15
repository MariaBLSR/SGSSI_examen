import os
import subprocess

def ejecutar_comando(comando):
    """Ejecuta un comando en la terminal y maneja errores."""
    try:
        resultado = subprocess.run(comando, shell=True, check=True, text=True, capture_output=True)
        print(resultado.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {comando}")
        print(e.stderr)

def main():
    # Solicitar correo y ruta al usuario
    correo = input("Introduce el correo del destinatario: ")
    ruta = input("Introduce la ruta del archivo a encriptar y firmar: ")

    # Comprobar si el archivo existe
    if not os.path.isfile(ruta):
        print("El archivo no existe. Por favor, introduce una ruta válida.")
        return

    # Crear el comando GPG
    comando_gpg = f'gpg --output documento_encriptado_firmado.gpg --encrypt --sign --recipient "{correo}" "{ruta}"'
    print(f"Ejecutando: {comando_gpg}")

    # Ejecutar el comando
    ejecutar_comando(comando_gpg)

    print("Proceso completado.")

if __name__ == "__main__":
    main()
