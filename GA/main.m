
clc;
clear;
close all;

% Indica o nome do arquivo
FileName = 'instance.csv';

rng(1);

% Converte o arquivo em uma matriz
data = readmatrix(FileName);

% Parâmetros do Algorítmo Genético
maxIteration = 2000; % Número de iterações
population_size = 10; % Tamanho da população
cross_over_probability = 0.9; % Probabilidade de ocorrer crossover
mutation_probability = 0.3; % Probabilidade de ocorrer mutação

for i=1:20
    tic

    % Chamada do algorítmo genético
    % Retorna a menor quantidade de câmereas utizadas (bestfiness)
    % bem como o vetor binário de tamanho igual a 200 que indica em quais localizações as câmeras foram
    % instaladas(bestsol)
    [bestsol(i,:), bestfitness(i)] = AG(data, maxIteration, population_size, cross_over_probability, mutation_probability);
    
    bestfitness(i)
    
    runtime = toc;

    runtime_in_minutes = runtime/60;

    runtime_in_minutes
    
    
end

mean_fitness = mean(bestfitness);
worst_fitness = max(bestfitness);
best_fitness = min(bestfitness);
std_fitness = std(bestfitness);

save('Resultados/Resultados.mat', 'bestsol', 'bestfitness', 'mean_fitness', 'worst_fitness', 'best_fitness', 'std_fitness');


