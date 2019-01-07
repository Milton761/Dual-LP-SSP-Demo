from pulp import *


SSP = LpProblem("Navigation", LpMinimize)

#Declare Variables

#Occupation Measure Variables
#S1
S1_R_S2 = LpVariable("S1_R_S2",0)
S1_D_S5 = LpVariable("S1_D_S5",0)
S1_D_DE = LpVariable("S1_D_DE",0)
#S2
S2_L_S1 = LpVariable("S2_L_S1",0)
S2_R_S3 = LpVariable("S2_R_S3",0)
S2_D_S6 = LpVariable("S2_D_S6",0)
S2_D_DE = LpVariable("S2_D_DE",0)
#S3
S3_L_S2 = LpVariable("S3_L_S2",0)
S3_R_S4 = LpVariable("S3_R_S4",0)
S3_D_S7 = LpVariable("S3_D_S7",0)
S3_D_DE = LpVariable("S3_D_DE",0)
#S4
S4_L_S3 = LpVariable("S4_L_S3",0)
S4_D_S8 = LpVariable("S4_D_S8",0)
S4_D_DE = LpVariable("S4_D_DE",0)
#S5
S5_U_S1 = LpVariable("S5_U_S1",0)
S5_R_S6 = LpVariable("S5_R_S6",0)
S5_R_DE = LpVariable("S5_R_DE",0)
S5_D_S9 = LpVariable("S5_D_S9",0)
#S6
S6_L_S5 = LpVariable("S6_L_S5",0)
S6_L_DE = LpVariable("S6_L_DE",0)
S6_U_S2 = LpVariable("S6_U_S2",0)
S6_R_S7 = LpVariable("S6_R_S7",0)
S6_R_DE = LpVariable("S6_R_DE",0)
S6_D_10 = LpVariable("S6_D_10",0)
#S7
S7_L_S6 = LpVariable("S7_L_S6",0)
S7_L_DE = LpVariable("S7_L_DE",0)
S7_U_S3 = LpVariable("S7_U_S3",0)
S7_R_S8 = LpVariable("S7_R_S8",0)
S7_R_DE = LpVariable("S7_R_DE",0)
S7_D_S11 = LpVariable("S7_D_S11",0)
#S8
S8_L_S7 = LpVariable("S8_L_S7",0)
S8_L_DE = LpVariable("S8_L_DE",0)
S8_U_S4 = LpVariable("S8_U_S4",0)
S8_D_S12 = LpVariable("S8_D_S12",0)
#S9
S9_U_S5 = LpVariable("S9_U_S5",0)
S9_U_DE = LpVariable("S9_U_DE",0)
S9_R_10 = LpVariable("S9_R_10",0)
#S10
S10_L_S9 = LpVariable("S10_L_S9",0)
S10_U_S6 = LpVariable("S10_U_S6",0)
S10_U_DE = LpVariable("S10_U_DE",0)
S10_R_S11 = LpVariable("S10_R_S11",0)
#S11
S11_L_S10 = LpVariable("S11_L_S10",0)
S11_U_S7 = LpVariable("S11_U_S7",0)
S11_U_DE = LpVariable("S11_U_DE",0)
S11_R_S12 = LpVariable("S11_R_S12",0)
#S12
S12_L_S11 = LpVariable("S12_L_S11",0)
S12_U_S8 = LpVariable("S12_U_S8",0)
S12_U_DE = LpVariable("S12_U_DE",0)

#In Variables
IN_S1  = LpVariable("IN_S1" ,0)
IN_S2  = LpVariable("IN_S2" ,0)
IN_S3  = LpVariable("IN_S3" ,0)
IN_S4  = LpVariable("IN_S4" ,0)
IN_S5  = LpVariable("IN_S5" ,0)
IN_S6  = LpVariable("IN_S6" ,0)
IN_S7  = LpVariable("IN_S7" ,0)
IN_S8  = LpVariable("IN_S8" ,0)
IN_S9  = LpVariable("IN_S9" ,0)
IN_S10 = LpVariable("IN_S10",0)
IN_S11 = LpVariable("IN_S11",0)
IN_S12 = LpVariable("IN_S12",0)

IN_DE  = LpVariable("IN_DE",0)

#Out Variables
OUT_S1  = LpVariable("OUT_S1" ,0)
OUT_S2  = LpVariable("OUT_S2" ,0)
OUT_S3  = LpVariable("OUT_S3" ,0)
OUT_S4  = LpVariable("OUT_S4" ,0)
OUT_S5  = LpVariable("OUT_S5" ,0)
OUT_S6  = LpVariable("OUT_S6" ,0)
OUT_S7  = LpVariable("OUT_S7" ,0)
OUT_S8  = LpVariable("OUT_S8" ,0)
OUT_S9  = LpVariable("OUT_S9" ,0)
OUT_S10 = LpVariable("OUT_S10",0)
OUT_S11 = LpVariable("OUT_S11",0)
OUT_S12 = LpVariable("OUT_S12",0)

DE  = LpVariable("DE",0)


#Objective

