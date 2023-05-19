# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sallorca <sallorca@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/18 10:50:16 by sallorca          #+#    #+#              #
#    Updated: 2023/04/18 17:14:14 by sallorca         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys, string

def goodword():
    if (len(sys.argv) != 3):
        print("ERROR")
    else:
        try:
            n = int(sys.argv[2])
            p = string.punctuation
            s = sys.argv[1]
            s = s.translate(str.maketrans('', '', p))
            w = [word for word in s.split() if len(word) > n]
            print(w)
        except:
            print("ERROR")
        
if __name__=="__main__":
    goodword()