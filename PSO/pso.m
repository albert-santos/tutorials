
clc;
clear;
close all;

%% Definição do Problema

CostFunction=@(x) Sphere(x);        % Função Objetivo

nVar=10;            % Número de variáveis de decisão

VarSize=[1 nVar];   % Tamanho da matriz com as variáveis de decisão (1 linha x 10 colunas)

VarMin=0;         % Limite mínimo das variáveis
VarMax= 1;         % Limite máximo das variáveis


%% PSO Parameters

MaxIt=1000;      % Número máximo de iterações do PSO

nPop=100;        % Tamanho da população (Tamanho das partículas)

% Parâmetros do PSO
w=0.8;            % Peso de inércia
%wdamp=0.99;  
c1=1.5;         % Fator de aceleração (Parâmetro pessoal)
c2=2.0;         % Fator de aceleração (Parâmetros Global)

% Limite de velocidade
% VelMax=0.1*(VarMax-VarMin);
% VelMin=-VelMax;

% VelMax=20;
% VelMin=-VelMax;

%% Initialization

empty_particle.Position=[];
empty_particle.Cost=[];
empty_particle.Velocity=[];
empty_particle.Best.Position=[];
empty_particle.Best.Cost=[];

particle=repmat(empty_particle,nPop,1);

GlobalBest.Cost=inf;

for i=1:nPop
    
    % Inicializa as posições
    particle(i).Position=unifrnd(VarMin,VarMax,VarSize);
    
    % Inicializa as velocidades
    particle(i).Velocity=zeros(VarSize);
    
    % Avaliação inicial para a partícula i
    particle(i).Cost=CostFunction(particle(i).Position);
    
    % Atualiza o Pbest
    particle(i).Best.Position=particle(i).Position;
    particle(i).Best.Cost=particle(i).Cost;
    
    % Atualiza o Gbest
    if particle(i).Best.Cost<GlobalBest.Cost
        
        GlobalBest=particle(i).Best;
        
    end
    
end

BestCost=zeros(MaxIt,1);

%% PSO Main Loop

for it=1:MaxIt
    
    for i=1:nPop
        
        % Atualiza a velocidade
        particle(i).Velocity = w*particle(i).Velocity ...
            +c1*rand(VarSize).*(particle(i).Best.Position-particle(i).Position) ...
            +c2*rand(VarSize).*(GlobalBest.Position-particle(i).Position);
        
        % Aplica os limites de velocidade
%         particle(i).Velocity = max(particle(i).Velocity,VelMin);
%         particle(i).Velocity = min(particle(i).Velocity,VelMax);
        
        % Atualiza a posição
        particle(i).Position = round(particle(i).Position + particle(i).Velocity);
        
        % Mirror Effect na velocidade
        IsOutside=(particle(i).Position<VarMin | particle(i).Position>VarMax);
        particle(i).Velocity(IsOutside)=-particle(i).Velocity(IsOutside);
        
        % Aplica os limites de posições
        particle(i).Position = max(particle(i).Position,VarMin);
        particle(i).Position = min(particle(i).Position,VarMax);
        
        % Avalia as soluções de acordo com a função objetivo
        particle(i).Cost = CostFunction(particle(i).Position);
        
        % Atualiza o Pbest
        if particle(i).Cost<particle(i).Best.Cost
            
            particle(i).Best.Position=particle(i).Position;
            particle(i).Best.Cost=particle(i).Cost;
            
            % Atualiza o Gbest
            if particle(i).Best.Cost>GlobalBest.Cost
                
                GlobalBest=particle(i).Best;
                
            end
            
        end
        
    end
    
    BestCost(it)=GlobalBest.Cost;
    
    disp(['Iteration ' num2str(it) ': Best Cost = ' num2str(BestCost(it))]);
    
    %w = w*wdamp;
end

BestSol = GlobalBest;

%% Resultados

figure;
%plot(BestCost,'LineWidth',2);
semilogy(BestCost,'LineWidth',2);
xlabel('Iteration');
ylabel('Best Cost');
grid on;
