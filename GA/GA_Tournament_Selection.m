function MatingPool = GA_Tournament_Selection(f,Np)
%{
Tournament selection: Cada indivíduo participa exatamente duas vezes.
Ocorre uma competição entre os indivíduos da população. Esta competição é
feita entre pares de indivíduos. O indivíduo que obtiver o menor valor da função objetivo
substitui o adversário na população.
%}


MatingPool = NaN(Np,1);                     % Vetor para armaznar o índice de parents
indx = randperm(Np);                        % Randomicamente embaralhando o índice dos membros da população

for i = 1 : Np-1                            % Percorre até o penúltimo indivíduo da população 
    Candidate = [ indx(i) indx(i+1)];       % Seleciona um par de indivíduos
    CandidateObj = f(Candidate);
    [~, ind] = min(CandidateObj);           % Seleciona o vencedor baseado no menor valor da função objetivo
    MatingPool(i) = Candidate(ind);         % Armazena o índice do vencedor
end

% Tournament selection entre o último e o primeiro indivíduo
Candidate = [ indx(Np) indx(1)];            
CandidateObj = f(Candidate);
[~, ind] = min(CandidateObj);
MatingPool(Np) = Candidate(ind);
