# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sallorca <sallorca@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/19 12:44:17 by sallorca          #+#    #+#              #
#    Updated: 2023/04/20 13:44:29 by sallorca         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def guess():
    secret = random.randint(1, 99)
    #print(secret)
    
    terminado = 0
    num_int = 0
    while not terminado:
        print("What's your guess between 1 and 99?")
        number_inp = input('>> ')
        if number_inp == 'exit':
            print("Goodbye!")
            return
        elif (not number_inp.isdigit() or int(number_inp) < 1 or int(number_inp) > 99):
            print("Not the right ussage: enter a number between 1 and 99")
            num_int += 1
            continue
        number = int(number_inp)
        num_int += 1
        if number > secret:
            print("Too high!")
        elif number < secret:
            print("Too low!")
        elif number == secret and secret == 42:
            print("The answer to the ultimate  question of life, the universe and everything is 42.")
            terminado = 1
        elif number == secret and num_int == 1:
            print("Congratulations! You got it on your first try!")
            terminado = 1
        else:
            print("Congratulations, you've got it!")
            print("You won in", num_int, "attempts!")
            terminado = 1
    
if __name__=="__main__":
    print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!\n")
    guess()    
