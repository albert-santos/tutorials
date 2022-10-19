function [total_power] = GA_objective_function (new_solution, power_levels, users, Macros, Smalls)

number_of_rrhs = size(new_solution, 2);
total_power = 0;

[saida, S1] = connection_with_the_new_power_values(new_solution, power_levels, users, Macros, Smalls);


% Se o número de usuários não conectados for igual a zero
if  saida(1,2) == 0
    
    % Calcula o consumo de energia total
    for i = 1:number_of_rrhs
    
        % índice do nível selecionado (Ex: 1, 2, 3)
        assigned_power_level = new_solution(i);
    
        % Valor do nível seleciondado (Ex: 0dBm, 20dBm, 33dbm)
        assigned_power_value = power_levels(assigned_power_level);
        
        % Somar apenas se a potência for diferente de zero
        if assigned_power_value ~= 0
            % Transformando a potência de dBm para watts(W)
            assigneg_power_level_in_watts =  10^((assigned_power_value - 30)/10);
       
            % Somando o valor de potência total
            total_power = total_power + assigneg_power_level_in_watts + 130;
        else
            total_power = total_power + 75;
        end
        
    end
    
    
else
    total_power = inf;
end


end
    