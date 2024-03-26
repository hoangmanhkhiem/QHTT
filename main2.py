from pulp import *
_prob = LpProblem("", LpMaximize)
_x1 = LpVariable("x1", lowBound=0, cat='Integer')
_x2 = LpVariable("x2", lowBound=0, cat='Integer')
_x1.lowBound = 100
_prob += 8000*_x1 + 12000*_x2, "Tong"
_prob += 300*_x1 + 500*_x2 <= 200000
_prob += 10000*_x1 + 15000*_x2 <= 8000000
_prob.solve()
print("_x1 =", value(_x1))
print("_x2 =", value(_x2))
print("J =", value(_prob.objective))