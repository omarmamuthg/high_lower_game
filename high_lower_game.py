# Importación de módulos necesarios
from data import data  # Importa los datos del archivo data.py
import art  # Importa el arte ASCII para mejorar la presentación
import random  # Importa el módulo random para generar números aleatorios
import os  # Importa el módulo os para interactuar con el sistema operativo

# Función para generar un número aleatorio dentro del rango de la lista de datos
def random_data():
    data_random = random.randint(0, len(data) - 1)
    return data_random

# Lista para almacenar los datos que se usan en el juego
dict_data = []

# Función para formatear y seleccionar datos aleatorios únicos del juego
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

    return f"{name}, a {description}, from {country}"  # Retorna una cadena formateada con los datos seleccionados

# Contador para llevar la puntuación del jugador
contador = 0

# Función para comparar las variables A y B y actualizar el juego
def compare_variables(letter):
    global contador
    os.system('cls')  # Limpia la pantalla para una mejor visualización (para sistemas Windows)
    
    followers_numbera = dict_data[0]["follower_count"]
    followers_numberb = dict_data[1]["follower_count"]
    
    # Comparación de los números de seguidores y actualización del juego
    if (followers_numbera > followers_numberb and letter == "A"):
        contador += 1
        del dict_data[1]  # Elimina el dato B de dict_data después de acertar
        print(art.high_lower)  # Imprime arte ASCII
        return f"You're right! Current score: {contador}"
    elif (followers_numberb > followers_numbera and letter == "B"):
        contador += 1
        del dict_data[0]  # Elimina el dato A de dict_data después de acertar
        print(art.high_lower)  # Imprime arte ASCII
        return f"You're right! Current score: {contador}"
    else:
        dict_data.clear()  # Borra todos los datos en dict_data si se responde incorrectamente
        print(art.high_lower)  # Imprime arte ASCII
        return f"Sorry, that's wrong. Final score: {contador}"

# Función para comenzar el juego mostrando las opciones A y B
def start_game():
    a_const = "Compare A:"
    b_const = "Against B:"
    print(art.high_lower)  # Imprime arte ASCII
    data_gameA = data_game_format()  # Obtiene y formatea los datos para A
    print(f"{a_const} {data_gameA}")  # Imprime la opción A
    print(art.vs)  # Imprime arte ASCII de VS
    data_gameB = data_game_format()  # Obtiene y formatea los datos para B
    print(f"{b_const} {data_gameB}")  # Imprime la opción B
    print(dict_data)  # Imprime los datos actuales en dict_data

# Función para mostrar los datos de comparación A
def show_data():
    name = dict_data[0]['name']
    followers = dict_data[0]['follower_count']
    description = dict_data[0]['description']
    country = dict_data[0]['country']
    return f"{name}, a {description}, from {country}"  # Retorna una cadena formateada con los datos de A

# Función para continuar el juego mostrando nuevas comparaciones A y B
def continue_game():
    comparea = show_data()  # Obtiene y muestra los datos de A
    print(f"Compare A: {comparea}")  # Imprime la opción A
    print(art.vs)  # Imprime arte ASCII de VS
    compare2 = data_game_format()  # Obtiene y formatea los datos para B
    print(f"Against B: {compare2}")  # Imprime la opción B
    print(dict_data)  # Imprime los datos actuales en dict_data

# Inicia el juego mostrando la primera ronda de comparaciones
start_game()

# Bucle principal del juego
while True:
    option = input("Who has more followers? Type 'A' or 'B': ").upper()  # Pregunta al jugador por su elección
    print(compare_variables(option))  # Compara la elección del jugador y muestra el resultado
    
    # Si todavía quedan datos en dict_data, continúa el juego
    if len(dict_data) != 0:
        continue_game()  # Muestra las siguientes comparaciones
    else:
        break  # Si no quedan más datos, termina el juego

