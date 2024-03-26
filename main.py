from pulp import *
prob = LpProblem("", LpMaximize)
x1 = LpVariable("x1", lowBound=0, cat='Integer')
x2 = LpVariable("x2", lowBound=0, cat='Integer')
x3 = LpVariable("x3", lowBound=0, cat='Integer')
x4 = LpVariable("x4", lowBound=0, cat='Integer')
prob += 3*x1 + 2*x2 + x3 + x4, "Tong"
prob += 6*x1 + 3*x2 + 1.5*x3 + 4*x4 <= 850
prob += 3*x2 + 1.5*x3 + 4*x4 <= 550
prob += 6*x1 + 1.5*x3 + 4*x4 <= 620
prob.solve()
print("x1 =", value(x1))
print("x2 =", value(x2))
print("x3 =", value(x3))
print("x4 =", value(x4))
print("J =", value(prob.objective))





