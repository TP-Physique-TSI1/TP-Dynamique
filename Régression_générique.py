import numpy as np
from matplotlib import pyplot as plt

#%% Définition du tirage au sort de la valeur d'une variable

"""
    Renvoie une valeur x aléatoire de la variable X d'incertitude-type u(X)
        X = [x, u(X)] (loi normale)
"""

def Alea(X):
    tirage = np.random.normal()   
    return X[0]+X[1]*tirage

#%% Procedure Regression Linéaire; tableaux np X et Y (méthode des moindres carrés)
    
def RegLin(X,Y):
    N = len(X)
    moyX = sum(X)/N
    moyY = sum(Y)/N
    pente = sum((X-moyX)*(Y-moyY))/(sum((X-moyX)**2))   # calcule la pente de la droite de régression
    ordor = moyY - pente*moyX                           # calcule l'ordonnée à l'origine de la droite de régression
    return [pente,ordor]

#%% Entrées
    
grandeur1 = []        # Liste contenant les valeurs mesurées de la grandeur 1
grandeur2 = []        # Liste contenant les valeurs mesurées de la grandeur 2
incertitude_grandeur1 =                         # Estimation de l'incertitude-type sur la grandeur 1
incertitude_grandeur2 =                         # Estimation de l'incertitude-type sur la grandeur 2                      
                                                      


#%% Préparation des listes avec incertitudes

Grandeur1 = []
for k in range(len(hauteur_chute)):
    Grandeur1.append([grandeur1[k], incertitude_grandeur1])            # Remplit une liste de listes contenant les valeurs mesurées de la grandeur 1e assorties de leur incertitude 
    
Grandeur2  = []
for k in range(len(duree_chute)):
    Grandeur2.append([(grandeur2[k]), incertitude_grandeur2])           # Remplit une liste de listes contenant les valeurs mesurées de la grandeur 2 assorties de leur incertitude 
    
#%% Méthode de Monte Carlo pour déterminer les incertitudes sur la pente et l'ordonnée à l'origine de la régression linéaire
    
LPente = []     # Crée une liste vide pour stocker les valeurs de la pente de la droite de régression issues de la simulation
LOrdor = []     # Crée une liste vide pour stocker les valeurs de l'ordonnée à l'origine de la droite de régression issues de la simulation

iterations = 100000     # Nombre d'essais de la simulation

for i in range(iterations):
    

    Alea_ordonnée = []          # Crée une liste vide pour stocker les valeurs de la grandeur à porter en ordonnée issues de la simulation
    Alea_abscisse = []            # Crée une liste vide pour stocker les valeurs de la grandeur à porter en abscisse issues de la simulation
    
    for k in range(len(grandeur1)):
       
        Alea_ordonnée.append()                                   # Remplit la liste Alea_ordonnée avec len(grandeur1) valeurs tirées au hasard (loi normale) de la grandeur à porter en ordonnée du graphe de régression
        Alea_abscisse.append()                                    # Remplit la liste  Alea_abscisse avec avec len(grandeur1) valeurs tirées au hasard (loi normale) de la grandeur à porter en abscisse du graphe de régression
    Pente = RegLin(np.array(Alea_abscisse),np.array(Alea_ordonnée))[0]              # Calcule la pente de la droite de régression pour chaque itération
    OrdOr = RegLin(np.array(Alea_abscisse),np.array(Alea_ordonnée))[1]              # Calcule l'ordonnée à l'origine de la droite de régression pour chaque itération
    LPente.append(Pente)                                                                    # Remplit la liste LPente avec les valeurs calculées de la pente de la droite de régression pour chaque itération
    LOrdor.append(OrdOr)                                                                    # Remplit la liste LOrdor avec les valeurs calculées de l'ordonnée à l'origine de la droite de régression pour chaque itération
    
MoyPente = np.sum(LPente)/iterations                                                        # Calcule la moyenne des valeurs simulées de la pente 
MoyOrdOr = np.sum(LOrdor)/iterations                                                        # Calcule la moyenne des valeurs simulées de l'ordonnée à l'origine

incertitude_type_Pente = np.std(np.array(LPente))                                           # Calcule l'incertitude-type sur la pente de la droite de régression
incertitude_elargie_Pente = 2*incertitude_type_Pente                                        # Calcule l'incertitude élargie sur la pente de la droite de régression
incertitude_type_OrdOr = np.std(np.array(LOrdor))                                           # Calcule l'incertitude-type sur l'ordonnée à l'origine de la droite de régression
incertitude_elargie_OrdOr = 2*incertitude_type_OrdOr                                        # Calcule l'incertitude élargie sur l'ordonnée à l'origine de la droite de régression

#%% Affichage

print ('Pente de la droite de régression:', MoyPente, 'unité')
print('Incertitude élargie sur la pente :',incertitude_elargie_Pente, 'unité)
print("Ordonnée à l origine :",MoyOrdOr, 'unité')
print("Incertitude élargie sur l'ordonnée à l origine:",incertitude_elargie_OrdOr, 'unité')

fig = plt.figure(figsize = (10, 10))                                                        # Crée une zone graphique
plt.gcf().subplots_adjust(left = 0.1, bottom = 0.1,
                       right = 0.9, top = 0.9, wspace = 0, hspace = 0.2)                    # Ajuste les valeurs des marges de la figure
ax1 = fig.add_subplot(2,1,1)                                                                # Crée le premier graphe de la figure
ax1.hist(LPente, range = (7.5, 12), bins = 50, color = 'orange', edgecolor = 'black')        # Affiche l'histogramme de répartion des valeurs simulées de la pente
ax1.set_xlabel('Pente (unité) ')
ax1.set_ylabel('effectif')
ax1.set_title('Pour 100 000 iterations')

ax2 = fig.add_subplot(2,1,2)                                                                # Crée le deuxième graphe de la figure
ax2.hist(LOrdor, range = (-0.6, 0.7), bins = 50, color = 'blue', edgecolor = 'black')       # Affiche l'histogramme de répartion des valeurs simulées de l'ordonnée à l'origine
ax2.set_xlabel("Ordonnée à l'origine (unité)")
ax2.set_ylabel('effectif')


plt.show()    


