# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sallorca <sallorca@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 13:20:26 by sallorca          #+#    #+#              #
#    Updated: 2023/04/19 19:09:38 by sallorca         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = (1, 4)

if __name__=="__main__":
    if isinstance(kata, int):
        print("The number is:", kata)
    else:
        print("The", len(kata), "numbers are: ",', ' .join(str(x)for x in kata))
