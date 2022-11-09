import random
import copy
import math
from turns_on_only_selected_base_stations import turns_on_only_selected_base_stations

def SA_create_neighbour(base_station_organization):

    base_station_organization = copy.deepcopy(base_station_organization)

    # Número de base stations
    number_of_base_stations = len(base_station_organization[:])
    
    # índice da primeira base station selecionada
    index_a = random.randint(0, number_of_base_stations-1)
    # índice da segunda base station selecionada
    index_b = random.randint(0, number_of_base_stations-1)

    # Variável que armazenará a nova organização das base stations
    new_base_station_organization = copy.deepcopy(base_station_organization)
    # Mudando a ordem das duas base stations selecionadas
    new_base_station_organization[index_a][:] = base_station_organization[index_b][:]
    new_base_station_organization[index_b][:] = base_station_organization[index_a][:]

    return new_base_station_organization


def SA_selection_function(base_station_organization, number_of_activated_base_stations, number_of_users):

    connected_users = 0

    for i in range(0, number_of_activated_base_stations):
        connected_users = connected_users + base_station_organization[i][1]

    cost = number_of_users - connected_users

    return cost


def SA_algorithm(base_station_organization, users, smalls, macros):

    # Parâmetros iniciais do SA
    initial_temperature = 1000 # Temperatura inicial
    temperature = initial_temperature # Temperatura ao longo das iterações
    alpha = 0.99 # Fator de diminuição da temperatura
    max_iteration = 1000 # Número máximo de iterações do SA
    best_cost = math.inf # Melhor custo. O custo equivale a quantidade de usuários não conectados
    fitness_history =  [] # histórico do custo ao longo das iterações

    # A melhor organização das base stations
    best_base_station_organization = copy.deepcopy(base_station_organization)
    # Número de smalls
    number_of_smalls = len(smalls)
    # Número de usuários
    number_of_users = len(users)

    # Ciclo que hábilita a quantidade de small cells que podem ser ligadas. incrementado de 2 em 2
    for i in range(0, number_of_smalls, 2):
        # Ciclo principal do SA
        for j in range(0, max_iteration):

            # Adiciona o custo atual no histórico
            fitness_history.append(best_cost) 

            # Gera uma nova organização
            new_base_station_organization = SA_create_neighbour(best_base_station_organization)
            # Calcula o custo da nova organização
            new_cost = SA_selection_function(new_base_station_organization, i, number_of_users)

            # Diferença entre o custo da nova organização e a atual melhor organização
            Delta = new_cost - best_cost

            if Delta < 0:
                best_base_station_organization = copy.deepcopy(new_base_station_organization)
                best_cost = new_cost

            else:
                p = math.exp(-Delta/temperature)
                if random.random() <= p:
                    best_base_station_organization = copy.deepcopy(new_base_station_organization)
                    best_cost = new_cost

            temperature = temperature*alpha

        
        # Conecta os usuários utilizando somente as small cells base station selecionadas
        results, smalls_after_connetion = turns_on_only_selected_base_stations(i, users, best_base_station_organization, macros, smalls)

        # Restrição para os desligamentos das small cells base stations
        if results[1] < (number_of_smalls*0.001) or i == number_of_smalls:
            break


    return results, smalls_after_connetion

     

    

