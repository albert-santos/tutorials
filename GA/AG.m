function  [bestsol, bestfitness] = AG(data, maxIteration, population_size, cross_over_probability, mutation_probability)

%% Inicia AG (Algoritmo Genético)

% maxIteration = 20000; % Número de iterações
% population_size = 100; % Tamanho da população
% cross_over_probability = 0.9; % Probabilidade de ocorrer crossover
% mutation_probability = 0.1; % Probabilidade de ocorrer mutação


f = NaN(population_size, 1);           % Vetor que armazena o valor da função objetivo dos membros da população 
OffspringObj = NaN(population_size, 1);% Vetor que armazena o valor da função objetivo dos membros da offspring 

% Número de possíveis localizações das câmeras que corresponde ao número de variáveis de decisão de cada
% indivíduo (ou seja, o número de colunas de cada indivíduo)
number_of_camera_locations = 200;
% Vetor binário que indica se a área crítica será monitorada ou não
critical_areas = zeros(1, 1000);

% Criando o vetor binário para localizações disponíveis, inicialmente com valores iguais a zero. O índice do vetor representa o ID da localização e valor do vetor
% indica se a localização vai ser utilzada ou não
camera_location = zeros(1,number_of_camera_locations);

%% Cria a população inicial do AG

% Percorre os indivíduos da população
for i=1: population_size
    
    % Percorre as 200 localizações disponíveis
    for j=1:number_of_camera_locations
        
        
        % A matriz camera_location possui dimensôes de: 
        % (population_size x 200)
        % Ou seja, o número de linhas representa os indivíduos da população
        % e o número de colunas representa as 200 possíveis localizações
        % Se camera_location(i,j) = 1, significa que na localização j do
        % indivíduo i será instalada uma câmera
        
        % Atribui 0 ou 1 de forma aleatória na matriz camera_location
        camera_location(i, j) = randi(2)-1;
        
        % O primeiro indíviduo instala câmeras em todas as possíveis
        % localizações. Essa abordagem foi utilizada para inserir um indivíduo com
        % a solução menos eficiente em relação ao monitoramento das áreas
        % críticas
        if i == 1
            camera_location(i, j) = 1;
        end        
    end
end

% População inicial do AG
P = camera_location;

% Avaliando o valor da função objetivo para os membros da população incial
for i=1:population_size
    f(i,:) = GA_objective_function (data, P(i,:), critical_areas);
end


%% Loop Principal do AG

for i=1:maxIteration

    % Utiliza  a função Tournament selection para selecionar os melhores
    % indivíduos da população incial
    MatingPool = GA_Tournament_Selection(f,population_size);        % Performing the tournaments to select the mating pool
    Parent = P(MatingPool,:);                        % Selecting parent solution
    
    % Realiza o crossover da população
    offspring  = GA_Crossover(Parent,cross_over_probability);
    
    % Realiza a mutação da população
    offspring  = GA_Mutation(offspring,mutation_probability);
    
    % Avalia o valor da função objetivo de cada indivíduo da nova população
    % gerada
    for j = 1:population_size
        OffspringObj(j) = GA_objective_function(data, offspring(j,:), critical_areas);     % Evaluating the fitness of the offspring solution
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
    
    % Variável que armazena o histórico do melhor valor da função objetivo
    % para cada iteração do AG. Nesse caso, o valor representa a menor
    % quantidade, em cada iteração, de câmeras utlizada para monitorar todas as 1000 áreas
    % críticas
    fitness_history(i) = f(1);

end

% Armazena a menor quantidade de câmeras necessárias para monitorar as
% áreas críticas
bestfitness = f(1);
% Armazena o vetor binário com as 200 possíveis localizações. O valor 1
% indica na localização foi instalada uma câmera e 0 indica a localização
% não foi utilizada
bestsol = P(1,:);

% Exibe a variável no terminal
% bestsol
% bestfitness


% Plota o gráfico com o histórico da menor quantidade de câmeras necessárias ao
% longo das iterações do AG
figure;
plot(fitness_history,'LineWidth',2);
xlabel('Iterações');
ylabel('Quantidade de Câmeras');
grid on;



 
end