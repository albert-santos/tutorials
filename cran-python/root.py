from start_scenario import start_scenario
from users_connection_in_the_macro import users_connection_in_the_macro
from users_connection_in_the_small import users_connection_in_the_small
from calculate_base_station_users_and_throughputs import calculate_base_station_users_and_throughputs
from calculate_results import calculate_results
import copy

def root(users_maximum_number, small_cells_number, macro_cells_number):

    # Criação do cenário
    users, smalls, macros = start_scenario(users_maximum_number, small_cells_number, macro_cells_number)

    total_users_created = len(users)
    # Lista que armazenará os usários de cada hora
    total_users_per_hour = []

    # Matriz que armazena os resultados para os 24 períodos
    rows, cols = (24, 10) # dimensões das matrizes
    results = [[0 for i in range(cols)] for j in range(rows)]

    for j in range(0, 23):
        counter = 1
        for k in range(0, total_users_created):
            user_hour = users[k].time
            if  user_hour == j + 1:
                total_users_per_hour.append(users[k])
                counter = counter + 1

        # É necessário fazer uma cópia para não alterar os objetos criados no start_scenario
        # Dessa forma cada período (0-23) utilza smalls e macros que não realizaram nenhuma conexão
        # Caso não fosse feita essa cópia, as small e as macros manteriam a conexão dos usuários do período anterior 
        macros_copy = copy.deepcopy(macros)
        smalls_copy = copy.deepcopy(smalls)

        # Conexão dos usuários na macro base station
        users_after_connection_in_macro, macros_after_connetion = users_connection_in_the_macro(total_users_per_hour, macros_copy)
        # Conexão dos usuários na small base station
        users_after_connection_in_small, smalls_after_connection = users_connection_in_the_small(users_after_connection_in_macro, smalls_copy)
        # Calcula a quantidade e taxa de usuários em cada small base station
        base_station_users_and_throughputs = calculate_base_station_users_and_throughputs(smalls_after_connection, users_after_connection_in_small)

        # Calcula os resultados
        results[j][:]= calculate_results(users_after_connection_in_small, smalls_after_connection)

        total_users_per_hour = []

    return results 