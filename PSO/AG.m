function [saida, number_of_activated_rrhs, S1, total_power, UE] = AG(V21, users, Smalls, Macros)


%% Inicia a otimização utilizando o AG (Algoritmo Genético)

population_size = 10; % Tamanho da população

cross_over_probability = 0.8;
mutation_probability = 0.2;

% Parâmetros herdados do AG mas não utilizados nessa implementação
lb = 1;
ub = 4;


f = NaN(population_size, 1);                                 % Vector to store the fitness function value of the population members
OffspringObj = NaN(population_size, 1);                      % Vector to store the fitness function value of the offspring members

% Número de RRHs que corresponde ao número de variáveis de decisão de cada
% indivíduo (simplificando: o número de colunas de cada indivíduo)
number_of_rrhs = length(Smalls);
% Níveis de potência que as RRHs podem assumir
power_levels = [0, 20, 24, 33];

% Criando o vetor das RRHs, inicialmente com valores iguais a zero. O índice do vetor representa o ID da RRH e valor do vetor
% representa o nível de potência que a RRH possui
rrh_levels = zeros(1,number_of_rrhs);


% Atribuindo níveis aleatórios para cada uma das RRHs para a população
% incial do GA
for i=1: population_size
    for j=1:number_of_rrhs
    
        %randi gera números aleatórios entre 1 e 3
        % 1 corresponde ao nível power_levels(1) = 0 dBm
        % 2 corresponde ao nível power_levels(2) = 20 dBm
        % 3 corresponde ao nível power_levels(3) = 33 dBm
        switch (i)
            
            % O primeiro membro da população inicial possui todos os níveis iguais a 1 (0 dBm)
            case 1
                rrh_levels(i,j) = 1;
                
            case 2
                rrh_levels(i,j) = 2;
                                
            case 3
                rrh_levels(i,j) = 3;
                
            case 4
                rrh_levels(i,j) = 4;
%                 
%             case 5
%                 rrh_levels(i,j) = 5;
%                 
%             case 6
%                 rrh_levels(i,j) = 6;
                
%             case 7
%                 rrh_levels(i,j) = 7;
            otherwise
                % O restante é aleatório
                rrh_levels(i, j) = randi(length(power_levels));
        end
        
    end
end

P = rrh_levels;

% Avaliando o valor da função objetivo para os membros da população incial
for i=1:population_size
    
    f(i,:) = GA_objective_function (P(i,:), power_levels, users, Macros, Smalls);
end

% Número de iterações
maxIteration = 800;

for i=1:maxIteration

    % Tournament selection
    MatingPool = GA_Tournament_Selection(f,population_size);        % Performing the tournaments to select the mating pool
    Parent = P(MatingPool,:);                        % Selecting parent solution
    
    % Crossover
    offspring  = GA_CrossoverSBX(Parent,cross_over_probability, lb,ub);
    
    % Mutation 
    offspring  = GA_MutationPoly(offspring,mutation_probability,length(power_levels), lb,ub);
    
    for j = 1:population_size
        OffspringObj(j) = GA_objective_function(offspring(j,:), power_levels, users, Macros, Smalls);     % Evaluating the fitness of the offspring solution
    end
    
    % Cria uma matriz com a população incial mais a nova população
    % A nova população é adicionada abaixo da população inicial.
    % Dessa forma, o número de linhas da matriz resultante (CombinedPopulation)
    % será igual a duas vezes o número de linas da matriz da população incial 
    CombinedPopulation = [P; offspring];
    
    % Os valores da função objetivo da população incial e da nova população são
    % combinados da mesma forma citada acima
    % Além disso ocorre a ordenação do vetor resultante
    [f,ind] = sort([f;OffspringObj]);               
    
    % Obtém os valores da função objetivo dos melhores indivíduos
    f = f(1:population_size);
    % Obtém os melhores indivíduos
    P = CombinedPopulation(ind(1:population_size),:);  


end
bestfitness = f(1);
bestsol = P(1,:);

% bestfitness
% bestsol




%% Realiza a conexão utilizando a melhor solução

[saida, S1, UE] = connection_with_the_new_power_values(bestsol, power_levels, users, Macros, Smalls);
saida(1,9)

%% Conta a quantidade de RRHs em cada nível e a quantidade de RHHs ligadas

number_of_rrhs_level_1 = 0;
number_of_rrhs_level_2 = 0;
number_of_rrhs_level_3 = 0;
number_of_rrhs_level_4 = 0;
number_of_rrhs_level_5 = 0;
number_of_rrhs_level_6 = 0;
number_of_rrhs_level_7 = 0;

for i=1:number_of_rrhs
    
    switch(bestsol(i))
        
        case 1
            number_of_rrhs_level_1 = number_of_rrhs_level_1 + 1;
        case 2
            number_of_rrhs_level_2 = number_of_rrhs_level_2 + 1;
        case 3
            number_of_rrhs_level_3 = number_of_rrhs_level_3 + 1;
        case 4
            number_of_rrhs_level_4 = number_of_rrhs_level_4 + 1;
        case 5
            number_of_rrhs_level_5 = number_of_rrhs_level_5 + 1;
        case 6
            number_of_rrhs_level_6 = number_of_rrhs_level_6 + 1;
        case 7
            number_of_rrhs_level_7 = number_of_rrhs_level_7 + 1;
            
    end
    
      
end

total_power = bestfitness;
number_of_activated_rrhs  = number_of_rrhs - number_of_rrhs_level_1;

fprintf('RRHs com nível 1: %i \n', number_of_rrhs_level_1);
fprintf('RRHs com nível 2: %i \n', number_of_rrhs_level_2);
fprintf('RRHs com nível 3: %i \n', number_of_rrhs_level_3);
fprintf('RRHs com nível 4: %i \n', number_of_rrhs_level_4);
% fprintf('RRHs com nível 5: %i \n', number_of_rrhs_level_5);
% fprintf('RRHs com nível 6: %i \n', number_of_rrhs_level_6);
% fprintf('RRHs com nível 7: %i \n\n', number_of_rrhs_level_7);

fprintf('RRHs ligadas: %i \n', number_of_activated_rrhs);
fprintf('RRHs desligadas: %i \n\n', number_of_rrhs_level_1);

fprintf('Potência total = %fW \n\n', total_power);
 


end