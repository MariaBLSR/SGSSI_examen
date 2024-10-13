import subprocess
import os

def generar_clave_ssh():
    email = "mariabogajo@gmail.com"
    ssh_folder = os.path.expanduser("~/.ssh")
    private_key_path = os.path.join(ssh_folder, "id_ed25519")
    public_key_path = private_key_path + ".pub"

    # Crear la carpeta .ssh si no existe
    if not os.path.exists(ssh_folder):
        os.makedirs(ssh_folder)

    # Generar la clave SSH
    try:
        print("Generando clave SSH...")
        subprocess.run(["ssh-keygen", "-t", "ed25519", "-C", email, "-f", private_key_path, "-N", ""])
        print("Clave SSH generada correctamente.")
    except Exception as e:
        print(f"Error generando la clave SSH: {e}")
        return

    # Iniciar el agente SSH
    try:
        print("Iniciando ssh-agent...")
        subprocess.run(["eval", "$(ssh-agent -s)"], shell=True, check=True)
        print("ssh-agent iniciado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error iniciando ssh-agent: {e}")
        return

    # Añadir la clave privada al agente
    try:
        print(f"Añadiendo clave privada al agente desde {private_key_path}...")
        subprocess.run(["ssh-add", private_key_path])
        print("Clave privada añadida al agente correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error añadiendo la clave privada al agente: {e}")
        return

    # Mostrar la clave pública
    try:
        print("Clave pública:")
        subprocess.run(["cat", public_key_path])
    except subprocess.CalledProcessError as e:
        print(f"Error mostrando la clave pública: {e}")

if __name__ == "__main__":
    generar_clave_ssh()
