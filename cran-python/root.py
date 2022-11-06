from start_scenario import start_scenario
from users_connection_in_the_macro import users_connection_in_the_macro
from users_connection_in_the_small import users_connection_in_the_small

def root(users_maximum_number, small_cells_number, macro_cells_number):
    
    # Criação do cenário
    users, smalls, macros = start_scenario(users_maximum_number, small_cells_number, macro_cells_number)

    total_users_created = len(users)
    # Lista que armazenará os usários de cada hora
    total_users_per_hour = []

    for j in range(0, 23):
        counter = 1
        for k in range(0, total_users_created):
            user_hour = users[k].time
            if  user_hour == j + 1:
                total_users_per_hour.append(users[k])
                counter = counter + 1


        # print(len(total_users_per_hour))
        # total_users_per_hour = []

        # Conexão dos usuários na macro base station
        users_after_connection_in_macro, macros_after_connetion = users_connection_in_the_macro(total_users_per_hour, macros)
        # Conexão dos usuários na small base station
        users_after_connection_in_small, smalls_after_connection = users_connection_in_the_small(users_after_connection_in_macro, smalls)
        # Calcula a quantidade e taxa de usuários em cada small base station
        base_station_users_and_throughputs = calculate_base_station_users_and_throughputs()




root(110, 10, 1)