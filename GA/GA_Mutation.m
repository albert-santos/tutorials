function offspring  = GA_Mutation(offspring,mutation_probability)

[Np,D] = size(offspring); % Tamanho da população e a Quantidade de variáveis

% Percorre a população
for i = 1:Np
    
        j= randi(D); % Gera um número aleatório entre 1 e 200
        r = rand; % Gera um número aleatório entre 0 e 1
        
        if r <  mutation_probability      % Checking for mutation probability
            
            % Adiciona um nível aleatório para realizar a mutação
            offspring(i,j) = randi(2)-1;
        end % Fim da verificação da probabilidade de ocorrer mutação
    
    
end % Fim da população


end % Fim da função