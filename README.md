
# Chat encriptado con Firebase

Este es un proyecto de chat encriptado que utiliza Firebase como base de datos y la biblioteca `cryptography` de Python para encriptar y desencriptar mensajes. Proporciona una forma segura de comunicarse en línea al cifrar los mensajes antes de enviarlos a través de la red.

## Requisitos previos

Antes de ejecutar la aplicación, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.x

## Instalación de dependencias

Puedes instalar las dependencias necesarias ejecutando el siguiente comando en tu terminal:

```bash
pip install requests cryptography
```

## Configuración

1. **Configuración de Firebase:**
   - Crea una base de datos en Firebase y obtén la URL de la base de datos.
   - Reemplaza `'https://tu-base-de-datos.firebaseio.com/'` con la URL de tu base de datos en el archivo `chat1111.py`.

## Uso

1. **Ejecutar la aplicación:**
   - Ejecuta el archivo `chat1111.py` en tu terminal usando Python.

2. **Iniciar sesión:**
   - Ingresa tu nombre de usuario, el nombre de la sala y tu contraseña cuando se te solicite.

3. **Enviar mensajes:**
   - Escribe tu mensaje en la línea de comandos y presiona Enter para enviarlo al chat.

4. **Comandos adicionales:**
   - Utiliza el comando `salir` para salir del chat.
   - Utiliza el comando `comandos` para ver la lista de comandos disponibles.

## Estructura del proyecto

- `chat1111.py`: El archivo principal que contiene la lógica del chat encriptado.
- `README.md`: El archivo que estás leyendo ahora, que proporciona información sobre el proyecto.

## Contribuciones

Si deseas contribuir a este proyecto, ¡no dudes en enviar un pull request! También puedes informar sobre errores o solicitar nuevas funcionalidades a través de las issues del repositorio.
