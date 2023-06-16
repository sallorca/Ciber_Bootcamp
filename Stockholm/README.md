# Stockholm

Stockholm es un programa de cifrado de archivos en Python que utiliza la biblioteca "cryptography.fernet" para encriptar archivos con una clave simétrica y desencriptarlos posteriormente. Este programa se ejecuta desde la línea de comandos y admite varias opciones.

## Requisitos

- Python 3.6 o superior
- biblioteca cryptography.fernet

## Uso

Ejecute el programa desde la línea de comandos. Puede usar las siguientes opciones:

- `-v, --version`: muestra la versión del programa.
- `-r, --reverse KEY`: descifra los archivos usando la clave "KEY" dada.
- `-s, --silent`: activa el modo silencioso.

Cuando se ejecuta sin opciones, el programa cifrará los archivos en la carpeta "infection" en el directorio principal del usuario actual. Si se proporciona una clave con la opción `-r`, el programa descifrará los archivos en la misma carpeta.

El programa buscará todos los archivos en la carpeta "infection" con las extensiones especificadas en la lista "ext" y los cifrará o descifrará según corresponda. Los archivos cifrados se guardarán con una extensión adicional ".ft".

## Limitaciones

Este programa solo admite la encriptación y desencriptación de archivos en una sola carpeta. Además, no se proporciona ninguna medida de seguridad adicional, como la protección de la clave de cifrado. Por lo tanto, se recomienda utilizar este programa solo con fines educativos y no para cifrar archivos sensibles.
