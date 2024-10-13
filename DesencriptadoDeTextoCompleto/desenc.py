import subprocess

# Función para ejecutar un script Python
def ejecutar_script(script_name):
    try:
        # Llamada para ejecutar el script
        subprocess.run(["python3", script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar {script_name}: {e}")

# Ejecutar los scripts de forma secuencial
print("Ejecutando contador.py...")
ejecutar_script("contador.py")

print("Ejecutando mod_frecs.py...")
ejecutar_script("mod_frecs.py")

# Bucle para ejecutar los scripts de modificación
while True:
    print("Ejecutando mod_palabrascortas.py...")
    ejecutar_script("mod_palabrascortas.py")
    
    print("Ejecutando mod_texto.py...")
    ejecutar_script("mod_texto.py")
    
    # Preguntar al usuario si desea continuar
    respuesta = input("¿Has terminado de modificar el texto? S/n: ").strip().lower()
    
    if respuesta == 's':
        print("Finalizando programa.")
        break
    elif respuesta == 'n':
        print("Reiniciando el ciclo de modificación...")
    else:
        print("Respuesta no válida. Por favor, elija 'S' o 'n'.")