SSP += S1_R_S2+S1_D_S5+S1_D_DE+S2_L_S1 +S2_R_S3 +S2_D_S6 +S2_D_DE +S3_L_S2 +S3_R_S4 +S3_D_S7 +S3_D_DE +S4_L_S3+S4_D_S8 +S4_D_DE +S5_U_S1 +S5_R_S6 +S5_R_DE +S5_D_S9 +S6_L_S5+S6_L_DE +S6_U_S2 +S6_R_S7 +S6_R_DE +S6_D_10 +S7_L_S6 +S7_L_DE +S7_U_S3 +S7_R_S8 +S7_R_DE +S7_D_S11 +S8_L_S7 +S8_L_DE +S8_U_S4 +S8_D_S12 +S9_U_S5 +S9_U_DE +S9_R_10 +S10_L_S9 +S10_U_S6 +S10_U_DE +S10_R_S11 +S11_L_S10 +S11_U_S7 +S11_U_DE +S11_R_S12 +S12_L_S11 +S12_U_S8 +S12_U_DE 

#Constraints

#C1 - Done

#C2
SSP += IN_S1 == S5_U_S1 + S2_L_S1
SSP += IN_S2 == S1_R_S2 + S3_L_S2 + S6_U_S2
SSP += IN_S3 == S2_R_S3 + S4_L_S3 + S7_U_S3
SSP += IN_S4 == S3_R_S4 + S8_U_S4

SSP += IN_S5 == S1_D_S5*0.2 + S6_L_S5*0.2 + S9_U_S5*0.2
SSP += IN_S6 == S5_R_S6*0.4 + S2_D_S6*0.4 + S7_L_S6*0.4 + S10_U_S6*0.4
SSP += IN_S7 == S6_R_S7*0.6 + S3_D_S7*0.6 + S8_L_S7*0.6 + S11_U_S7*0.6
SSP += IN_S8 == S7_R_S8*0.8 + S4_D_S8*0.8 + S12_U_S8*0.8

SSP += IN_S9 == S5_D_S9 + S10_L_S9
SSP += IN_S10 == S9_R_10 + S6_D_10 + S11_L_S10
SSP += IN_S11 == S10_R_S11 + S7_D_S11 + S12_L_S11
SSP += IN_S12 == S11_R_S12 + S8_D_S12

SSP += IN_DE == S1_D_DE*0.8 + S2_D_DE*0.6 + S3_D_DE*0.4 + S4_D_DE*0.2 + S5_R_DE*0.6 + S6_R_DE*0.4 + S6_L_DE*0.8 + S7_R_DE*0.2 + S7_L_DE*0.6 + S8_L_DE*0.4 + S9_U_DE*0.8 + S10_U_DE*0.6 + S11_U_DE*0.4 + S12_U_DE*0.2

#C3


SSP += OUT_S1 == S1_R_S2 + S1_D_S5 + S1_D_DE 
SSP += OUT_S2 == S2_L_S1 + S2_R_S3 + S2_D_S6 + S2_D_DE
SSP += OUT_S3 == S3_L_S2 + S3_R_S4 + S3_D_S7 + S3_D_DE
SSP += OUT_S4 == S4_L_S3+S4_D_S8 +S4_D_DE
SSP += OUT_S5 == S5_U_S1 +S5_R_S6 +S5_R_DE +S5_D_S9
SSP += OUT_S6 == S6_L_S5+S6_L_DE +S6_U_S2 +S6_R_S7 +S6_R_DE +S6_D_10
SSP += OUT_S7 == S7_L_S6 +S7_L_DE +S7_U_S3 +S7_R_S8 +S7_R_DE +S7_D_S11
SSP += OUT_S8 == S8_L_S7 +S8_L_DE +S8_U_S4 +S8_D_S12
#SSP += OUT_S9 == S9_U_S5 +S9_U_DE +S9_R_10 
SSP += OUT_S10 == S10_L_S9 +S10_U_S6 +S10_U_DE +S10_R_S11 
SSP += OUT_S11 == S11_L_S10 +S11_U_S7 +S11_U_DE +S11_R_S12 
SSP += OUT_S12 == S12_L_S11 +S12_U_S8 +S12_U_DE 

#C4


SSP += OUT_S2  - IN_S2	<= 0
SSP += OUT_S3  - IN_S3  <= 0
SSP += OUT_S4  - IN_S4  <= 0
SSP += OUT_S5  - IN_S5  <= 0
SSP += OUT_S6  - IN_S6  <= 0
SSP += OUT_S7  - IN_S7  <= 0
SSP += OUT_S8  - IN_S8  <= 0
#SSP += OUT_S9  - IN_S9  <= 0
SSP += OUT_S10 - IN_S10 <= 0
SSP += OUT_S11 - IN_S11 <= 0
SSP += OUT_S12 - IN_S12 <= 0

#C5

SSP += OUT_S1 - IN_S1 <= 1

#C6

SSP += IN_S12 == 0.8



GLPK().solve(SSP)

# Solution
for v in SSP.variables():
	print v.name, "=", v.varValue

print "objective=", value(SSP.objective)  