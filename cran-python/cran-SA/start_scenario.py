from start_user import start_user
from start_small import start_small
from start_macro import start_macro

def start_scenario(users_maximum_number, small_cells_number, macro_cells_number):

    # Eixos dos cenários
    X = [0, 500] #Eixo mínimo e máximo
    Y = [0, 500] #Eixo mínimo e máximo

    # Cria os usuários
    users = start_user(users_maximum_number, X, Y)
    
    # Cria as small cells base stations
    small_cells = start_small(small_cells_number, X, Y)

    # Cria as macro cells base stations
    macro_cells = start_macro(macro_cells_number, X, Y)

    return users, small_cells, macro_cells
