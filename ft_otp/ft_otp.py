# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_otp.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sallorca <sallorca@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/05 12:27:09 by sallorca          #+#    #+#              #
#    Updated: 2023/05/10 16:14:17 by sallorca         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pyotp
import struct
import argparse
import hmac
import base64
import hashlib
import time
import binascii
from cryptography.fernet import Fernet


def arguments():
    
    parser = argparse.ArgumentParser(description="Herramienta para generar contraseñas")
    parser.add_argument("-g", help="Genera un fichero en eque almacenará una clave hexadecimal de 64 caracteres", dest="hex")
    parser.add_argument("-k", help="Genera nueva contraseña temporal la muestra en salida estandar", dest="key")
    args = parser.parse_args()
    return(args)
    
def read_file_hex():
    with open("key.hex", "r") as file:
        hex = file.read()
        return(hex)

def key_hex(hex):
    if len(hex) >= 64 and all(c in "0123456789abcdefABCDEF" for c in hex):
        pass
    else:
        print("ERROR, LA CLAVE NO ES HEXADECIMAL")
        exit()

def encrypt_key(hex):
    hex2bytes = bytes(hex, "utf-8")
    bytes2b32 = base64.b32encode(hex2bytes)
    secret = bytes2b32.decode("utf-8")
    clave_key = Fernet.generate_key()
    f = Fernet(clave_key)
    encrypt_key = f.encrypt(bytes(secret, "utf-8"))
    with open("master.key", "wb") as file:
        file.write(clave_key)
    with open("ft_otp.key", "wb") as file:
        file.write(encrypt_key)
    
    return encrypt_key

def decrypt_key():
    with open("master.key", "rb") as file:
        clave_key = file.read()
    with open("ft_otp.key", "rb") as file:
        encrypt_key = file.read()
        f = Fernet(clave_key)
        decry_key = f.decrypt(encrypt_key)
    return decry_key
    
def get_hotp_token(secret, intervals_no):
    key = base64.b32decode(secret, True)
    #decoding our key
    msg = struct.pack(">Q", intervals_no)
    #conversions between Python values and C structs represente
    h = hmac.new(key, msg, hashlib.sha1).digest()
    o = o = h[19] & 15
    #Generate a hash using both of these. Hashing algorithm is HMAC
    h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
    #unpacking
    return h
def get_totp_token(secret):
    #ensuring to give the same otp for 30 seconds
    x =str(get_hotp_token(secret,intervals_no=int(time.time())//30))
    #adding 0 in the beginning till OTP has 6 digits
    while len(x)!=6:
        x+='0'
    return x

def pytotp (token):
    totp = pyotp.TOTP(token)
    print("Current OTP:", totp.now())
    

if __name__ == "__main__":

    args = arguments()
    gen = args.hex
    get = args.key
    if (args.hex == "key.hex"):
        clave = read_file_hex()
        key_hex(clave)
        encrypt_key(clave)
        print("Key was successfully saved in ft_otp.key.")
    elif (args.key == "ft_otp.key"):
        token = decrypt_key()
        print(get_totp_token(token)) 
        pytotp(token)
    else:
        print("Error")