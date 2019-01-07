from pulp import *

SSP = LpProblem("SSP01", LpMinimize)


#declare variables

Aa1 = LpVariable("Aa1",0)
Aa2 = LpVariable("Aa2",0)
Aa3 = LpVariable("Aa3",0)
Bb1 = LpVariable("Bb1",0)
Cc1 = LpVariable("Cc1",0)

OUT_A = LpVariable("OUT_A",0)
OUT_B = LpVariable("OUT_B",0)
OUT_C = LpVariable("OUT_C",0)
OUT_D = LpVariable("OUT_D",0)

IN_A = LpVariable("IN_A",0)
IN_B = LpVariable("IN_B",0)
IN_C = LpVariable("IN_C",0)
IN_D = LpVariable("IN_D",0)


#Objective

SSP += Aa1*2 + Aa2*1 + Aa3*5 + Bb1*2 + Cc1*2


#Constraints

#C1 - Done

#C2

SSP += OUT_A - IN_A == 1

#C3

SSP += IN_D == 1

#C4

SSP += OUT_B - IN_B == 0
SSP += OUT_C - IN_C == 0

#C5

SSP += IN_B == Aa1
SSP += IN_C == Aa2
SSP += IN_D == Bb1 + Aa3 + Cc1

#C6

SSP += OUT_A == Aa1 + Aa2 + Aa3
SSP += OUT_B == Bb1
SSP += OUT_C == Cc1


GLPK().solve(SSP)

# Solution
for v in SSP.variables():
	print v.name, "=", v.varValue

print "objective=", value(SSP.objective)  	
