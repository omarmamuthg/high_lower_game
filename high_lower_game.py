from data import data
import art
import random
import os

def random_data():
    data_random=random.randint(0,len(data) - 1)
    return data_random

dict_data=[]
def data_game_format():
    while True:  # Bucle para intentar encontrar un nombre único
        random_number = random_data()
        name = data[random_number]['name']
        followers = data[random_number]['follower_count']
        description = data[random_number]['description']
        country = data[random_number]['country']

        # Verificar si el nombre ya está en dict_data
        name_exists = False
        for d in dict_data:
            if d['name'] == name:
                name_exists = True
                break  # Si se encuentra una coincidencia, salir del bucle

        if not name_exists:  # Si no se encontró el nombre en dict_data
            dict_data.append({
                "name": name,
                'follower_count': followers,
                "description": description,
                "country": country
            })
        break  # Añadir el nuevo dato y salir del bucle

    return f"{name}, a {description}, from {country}"


contador=0

def compare_variables(letter):
    global contador
    os.system('cls')
    followers_numbera=dict_data[0]["follower_count"]
    followers_numberb=dict_data[1]["follower_count"]
    if (followers_numbera>followers_numberb and letter == "A"):
        contador+=1
        del dict_data[1]
        print(art.high_lower)
        return f"You're right! current score {contador}"
    elif (followers_numberb>followers_numbera and letter =="B"):
        contador+=1
        del dict_data[0]
        print(art.high_lower)
        return f"You're right! current score {contador}"
    else:
        dict_data.clear()
        print(art.high_lower)
        return f"sorry that's wrong. FInal score {contador}"

def start_game():
    a_const="Compare A:"
    b_const="Against B:"
    print(art.high_lower)
    data_gameA=data_game_format()
    print(f"{a_const} {data_gameA}")
    print(art.vs)
    data_gameB=data_game_format()
    print(f"{b_const} {data_gameB}")
    print(dict_data)

def show_data():
    name=dict_data[0]['name']
    followers=dict_data[0]['follower_count']
    description= dict_data[0]['description']
    country=dict_data[0]['country']
    return f"{name}, a {description}, from {country}"

def continue_game():
    comparea=show_data()
    print(f"Compare A: {comparea}")
    print(art.vs)
    compare2=data_game_format()
    print(f"Against B: {compare2}")
    print(dict_data)




start_game()
while True:
    option= input("Who has more followers? Type 'A' or 'B': ").upper()
    print(compare_variables(option))
    if len(dict_data)!=0:
        continue_game()
    else:
        break
