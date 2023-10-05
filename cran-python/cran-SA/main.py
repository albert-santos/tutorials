from root import root

# Parâmetros da simulação
total_number_of_users = 200
number_of_small_base_stations = 10
number_of_macro_base_stations = 1

results, base_stations_after_optimized_connection, users  = root(total_number_of_users, number_of_small_base_stations, number_of_macro_base_stations)

print('Conexão finalizada')