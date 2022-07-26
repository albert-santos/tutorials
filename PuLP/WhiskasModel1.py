"""
The Simplified Whiskas Model Python Formulation for the PuLP Modeller

Authors: Antony Phillips, Dr Stuart Mitchell  2007
"""

# Import PuLP modeler functions
from pulp import *

# Create the 'problem ' variable to contain the problem data
problem = LpProblem("The_Whiskas_Problem", LpMinimize)

# The 2 variables Beef and Chicken are created with a lower limit of zero
x1 = LpVariable("ChickenPercent", lowBound=0)
x2 = LpVariable("BeefPercent", lowBound=0)

# The objective function is added to 'problem' first
problem += 0.013 * x1 + 0.008 * x2, "Total Cost of Ingredients per can"

# The five constraints are entered
problem += x1 + x2 == 100, "PercentagesSum"
problem += 0.1 * x1 + 0.2 * x2 >= 8.0, "ProteinRequirement"
problem += 0.08 * x1 + 0.1 * x2 >= 6.0, "FatRequirement"
problem += 0.001 * x1 + 0.005 * x2 <= 2.0, "FibreRequirement"
problem += 0.002 * x1 + 0.005 * x2 <= 0.4, "SaltRequirement"

# The problem data is written to an .lp file
problem.writeLP("WhiskasModel.lp")

# The problem is solved using PuLP's choice of Solver
problem.solve()

# The status of the solution is printed to the screen
print("Status: ", LpStatus[problem.status])

# Each of the variables is printed with it's resolved optimum value
for v in problem.variables():
        print(v.name, " = ", v.varValue)

# The optimised objective function value is printed to the screen
print("Total Cost of Ingredients per can = ", value(problem.objective))

