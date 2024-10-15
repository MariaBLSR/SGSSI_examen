import subprocess
import os

def install_gpg():
    print("Instalando GPG...")
    subprocess.run(["sudo", "apt", "install", "-y", "gpg"])

def generate_key(email):
    print("Generando clave GPG...")
    # Este comando ejecuta gpg --generate-key interactivamente
    # Para evitar interacciones, podrías considerar usar un archivo de configuración.
    subprocess.run(["gpg", "--batch", "--passphrase", "", "--generate-key"], input=f"""
    %no-protection
    Key-Type: default
    Key-Length: 2048
    Subkey-Type: default
    Name-Real: Mi Nombre
    Name-Email: {email}
    Expire-Date: 0
    %commit
    """, text=True, check=True)

def list_keys():
    print("Listando claves GPG...")
    subprocess.run(["gpg", "--list-keys"])

def generate_revocation(email):
    print(f"Generando certificado de revocación para {email}...")
    revocation_file = "revocacion.asc"
    subprocess.run(["gpg", "--output", revocation_file, "--gen-revoke", email])
    print(f"Certificado de revocación guardado como {revocation_file}.")

def main():
    email = input("Introduce tu correo electrónico: ")

    install_gpg()
    generate_key(email)
    list_keys()
    generate_revocation(email)

if __name__ == "__main__":
    main()
