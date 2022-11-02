from base_station import base_station
import numpy as np

def start_small(small_cells_number, x, y):
    
    # Posições das antenas entre Xmin-Xmax e Ymin-Ymax
    x_positions = np.linspace(x[0], x[1], small_cells_number)
    y_positions = np.linspace(y[0], y[1], small_cells_number)

    print(x_positions)
    print(y_positions)

    # Lista para armazenar as instâncias das small cells
    small_cells = []

    # Contador de small cell
    counter = 1

    for i in range(0, small_cells_number):
        for j in range(0, small_cells_number):

            new_small_cell = base_station()
            new_small_cell.id = counter
            new_small_cell.x = x_positions[i]
            new_small_cell.y = y_positions[j]
            new_small_cell.transmit_power = 32 # Potência em dBm
            new_small_cell.frequency = 2.6e9 # Frequência em Ghz
            new_small_cell.base_station_connected = True
            new_small_cell.total_PRB = 50
            new_small_cell.remaining_PRB = 50
            new_small_cell.bandwidth = 10e6 # Largura de banda em Mhz
            new_small_cell.coverage_area = 150
            new_small_cell.height = 6

            small_cells.append(new_small_cell)

            counter = counter + 1

    return small_cells


# small_cells = start_small(10, [0, 500], [0, 500])
# print(len(small_cells))
# small1 = small_cells[0]
# print(small1.id)

# small2 = small_cells[9]
# print(small2.id)

# print('fim')

