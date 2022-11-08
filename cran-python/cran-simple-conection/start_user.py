from user import user # importa a classe user
import random

def start_user(users_maximum_number, x, y):

    # Distribuição dos usuários de acordo com os dados de NY
    user_distribution = [0.90, 0.69, 0.56, 0.48, 0.39, 0.29, 0.20, 0.15, 0.14, 0.17, 0.30, 0.57, 0.87, 0.92, 0.73, 0.61, 0.74, 0.89, 0.85, 0.75, 0.72, 0.81, 0.96, 1]

    # Taxa de dados mínima exigida pelo usuário
    user_required_data_rate = 400 * 1024 #Taxa requerida

    # Lista para armazenar as instâncias dos usuários
    users = []

    # Ciclo correspondente às horas
    for j in range(0, 24):
        # Quantidade de usários de acordo com a distribuição
        total_users_per_hour = int(users_maximum_number * user_distribution[j])

        # Criação de usuários
        for i in range(0, total_users_per_hour):
            new_user = user() # cria um novo usuários
            new_user.id = i # ID do usuário
            # new_user.x = 150 # TESTE
            # new_user.y = 150 # TESTE
            new_user.x = random.random() * x[1] # Posição dos usuários no eixo x
            new_user.y = random.random() * y[1] # Posição dos usuários no eixo y
            new_user.required_data_rate = user_required_data_rate # taxa de dados mínima exigida
            new_user.time = j + 1 # hora a qual o usuário pertence

            users.append(new_user) #adiciona o novo usuário na lista

    return users