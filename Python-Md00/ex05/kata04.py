# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sallorca <sallorca@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/14 11:08:25 by sallorca          #+#    #+#              #
#    Updated: 2023/04/14 15:49:41 by sallorca         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = (0, 4, 132.42222, 10000, 12345.67)
print("module_{:02d}, ex_{:02d} : {:.02f}, {:.02e}, {:.02e}".format(kata[0], kata[1], kata[2], kata[3], kata[4]))