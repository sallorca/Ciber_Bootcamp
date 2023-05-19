# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sallorca <sallorca@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/18 17:22:31 by sallorca          #+#    #+#              #
#    Updated: 2023/04/19 11:29:38 by sallorca         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

cod_morse = {'a': '.-', 'b': '- . . .', 'c': '- . - .', 'd': '-..',
             'e': '..-..', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
             'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
             'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...',
             't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
             'y ': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3': '...--',
             '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
             '9': '----.', '0': '-----', ' ': '/'}

def ecode_morse(mens):
    stri = []
    for c in mens:
        words = cod_morse.get(c.lower())
        if (words):
            stri.append(words)
        else:
            return None
        return (" ".join(stri))

def send_mensaje():
    if (len(sys.argv) == 1):
        print("Error! Usage: python3 sos.py <arg>")
    else:
        mensaje = []
        for mens in (" ".join(sys.argv[1:])):
            stri = ecode_morse(mens)
            if stri:
                mensaje.append(stri)
            else:
                print("ERROR")
                sys.exit(1)
        print(" ".join(mensaje))

if (__name__=='__main__'):
    send_mensaje()
