import subprocess

def instalar_apache():
    """Instala Apache2 usando apt-get."""
    try:
        # Ejecuta el comando para instalar Apache2
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)  # Actualiza la lista de paquetes
        subprocess.run(['sudo', 'apt-get', 'install', 'apache2', '-y'], check=True)  # Instala Apache2
        print("Apache2 se ha instalado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Ocurrió un error durante la instalación: {e}")

if __name__ == "__main__":
    instalar_apache()
