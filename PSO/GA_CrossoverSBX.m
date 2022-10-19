function offspring  = GA_CrossoverSBX(Parent,cross_over_probability,lb,ub)

[Np,D] = size(Parent);                      % Detemining the no. of population and decision variables
indx = randperm(Np);                        % Permutating numbers from 1 to Np
Parent = Parent(indx,:);                    % Randomly shuffling parent solutions
offspring = NaN(Np,D);                      % Matrix to store offspring solutions

for i = 1:Np                              % Selecting parents in pairs for crossover
    
    r = rand;                               % Generating random number to decide if crossover is to be performed
    
    if r < cross_over_probability                               % Checking for crossover probability
        
        % Gera o ponto de cross-over dos pais
        cross_over_point = randi(D);
        
        for j=1:D
            
            
            %             if j < cross_over_point
            %                 % Adicina a primeira parte do novo indivíduo 1 recebida do pai 1
            %                 offspring(i,j) = Parent(i,j);
            %
            %                 % Adicina a primeira parte do novo indivíduo 2 recebida do
            %                 % pai 2
            %                 offspring(i+1,j) = Parent(i+1,j);
            %             else
            %                 % Adicina a segunda parte do novo indivíduo 1 recebida do
            %                 % pai 2
            %                 offspring(i,j) = Parent(i+1,j);
            %
            %                 % Adicina a segunda parte do novo indivíduo 2 recebida do
            %                 % pai 1
            %                 offspring(i+1,j) = Parent(i,j);
            %             end
            %
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
            %             offspring(i,j) = Parent(i,j);
            %             offspring(i+1,j) = Parent(i+1,j);
            
            
        end % Fim do loop que percorre as variáveis
        
    end % fim da verificação da probabilidade de ocorrer cross-over
end


end % Fim da função
