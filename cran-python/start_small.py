from base_station import base_station
import numpy as np

def start_small(small_cells_number, x, y):
    
    # Posições das antenas entre Xmin-Xmax e Ymin-Ymax
    # Linspace retorna números com espaçamento uniforme em um intervalo especificado. 
    x_positions = np.linspace(x[0], x[1], small_cells_number)
    y_positions = np.linspace(y[0], y[1], small_cells_number)

    # Lista para armazenar as instâncias das small cells base stations
    small_cells = []

    # Contador de small cell
    counter = 0

    for i in range(0, small_cells_number):
        for j in range(0, small_cells_number):

            new_small_cell = base_station()
            new_small_cell.id = counter # Id do usuário
            new_small_cell.x = x_positions[i] # Posição no eixo x
            new_small_cell.y = y_positions[j] # Posição no eixo y
            new_small_cell.transmit_power = 32 # Potência em dBm
            new_small_cell.frequency = 2.6e9 # Frequência em Ghz
            new_small_cell.base_station_connected = True # Se a base station está ligada ou não
            new_small_cell.total_PRB = 50 # Número total de PRBs
            new_small_cell.remaining_PRB = 50 # Número de PRBs disponíveis
            new_small_cell.bandwidth = 10e6 # Largura de banda em Mhz
            new_small_cell.coverage_area = 150 # Área de cobertura
            new_small_cell.height = 6 # Altura da base statino

            small_cells.append(new_small_cell) # Adiciona a small cell base station criada na lista de small cells

            counter = counter + 1 # Incrementa a variável contadora

    return small_cells

