# ﻿

# Simulated Annealing Algorithm
# Objective function f(x), x = (x1,...,xp)
# Initialize initial temperature To and initial guess x(0)
# Set final temperature Tf and max number of iterations N 

# while (T>Tf and n <N)


# Move randomly to new locations: xn+1 = n + (random walk) Calculate Af=fn+1(n+1)- fn(n)
# Accept the new solution if better
# if not improved
# Generate a random number r
# Accept if p= exp(-Aƒ/T] > r
# end if
# Update the best x and f
# n=n+1
# Define cooling schedule T→ aT, (0 < a <1)
# end while

import math
import random

# Defina a função de Rosenbrock
def rosenbrock(x1, x2):
    return 100*(x2 - x1**2)**2 + (1 - x1)**2

# Defina a função objetivo f(x) para o Simulated Annealing
def objective_function(x):
    return rosenbrock(x[0], x[1])

# Implementação do Simulated Annealing
def simulated_annealing(objective_function, initial_guess, initial_temperature, final_temperature, max_iterations):
    x_best = initial_guess
    f_best = objective_function(x_best)
    T = initial_temperature
    n = 0

    while T > final_temperature and n < max_iterations:
        x_new = [xi + random.uniform(-1, 1) for xi in x_best]  # Gera um novo ponto aleatório
        f_new = objective_function(x_new)
        delta_f = f_new - f_best

        if delta_f < 0 or random.random() < math.exp(-delta_f / T):
            x_best = x_new
            f_best = f_new

        T *= 0.99  # Atualiza a temperatura (aqui a = 0.95)

        n += 1

    return x_best, f_best

# Parâmetros do algoritmo
initial_guess = [10.0, 10.0]  # Valor inicial para x1 e x2
initial_temperature = 1000.0
final_temperature = 0.1
max_iterations = 10000

# Executa o Simulated Annealing
best_x, best_f = simulated_annealing(objective_function, initial_guess, initial_temperature, final_temperature, max_iterations)

print(f"Melhor solução encontrada: x = {best_x}, f(x) = {best_f}")
