#Numerical methods for solving voltagefall in lines

import numpy as np
import cmath as cm

#Constants
V_Biri = 60000 #V

#FeAl 1x95
R_95 = 0.1902
X_95 = 0.40

Z = R_95 + 1j*X_95

P_Viflat = 11000000 #W
Q_Viflat = 3000000 #var
S_Viflat = complex(P_Viflat, Q_Viflat) #VA
S_Viflat_conj = S_Viflat.conjugate() #VA

V_Viflat_tester = 60000 #V


V_Viflat = V_Biri - (Z*(S_Viflat_conj/V_Viflat_tester.conjugate())) #V

#Numerical iterations
while V_Viflat_tester != V_Viflat:
    V_Viflat_tester = V_Viflat
    V_Viflat = V_Biri - (Z*(S_Viflat_conj/V_Viflat_tester.conjugate())) #V 
    print("V_Viflat: ", cm.polar(V_Viflat))
