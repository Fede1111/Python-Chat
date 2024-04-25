import requests
import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC



nombre = input("Tu nombre: ")
sala = input("Ingrese el nombre de la sala. (Si no existe se crea una nueva): ")
contrasenia = input("Ingresa tu contraseña: ")

FIREBASE_DATABASE_URL = 'https://tu-base-de-datos.firebaseio.com/' + sala + '.json'

def generar_clave_desde_contrasenia(contrasenia, salt=b'saltsaltsaltsalt'):
    """Genera una clave a partir de una contraseña utilizando PBKDF2."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    clave = kdf.derive(contrasenia.encode())
    return base64.urlsafe_b64encode(clave)





clave_encriptacion = generar_clave_desde_contrasenia(contrasenia)
clave_desencriptacion = generar_clave_desde_contrasenia(contrasenia)
    

def mostrar_chat(sala):
    # Realiza una solicitud GET para obtener los mensajes del chat desde Firebase
    FIREBASE_DATABASE_URL = 'https://tu-base-de-datos.firebaseio.com/' + sala + '.json'
    response = requests.get(FIREBASE_DATABASE_URL)
    mensajes = response.json()

    if mensajes:
        print("•" * 40)
        print("      1111Chat")
        print("•" * 40)
        print("- Conversaciones cifradas -")
        print("•" * 40)
        print("La Privacidad es parte de la Libertad")
        print("•" * 40)

        try:

          for key, value in mensajes.items():
              
              texto_encriptado = value['mensaje'].encode('utf-8') 
              texto_desencriptado = desencriptar_texto(texto_encriptado, clave_desencriptacion)

              print(f"{value['usuario']}: " + texto_desencriptado)
              

          print("-" * 40)    
                
        except Exception as e:  
        
            print("El chat existe.")     
            print("Contraseña incorrecta")
           
            
    else:
        print("¡Aún no hay mensajes en el chat!")


# Función para generar la clave a partir de una contraseña
def generar_clave_desde_contrasenia(contrasenia, salt=b'saltsaltsaltsalt'):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    clave = kdf.derive(contrasenia.encode())
    return base64.urlsafe_b64encode(clave)

# Función para encriptar un texto usando la clave
def encriptar_texto(texto, clave):
    cipher_suite = Fernet(clave)
    texto_encriptado = cipher_suite.encrypt(texto.encode())
    return texto_encriptado

# Función para desencriptar un texto usando la clave
def desencriptar_texto(texto_encriptado, clave):
    cipher_suite = Fernet(clave)
    texto_desencriptado = cipher_suite.decrypt(texto_encriptado)
    return texto_desencriptado.decode()        

# Función para enviar un mensaje al chat en Firebase
def enviar_mensaje(usuario, mensaje_encriptado):
    mensaje_data = {'usuario': usuario, 'mensaje': mensaje_encriptado}
    response = requests.post(FIREBASE_DATABASE_URL, json=mensaje_data)

# Función principal
def main():
    # Limpia la pantalla
    os.system('clear')
    
    # Genera la clave a partir de la contraseña (deberías pedir al usuario que ingrese su contraseña)
   
    
    print("Clave generada en base64:", clave_desencriptacion)
    
    # Muestra el chat
    mostrar_chat(sala,contrasenia)

    # Ciclo principal para enviar mensajes
    while True:
        mensaje = input("Mensaje: ")

        if mensaje == "salir":
            break
        elif mensaje == "comandos":
            print("salir = Sale del chat")

        else:        
            # Encripta el mensaje antes de enviarlo
            mensaje_encriptado = encriptar_texto(mensaje, clave_encriptacion)
            # Envía el mensaje al chat
            enviar_mensaje(nombre, mensaje_encriptado)
            # Limpia la pantalla y muestra el chat actualizado
            os.system('clear')
            mostrar_chat(sala,clave_desencriptacion)

if __name__ == "__main__":
    main()



