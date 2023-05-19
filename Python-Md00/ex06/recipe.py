# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sallorca <sallorca@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/14 15:53:30 by sallorca          #+#    #+#              #
#    Updated: 2023/04/20 11:45:26 by sallorca         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


cookbook = {
    'Sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meals': 'lunch', 
        'prep_time': 10},
    'Cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meals': 'dessert',
        'prep_time': 60},
    'Salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meals': 'lunch',
        'prep_time': 15}
    }

def nombres_receta():
    for nombre in cookbook:
        print(nombre)

def nombre_detalle(nombre):
    if nombre in cookbook:
        print("\nRecipe for", nombre,':')
        print("    Ingredients list:", cookbook[nombre]["ingredients"])
        print("    To be eaten for", cookbook[nombre]["meals"],".")
        print("    Takes", cookbook[nombre]["prep_time"], "minutes of cooking.")
    else:
        print("The recipe is not in the Cookbook")

def nombre_clean(nombre):
    if nombre in cookbook:
        del cookbook[nombre]
        
def add_receta():
    print("Enter a name")
    nombre = input()
    if nombre in cookbook:
        print("The recipe is already exist")
        return False
    Ingredientes = []
    print("Enter ingredients:")
    valor = input()
    while valor != "":
        Ingredientes.append(valor)
        valor = input()
    print("Enter a meal type")
    meals = input() 
    while 42:
        tiempo = input("Enter a preparation time\n")
        try:
            tiempo = int(tiempo)
        except:
            print("Must be an integer")
        else:
            if (tiempo <= 0):
                print("Must be positive time")
            else:
                break
    cookbook.update({nombre:{"ingredients":Ingredientes,"meals": meals, "prep_time":tiempo}})
    return True
    
def list_option():
    print("List of available option:\n   1: Add a recipe\n   2: Delete a recipe\n   3: Print a recipe\n   4: Print the cookbook\n   5: Quit")
    while 42:
        opt = input("\nPlease select an option:\n")
        if opt == '1':
            add_receta()
        elif opt == '2':
            nombre = input("\nPlease enter recipe to delete\n")
            nombre_clean(nombre)
        elif opt == '3':
            nombre = input("\nPlease enter a recipe name to get its details:\n")
            nombre_detalle(nombre)
        elif opt == '4':
            nombres_receta()
        elif opt == '5':
            break
        else:
            print("Sorry, this option does not exist.")
            list_option()
            exit()
    print("Cookbook closed. Goodbye !")   


if __name__=="__main__":
    print("Welcome to Python Cookbook !")
    list_option()
    