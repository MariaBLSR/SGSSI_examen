import subprocess
import sys

def importar_clave(correo):
    try:
        print(f"Importando la clave de {correo}...")
        subprocess.run(['gpg', '--keyserver', 'keys.openpgp.org', '--search-keys', correo], check=True)
        print("La clave ha sido importada correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al importar la clave: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Solicitar el correo de la persona de quien importar la clave
    correo = input("Introduce el correo de la persona de quien deseas importar la clave: ")

    importar_clave(correo)
