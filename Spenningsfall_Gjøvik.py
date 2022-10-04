import cmath

#Spenningsfallsformelen der V_linje_slutt er kjent
def spenningsfall(v_forrige, P_tot, Q_tot, R, X, l):
    V_linje_slutt = v_forrige
    
    lengde = l #kilometer

    P_2 = P_tot #Aktiv effekt
    Q_2 = Q_tot #Reaktiv effekt
    R = R * l #motstand i luftlinje/Kabel [ohm/km]
    X = X * l #induktiv reaktans i luftlinje/kabel [ohm/km]

    V_conj_linje_2 = V_linje_slutt.conjugate()

    delta_V = (1/V_conj_linje_2) * complex((P_2 * R + Q_2 * X),(P_2*X - Q_2*R))

    return V_linje_slutt + delta_V


#FeAl 1x95
R_95 = 0.1902
X_95 = 0.40

#FeAl 1x240
R_240 = 0.0760
X_240 = 0.365

#TSLE 3x1x1200 Al
R_TSLE = 0.025
X_TSLE = 0.15

#Biri
V_Biri = 60000
P_Biri = 25000000
Q_Biri = 7000000
l_Biri = 20.2

#Viflat
V_Viflat = spenningsfall(V_Biri, P_Biri, Q_Biri, R_95, X_95, l_Biri)
P_Viflat = 11000000 + P_Biri
Q_Viflat = 3000000 + Q_Biri
l_Viflat = 4.1

#Bjugstad
V_Bjugstad = spenningsfall(V_Viflat, P_Viflat, Q_Viflat, R_95, X_95, l_Viflat)
P_Bjugstad = 40000000 + P_Viflat
Q_Bjugstad = 12000000 + Q_Viflat
l_Bjugstad = 3.4

#Mellomparti
V_mellomparti = spenningsfall(V_Bjugstad, P_Bjugstad, Q_Viflat, R_240, X_240, l_Bjugstad)
P_mellomparti = P_Bjugstad
Q_mellomparti = Q_Bjugstad
l_mellomparti = 1.4

#Gjøvik (MÅL)
V_Gjøvik = spenningsfall(V_mellomparti, P_mellomparti, Q_mellomparti, R_TSLE, X_TSLE, l_mellomparti)


print("V_Biri: ", cmath.polar(V_Biri))
print("V_Viflat: ", cmath.polar(V_Viflat))
print("V_Bjugstad: ", cmath.polar(V_Bjugstad))
print("V_mellomparti: ", cmath.polar(V_mellomparti))
print("V_Gjøvik: ", cmath.polar(V_Gjøvik))
