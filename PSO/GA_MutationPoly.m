function offspring  = GA_MutationPoly(offspring,mutation_probability,number_of_levels, lb,ub)

[Np,D] = size(offspring); % Tamanho da população e a Quantidade de variáveis

% Percorre a população
for i = 1:Np
    
    % Percorre as variáveis da população i
    for j=1:D
        
        r = rand; % Gera um número aleatório entre 0 e 1
        
        if r <  mutation_probability      % Checking for mutation probability
            
            % Adiciona um nível aleatório para realizar a mutação
%             offspring(i,j) = randi(number_of_levels);
              offspring(i,j) = 1;
        end % Fim da verificação da probabilidade de ocorrer mutação
    
    end % Fim das variáveis da população
    
end % Fim da população


end % Fim da função