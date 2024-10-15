from PIL import Image
import hashlib

def encode_message(image_path, message, output_path):
    """ Oculta un mensaje en una imagen. """
    image = Image.open(image_path)
    binary_message = ''.join(format(ord(i), '08b') for i in message) + '1111111111111110'  # Fin del mensaje
    data = list(image.getdata())

    # Verifica si hay suficiente espacio para el mensaje
    if len(binary_message) > len(data) * 3:
        raise ValueError("El mensaje es demasiado largo para esta imagen.")

    # Reemplazar los bits menos significativos
    for i in range(len(binary_message)):
        pixel = list(data[i])
        for j in range(3):  # Para cada canal RGB
            if i < len(binary_message):
                pixel[j] = (pixel[j] & ~1) | int(binary_message[i])  # Cambiar el último bit
                i += 1
        data[i-1] = tuple(pixel)

    # Crear nueva imagen con el mensaje oculto
    image.putdata(data)
    image.save(output_path)
    print(f"Mensaje oculto en {output_path}")

def decode_message(image_path):
    """ Extrae el mensaje oculto de una imagen. """
    image = Image.open(image_path)
    binary_message = ''
    data = list(image.getdata())

    for pixel in data:
        for color in pixel[:3]:  # Solo RGB
            binary_message += str(color & 1)  # Obtener el último bit

    print(f"Mensaje binario extraído: {binary_message}")  # Mensaje binario para depuración

    # Convertir el mensaje binario a texto
    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if byte == '11111110':  # Fin del mensaje (cambiado para evitar confusiones)
            break
        message += chr(int(byte, 2))

    return message

def calculate_hash(file_path):
    """ Calcula el hash MD5 de un archivo. """
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Uso del script
if __name__ == "__main__":
    # Pedir al usuario la ruta de la imagen
    input_image = input("Introduce la ruta de la imagen de entrada: ")
    output_image = input("Introduce la ruta de la imagen de salida (ejemplo: output_image.png): ")

    # Validar que la ruta de salida tenga una extensión
    if not output_image.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        print("Error: El nombre de la imagen de salida debe incluir una extensión válida (ejemplo: .png, .jpg).")
        exit(1)

    secret_message = input("Introduce el mensaje secreto: ")

    # Ocultar el mensaje en la imagen
    encode_message(input_image, secret_message, output_image)

    # Calcular hash de la imagen con el mensaje oculto
    hash_value = calculate_hash(output_image)
    print(f"Hash MD5 de la imagen con mensaje: {hash_value}")

