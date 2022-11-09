from users_connection_in_the_macro import users_connection_in_the_macro
from users_connection_in_the_small import users_connection_in_the_small
from calculate_results import calculate_results
import copy

def turns_on_only_selected_base_stations(number_of_activated_base_stations, users, best_base_station_organization, macros, smalls):
    
    users = copy.deepcopy(users)
    best_base_station_organization = copy.deepcopy(best_base_station_organization)
    macros = copy.deepcopy(macros)
    smalls = copy.deepcopy(smalls)

    # Número de small cell base stations
    number_of_smalls = len(smalls)

    # Desliga todas as small cell base stations
    for i in range(0, number_of_smalls):
        smalls[i].base_station_connected = False

    # Conecta as N primeiras (number_of_activated_base_stations) small cells já organizadas pelo algoritmo de otimização
    for j in range(0, number_of_activated_base_stations):
        base_station_id = best_base_station_organization[j][0]
        smalls[base_station_id].base_station_connected = True


    # -------Realiza a conexão após os desligamentos-------

    # Conexão dos usuários na macro
    users_after_connection_in_macro, macros_after_connetion = users_connection_in_the_macro(users, macros)
    
    # Conexão dos usuários nas smalls
    users_after_connection_in_small_and_macro, smalls_after_connetion = users_connection_in_the_small(users_after_connection_in_macro, smalls)
    
    results = calculate_results(users_after_connection_in_small_and_macro, smalls_after_connetion)

    return results, smalls_after_connetion