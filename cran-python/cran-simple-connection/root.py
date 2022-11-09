from start_scenario import start_scenario
from users_connection_in_the_macro import users_connection_in_the_macro
from users_connection_in_the_small import users_connection_in_the_small
from calculate_base_station_users_and_throughputs import calculate_base_station_users_and_throughputs
from calculate_results import calculate_results
import copy

"""
    Função que retorna a saída com os resultados obtidos da modelagem. Os resultados são armazenados em uma matriz (24x10)
    As linhas representam as horas.
    As colunas representam o seguinte:
        1 = Usuários conectados
        2 = Usuários não conectados
        3 = Média taxa de dados dos usuários (Geral)
        4 = Taxa de dados mínima obtidada pelos usuários (Geral)
        5 = Taxa de dados máxima obtidada pelos usuários (Geral)
        6 = Média taxa de dados dos usuários (somente nas small base stations)
        7 = Taxa de dados mínima obtidada pelos usuários (somente nas small base stations)
        8 = Taxa de dados máxima obtidada pelos usuários (somente nas small base stations)
        9 = Small cells ligadas
        10 = Usuários conectados (somente nas small cells base stations)

"""

def root(users_maximum_number, small_cells_number, macro_cells_number):

    # Criação do cenário
    users, smalls, macros = start_scenario(users_maximum_number, small_cells_number, macro_cells_number)

    # Número total de usuários considerando todas as horas
    total_users_created = len(users)
    # Lista que armazenará os usários de uma hora específica
    total_users_per_hour = []

    # Matriz que armazena os resultados para os 24 períodos
    rows, cols = (24, 10) # dimensões das matrizes
    results = [[0 for i in range(cols)] for j in range(rows)]

    # Ciclo correspondente aos 24 períodos do dia
    for j in range(0, 24):

        # Percorre todos os usuários considerando todas as horas
        for k in range(0, total_users_created):
            # hora a qual o usuário pertence
            user_hour = users[k].time
            # Separa os usuários de acordo com a hora j
            if  user_hour == j + 1:
                # Lista que armazena todos os usuários da hora j
                total_users_per_hour.append(users[k])
                

        # É necessário fazer uma cópia para não alterar os objetos criados no start_scenario
        # Dessa forma cada período (0-23) utilza smalls e macros que não realizaram nenhuma conexão
        # Caso não fosse feita essa cópia, as small e as macros manteriam a conexão dos usuários do período anterior 
        macros_copy = copy.deepcopy(macros)
        smalls_copy = copy.deepcopy(smalls)

        # Conexão dos usuários na macro base station
        users_after_connection_in_macro, macros_after_connetion = users_connection_in_the_macro(total_users_per_hour, macros_copy)
        # Conexão dos usuários na small base station
        users_after_connection_in_small_and_macro, smalls_after_connection = users_connection_in_the_small(users_after_connection_in_macro, smalls_copy)
        # Calcula a quantidade e taxa de usuários em cada small base station
        base_station_users_and_throughputs = calculate_base_station_users_and_throughputs(smalls_after_connection, users_after_connection_in_small_and_macro)

        # Calcula os resultados
        results[j][:]= calculate_results(users_after_connection_in_small_and_macro, smalls_after_connection)

        # Limpa a variável para receber os usuários da próxima hora
        total_users_per_hour = []

    return results 