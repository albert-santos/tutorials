function offspring  = GA_Crossover(Parent,cross_over_probability)

%{
 O crossover heurístico foi utilizado com um arredondamento no final para obter valoes inteiros.
%}

[Np,D] = size(Parent);                      % Tamanho da população e das variáveis de decisão
indx = randperm(Np);                        % Permutando os número de 1 até Np
Parent = Parent(indx,:);                    % Embaralhando aleatoriamente a solução
offspring = NaN(Np,D);                      % Matriz para armazena as soluções da offspring(nova solução)

for i = 1:Np                              
    
    r = rand;           % Gerando um número aleatório para decidir se o crossover será realizado
    
    if r < cross_over_probability                  % Confere a probabilidade de ocorrer crossover
        
        
        for j=1:D
            if i == Np
                offspring(i,j) = round ( Parent(1,j) + 0.5*( Parent(i,j) - Parent(1,j) ) );
            else
                offspring(i,j) = round ( Parent(i+1,j) + 0.5*( Parent(i,j) - Parent(i+1,j) ) );
            end
            
        end % Fim do loop que percorre as variáveis
        
        
        

    else % Não realiza cross-over
        
        % Nessa caso os valores da offspring serão todos iguais ao do
        % Parent
        for j=1:D
            
            offspring(i,j) = Parent(i,j);  
            
        end % Fim do loop que percorre as variáveis
        
    end % fim da verificação da probabilidade de ocorrer cross-over
end


end % Fim da função
