from base_station import base_station

def start_macro(macro_cells_number, x, y):

    # Coordenadas da macro cell
    x_macro_position = []
    y_macro_position = []

    # Adiciona os valores. Nesse caso a macro cell ficará localizada no centro do cenário
    # Essa abordagem é realizada quando consideramos apenas uma macro base station
    x_macro_position.append(x[1] / 2)
    y_macro_position.append(y[1] / 2)

    # Lista para armazenar as instâncias das macro cells
    macro_cells = []

    # Contador de macros
    counter = 1

    for i in range(0, macro_cells_number):
        for j in range(0, macro_cells_number):
            
            new_macro_cell = base_station() # Instancia a macro base station
            new_macro_cell.id = counter # ID da macro
            new_macro_cell.x = x_macro_position[i] # Posição no eixo x
            new_macro_cell.y = y_macro_position[j] # Posição no eixo y
            new_macro_cell.transmit_power = 49 # Potência em dBm
            new_macro_cell.frequency = 1.8e9 # Frequência em Ghz
            new_macro_cell.base_station_connected = True # Indica se a macro está ligada ou não
            new_macro_cell.total_PRB = 100 # Número total de PRBs
            new_macro_cell.remaining_PRB = 100 # Número de PRBs disponíveis
            new_macro_cell.bandwidth = 20e6 # Largura de banda em Mhz
            new_macro_cell.coverage_area = 1000 # Área de cobertura da base station
            new_macro_cell.height = 40 # altura da base station

            macro_cells.append(new_macro_cell) # Adiciona a macro base station criada na lista de macros
 
            counter = counter + 1 # Incrementa a variável contadora

    return macro_cells