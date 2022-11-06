from user import user # importa a classe user
import random

def start_user(users_maximum_number, x, y):

    # Distribuição dos usuários 
    user_distribution = [0.90, 0.69, 0.56, 0.48, 0.39, 0.29, 0.20, 0.15, 0.14, 0.17, 0.30, 0.57, 0.87, 0.92, 0.73, 0.61, 0.74, 0.89, 0.85, 0.75, 0.72, 0.81, 0.96, 1]

    user_required_data_rate = 400 * 1024 #Taxa requerida

    # Lista para armazenar as instâncias dos usuários
    users = []

    counter = 1

    for j in range(0, 24):
        # Quantidade de usários de acordo com a distribuição
        total_users_per_hour = int(users_maximum_number * user_distribution[j])

        # Criação de usuários
        for i in range(0, total_users_per_hour):
            new_user = user() # cria um novo usuários
            new_user.id = i
            new_user.x = random.random() * x[1]
            new_user.y = random.random() * y[1]
            new_user.required_data_rate = user_required_data_rate
            new_user.time = j + 1 # hora

            users.append(new_user) #adiciona o novo usuário na lista

            counter = counter + 1 # incrementa o número de usuários criados

    return users

# users = start_user(10, [0, 500], [0, 500])
# print(len(users))
# user1 = users[0]
# print(user1.time)

# user2 = users[135]
# print(user2.time)

# print('fim')