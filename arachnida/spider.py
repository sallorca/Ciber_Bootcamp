# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    spider.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sallorca <sallorca@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/21 13:50:37 by sallorca          #+#    #+#              #
#    Updated: 2023/05/03 15:58:40 by sallorca         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse
import requests
import os

from bs4 import BeautifulSoup as sopa
from urllib.parse import urlparse

web_pages = set()
images_found = set()
img_form = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')

def extraer_url(url, level):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            xml = sopa(response.content, "html.parser")
            enlaces = [enlace.get("href") for enlace in xml.find_all("a") if enlace.has_attr("href") and (enlace["href"].startswith("http://") or enlace["href"].startswith("https://"))]
            urlparseada = urlparse(url)
            esquema = urlparseada.scheme
            dominio = urlparseada.netloc
            ruta = urlparseada.path
            if int(level) < 1:
                return
            else:
                for enlace in enlaces:
                    if enlace is not None and enlace.startswith(esquema + "://" + dominio):
                        urlparseada_enlace = urlparse(enlace)
                        dominio_enlace =  urlparseada_enlace.netloc
                        if dominio_enlace == dominio:
                            if enlace not in web_pages:
                                web_pages.add(enlace)
                                print(" " * level, enlace)
                                extraer_url(enlace, level - 1)
                    else:
                        if enlace.startswith("/") and not enlace.startswith("://"):
                            enlace_completo = esquema + "://" + dominio + enlace
                            if enlace_completo not in web_pages:
                                web_pages.add(enlace_completo)
                                print(" " *level, enlace_completo)
                                extraer_url(enlace_completo, level -1)
            return esquema, dominio, ruta
    except:
        print("URL NOT VALID")

def extraer_img():
    for element in web_pages:
        try:
            i = requests.get(element)
            if i.status_code == 200:
                xmli = sopa(i.content, "html.parser")
                etiquetas = xmli.find_all("img")
        except:
            print("URL NOT VALID")
        else:
            url_img = [img["src"] for img in etiquetas]
            for url in url_img:
                if url in images_found:
                    continue
                else:
                    try:
                        urli = requests.get(url)
                    except:
                        continue
                    else:
                        if not any(cont in url for cont in img_form):
                            continue
                        else:
                            nombre = url.split("/")[-1]
                            if not os.path.exists(p):
                                os.mkdir(p)
                            with open(p + '/' + nombre, 'wb') as archivo:
                                archivo.write(urli.content)
                        images_found.add(url)                                 
                            
                    
def spider():
    global url, level, p, re
    
    parser = argparse.ArgumentParser(description='Extrac images from a URL')
    parser.add_argument('URL', help='URL to extract the images from')
    parser.add_argument('-r', help='recursive download of images', action='store_true', required=False)
    parser.add_argument('-l', help='level of the recursive download of images, 5 by  default',
                        metavar='N', default=5, type=int, dest='l', required=False)
    parser.add_argument('-p', help='path where download the images, by default the images will be download in the "data" directory',
                      action='store', default='data', dest='p', required=False)
    args = parser.parse_args()
    
    url = args.URL
    re = args.r
    level = args.l
    p = args.p
    try:
        print("Analizando las paginas")
        if re:
            extraer_url(url, level)
        else:
            web_pages.add(url)
        extraer_img()
    except:
        print("URL NOT VALID")
    
    
if __name__ == "__main__":
    spider()
        





