from calculate_channel import calculate_channel

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
    




    return users, macros