# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scorpion.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sallorca <sallorca@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/02 15:20:42 by sallorca          #+#    #+#              #
#    Updated: 2023/05/03 15:38:01 by sallorca         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse
import sys
from PIL import Image, ExifTags

def arguments():
    parser = argparse.ArgumentParser(description="Analizador de metadatos")
    parser.add_argument("Imagen", help="Imagen a analizar", type=str)
    parser.add_argument("Imagenes", help="Imagenes a analizar", nargs="*")
    return parser.parse_args()

def info(imagen):
    print("Nombre".ljust(29), ":", imagen.filename.split("/"))
    print("Dimensiones".ljust(29), ":", imagen.size[0], imagen.size[1])
    print("Formato".ljust(29), ":", imagen.format) 
    print("Modo".ljust(29), ":", imagen.mode)
    print("Paleta".ljust(29), ":", imagen.palette)

def scorpion(rutas):
    for r in rutas:
        try:
            open_ima = Image.open(r)
        except:
            print("No se puede abrir mi imagen", r)
        else:
            exi_ima = open_ima.getexif()
            print(r.split("/")[-1])
            info(open_ima)
            if not exi_ima:
                print("No hay datos exif")
            for key, val in exi_ima.items():
                if key in ExifTags.TAGS:
                    print(f'{ExifTags.TAGS[key]:30} {val}')

if __name__ == "__main__":
    
    args = arguments()

    comandos = list()
    comandos.append(args.Imagen)
    comandos += args.Imagenes
    
    scorpion(comandos)
    
                
    