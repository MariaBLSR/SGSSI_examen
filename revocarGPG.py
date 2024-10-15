import os
import subprocess

def importar_revocacion(revocacion_file):
    """Importa el certificado de revocación."""
    try:
        subprocess.run(['gpg', '--import', revocacion_file], check=True)
        print(f"Revocación importada desde {revocacion_file}.")
    except subprocess.CalledProcessError:
        print("Error al importar la revocación.")

def enviar_revocacion(key_id):
    """Envía la revocación al servidor de claves."""
    try:
        subprocess.run(['gpg', '--keyserver', 'hkp://keyserver.ubuntu.com', '--send-keys', key_id], check=True)
        print(f"Revocación enviada para la clave {key_id}.")
    except subprocess.CalledProcessError:
        print("Error al enviar la revocación al servidor de claves.")

def main():
  
    revocacion_file = input("Introduce la ubicación del archivo de revocación (ej. /ruta/a/revocacion.asc): ")

    if not os.path.isfile(revocacion_file):
        print("El archivo de revocación no existe. Asegúrate de que la ruta sea correcta.")
        return
    
    key_id = input("Introduce el ID de la clave que deseas revocar: ")
        
    importar_revocacion(revocacion_file)
    
    enviar_revocacion(key_id)

if __name__ == "__main__":
    main()
