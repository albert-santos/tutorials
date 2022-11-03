from calculate_channel import calculate_channel
import numpy as np
from operator import itemgetter

def users_connection_in_the_macro(users, macros):

    number_of_macros = len(macros)
    number_of_users = len(users)

    # Cria as matrizes que armazenam a taxa de dados, cqi e sinr dos usuários em relação às antenas
    # As linhas representam os usuários e as colunas as antenas
    rows, cols = (number_of_users, number_of_macros) # dimensões das matrizes
    data_rate = [[0 for i in range(cols)] for j in range(rows)]
    cqi = [[0 for i in range(cols)] for j in range(rows)]
    sinr = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(0, number_of_users):
        for j in range(0, number_of_macros):
            data_rate[i][j], cqi[i][j], sinr[i][j] = calculate_channel(users[i], macros[j], macros)

    

    # Dimensão da matriz para armazenar os usuários e a quantidade de PRBs que eles precisam
    # Linhas = quantidade de usuários
    # Colunas 1: id do usuário | Coluna 2: Quantidade de PRB exigida por ele
    rows, cols = (number_of_users, 2) 
    number_of_prbs_requested_by_users = [[0 for i in range(cols)] for j in range(rows)]

    # Identificando a quantidade de PRB requisitadas por cadas usuário
    # A prioridade de conexão será primeiro para os usuários que demandam
    # poucos PRB, ou seja, cujo sinal possui maior qualidade
    for i in range(0, number_of_users):

        # A maior taxa de dados que o usuário i conseguiu atingir utilizando 1 PRB
        # data_rate[i] passa todas as colunas da linha i
        max_user_data_rate = np.max(data_rate[i])
        # Calcula a quantidade de PRBs necessárias para atingir a taxa de dados mínima do usuário i
        user_requested_PRB = np.ceil(users[i].required_data_rate/max_user_data_rate)

        # id do usuário
        number_of_prbs_requested_by_users[i][0] = users[i].id
        # quantidade de PRBs necessária
        number_of_prbs_requested_by_users[i][1] = user_requested_PRB

    
    # Organizando em ordem crescente pela quantidade de PRB requisitados de cada usuário
    number_of_prbs_requested_by_users = sorted(number_of_prbs_requested_by_users[1:], key=itemgetter(1))
    
    # Realiza a conexão dos usuários
    for user_id in range(0,number_of_users):
        
        # Variável auxiliar
        helper = 0

        # A conexão inicia pelo usuário que exige a menor quantiade de PRBs
        i = number_of_prbs_requested_by_users(user_id, 1)

        # Verifica se o usuário já não está conectado em alguma base station
        if users[i].user_connected == False:

            while helper == 0:
                max_user_data_rate = np.max(data_rate[i])
                base_station_index = np.argmax(data_rate[i])
                user_requested_PRB = np.ceil(users[i].required_data_rate/max_user_data_rate)

                if macros[base_station_index].remaining_PRB >= user_requested_PRB:
                    b=1




                




    return users, macros