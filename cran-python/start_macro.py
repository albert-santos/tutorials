from base_station import base_station

def start_macro(macro_cells_number, x, y):

    # Coordenadas da macro cell
    x_macro_position = []
    y_macro_position = []
    # Adiciona os valores na lista. Nesse caso ficará localizada no centro do cenário
    x_macro_position.append(x[1] / 2)
    y_macro_position.append(y[1] / 2)

    # Lista para armazenar as instâncias das macro cells
    macro_cells = []

    # Contador de macros
    counter = 1

    for i in range(0, macro_cells_number):
        for j in range(0, macro_cells_number):
            
            new_macro_cell = base_station()
            new_macro_cell.id = counter
            new_macro_cell.x = x_macro_position[i]
            new_macro_cell.y = y_macro_position[j]
            new_macro_cell.transmit_power = 49 # Potência em dBm
            new_macro_cell.frequency = 1.8e9 # Frequência em Ghz
            new_macro_cell.base_station_connected = True
            new_macro_cell.total_PRB = 100
            new_macro_cell.remaining_PRB = 100
            new_macro_cell.bandwidth = 20e6 # Largura de banda em Mhz
            new_macro_cell.coverage_area = 1000
            new_macro_cell.height = 40

            macro_cells.append(new_macro_cell)

            counter = counter + 1

    return macro_cells


# macro_cells = start_macro(1, [0, 500], [0, 500])
# print(len(macro_cells))
# macro1 = macro_cells[0]
# print(macro1.id)
# print(macro1.height)

# print('fim')