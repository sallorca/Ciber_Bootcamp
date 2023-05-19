# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sallorca <sallorca@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 12:25:44 by sallorca          #+#    #+#              #
#    Updated: 2023/04/19 17:15:48 by sallorca         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys, string

def text_analyzer(cadena=""):
    """
   This function counts the number of upper characters, lower characters,\n   punctuation and spaces in a given text.
    """
    upp, low, sig, sp, ch = 0, 0, 0, 0, 0

    if cadena == "":
        cadena = input("What is the text to analyze?\n")
    if not isinstance(cadena, str):
        print("AssertionError: argument is not a string")
        return
    for c in cadena:
        if c.isupper(): upp +=1
        elif c.islower(): low +=1
        elif c in string.punctuation: sig +=1
        elif c.isspace(): sp +=1
        ch +=1
    print(f"The text contains {ch} character(s):")
    print(f"- {upp} upper letter(s)")
    print(f"- {low} lower letter(s)")
    print(f"- {sig} punctation mark(s)")
    print(f"- {sp} space(s)")

if __name__=="__main__":
    if len(sys.argv) > 2:
        print("Error too many arguments")
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        text_analyzer()

