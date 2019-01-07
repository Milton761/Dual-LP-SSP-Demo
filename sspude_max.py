from pulp import *

SSP = LpProblem("SSP01", LpMaximize)


S0a0 = LpVariable("S0a0", 0)
S0a1 = LpVariable("S0a1", 0)
S1a0 = LpVariable("S1a0", 0)
S2a1 = LpVariable("S2a1", 0)
D2a1 = LpVariable("D2a1", 0)
D3a1 = LpVariable("D3a1", 0)

OUT_S0 = LpVariable("OUT_S0",0)
OUT_S1 = LpVariable("OUT_S1",0)
OUT_S2 = LpVariable("OUT_S2",0)
OUT_Sg = LpVariable("OUT_Sg",0)
OUT_D1 = LpVariable("OUT_D1",0)
OUT_D2 = LpVariable("OUT_D2",0)
OUT_D3 = LpVariable("OUT_D3",0)

IN_S0 = LpVariable("IN_S0",0)
IN_S1 = LpVariable("IN_S1",0)
IN_S2 = LpVariable("IN_S2",0)
IN_Sg = LpVariable("IN_Sg",0)
IN_D1 = LpVariable("IN_D1",0)
IN_D2 = LpVariable("IN_D2",0)
IN_D3 = LpVariable("IN_D3",0)

#Objective

SSP += IN_Sg

#C1
#C2

SSP += IN_S0 == S2a1*0.25 + S1a0*0.5
SSP += IN_S1 == S0a0*0.5
SSP += IN_S2 == S0a1
SSP += IN_Sg == S1a0*0.5 + S2a1*0.25
SSP += IN_D1 == S0a0*0.5
SSP += IN_D2 == S2a1*0.5 + D3a1
SSP += IN_D3 == D2a1

#C3

SSP += OUT_S0 == S0a0 + S0a1 
SSP += OUT_S1 == S1a0  
SSP += OUT_S2 == S2a1
SSP += OUT_D2 == D2a1 
SSP += OUT_D3 == D3a1

#C7
#SSP += OUT_S0 - IN_S0 == 0
SSP += OUT_S1 - IN_S1 == 0
SSP += OUT_S2 - IN_S2 == 0 
#SSP += OUT_Sg - IN_Sg == 0
SSP += OUT_D1 - IN_D1 == 0
SSP += OUT_D2 - IN_D2 == 0
SSP += OUT_D3 - IN_D3 == 0

#C8

SSP += OUT_S0 - IN_S0 == 1

GLPK().solve(SSP)

# Solution
for v in SSP.variables():
	print(v.name, "=", v.varValue)

print("objective=", value(SSP.objective) )
