function [number_of_used_cameras] = GA_objective_function (data, camera_location, critical_areas)

%{
A função Objetivo do AG retorna o número de câmeras utilizadas pelo indivíduo da população.
O indíviduo representado pela variável camera_location é formado por um vetor binário de tamanho igual a 
200 (possíveis localizações). camera_location(i) = 1 indica que será instalada uma câmera na posição i. 
camera_location(i) = 0  indica que não será instalada uma câmera na posição i
%}

% Número de possíveis localizações (200)
number_of_camera_locations = size(camera_location, 2);
% Número de áreas críticas (1000)
number_of_critical_areas = size(critical_areas, 2);
% Número de câmeras instaladas
number_of_used_cameras = 0;
% Númerod de posições críticas monitoradas
number_of_critical_areas_monitored = 0;


% Calcula o número de câmeras instaladas de acordo com os valores do
% indivíduo camera_location. De acordo com a localização utilizada é
% possível obter as áreas críticas monitoradas por meio do arquivo "data"
% A variável critical_areas é um vetor binário de tamanho 1000 pois representa as
% áreas críticas devem ser monitoradas.
% critical_areas(i) = 1 indica que a área crítica i está sendo monitorada.
% critical_areas(i) = 0 indica que a área crítica i não está sendo monitorada.
for i = 1:number_of_camera_locations
    
    % Valor do estado selecionado (0 ou 1 / A posição será utlizada ou não)
    state_location = camera_location(i);
    
    % Se o estado for 1 signnifica que uma câmera será utilizada na
    % posição i.
    if state_location == 1
        % Soma o número de câmeras utilizadas
        number_of_used_cameras = number_of_used_cameras + 1;
        % Indica quais áreas críticas serão monitoradas com a camera na
        % posição i
        for j=1:size(data, 2)
            if ~isnan(data(i,j))
                % índice/Número da área crítica monitorada
                area_monitored_index = data(i,j);
                % Muda o estado para 1 indicando que a área crítica será
                % monitorada
                critical_areas(area_monitored_index) = 1;
            end
        end
    end
    
end


% Soma o número de áreas críticas monitoradas
for i=1:number_of_critical_areas
    if critical_areas(i) == 1
        number_of_critical_areas_monitored = number_of_critical_areas_monitored + 1;
    end
end


% A função objetivo recebe valor inf quando o número de áreas críticas monitoradas é diferente de 1000 visto que
% a solução final deve monitorar todas as áreas críticas
if  number_of_critical_areas_monitored ~= 1000
    
    number_of_used_cameras = inf;
end


end
