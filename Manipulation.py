# Importer la bibliothéque math pour calculer les angles
import math
# Importer la bibliothéque requests pour envoyer des notifications aux smartphones
import requests 
# Importer la bibliothéque pytorch 
import torch


class Manipulation:
    # Initialisation du tenseur des pourcentages
    mvt_pourcentage = torch.zeros([5])
    # Initialisation du tenseur des coups effectués
    coups = torch.tensor([])
    # Initialisation du tenseur des enchainements (combinaisons) détectés
    comb = torch.zeros([1,4])

    # Fonction de calcul d'angle
    def getAngle(self,mon_x_temp, mon_y_temp,a,b,c):
        ang = 0
        
        # On calcul l'angle seulement si les deux dernieres valeurs ([-1] , [-2]) de x , y sont différentes dans les trois points a,b et c
        if(mon_y_temp[:,c][-1]!=mon_y_temp[:,c][-2] and mon_y_temp[:,b][-1] != mon_y_temp[:,b][-2] and 
           mon_y_temp[:,a][-1] !=mon_y_temp[:,a][-2] and mon_x_temp[:,c][-1] != mon_x_temp[:,c][-2] and 
           mon_x_temp[:,b][-1] != mon_x_temp[:,b][-2] and mon_x_temp[:,a][-1] !=mon_x_temp[:,a][-2]):
            
            # Calculer mathématiquement l'angle
            ang = math.degrees(math.atan2(mon_y_temp[:,c][-1]-mon_y_temp[:,b][-1], mon_x_temp[:,c][-1]-mon_x_temp[:,b][-1]) - math.atan2(mon_y_temp[:,a][-1]-mon_y_temp[:,b][-1], mon_x_temp[:,a][-1]-mon_x_temp[:,b][-1]))
            
            if ang < 0:
                ang = ang + 360
                return ang
            else:
                return ang
        else:
            return ang

    # Une fonction qui stock les coups dans le tenseur "coups" 
    def combinaisons(self,gauche,droite,upper_gauche,upper_droite): 
        # Quand on a une droite (CROSS) détectée on rajoute dans le tenseur le nombre 4
        if droite == 4:
            Manipulation.coups = torch.cat((Manipulation.coups,torch.tensor([4])),0)
        # Quand on a une gauche (JAB) détectée on rajoute dans le tenseur le nombre 3
        elif gauche == 3: 
            Manipulation.coups = torch.cat((Manipulation.coups,torch.tensor([3])),0)
        # Quand on a un uppercut gauche détecté on rajoute dans le tenseur le nombre 5
        elif upper_gauche == 5: 
            Manipulation.coups = torch.cat((Manipulation.coups,torch.tensor([5])),0)
        # Quand on a un uppercut droite détecté on rajoute dans le tenseur le nombre 6
        elif upper_droite == 6: 
            Manipulation.coups = torch.cat((Manipulation.coups,torch.tensor([6])),0)

    
    # Une fonction qui calcul les statistiques à partir du tenseur "compteur"
    def statistiques(self,compteur):
        # Le nombre totale des coups
        Manipulation.mvt_pourcentage[0] = compteur[0,3] + compteur[0,2] + compteur[0,1] + compteur[0,0]
        # Pourcentage des Jab
        Manipulation.mvt_pourcentage[1] =  (compteur[0,2] / Manipulation.mvt_pourcentage[0]) * 100
        # Pourcentage des Cross
        Manipulation.mvt_pourcentage[2] =  (compteur[0,3] / Manipulation.mvt_pourcentage[0]) * 100
        # Pourcentage des Left uppercut
        Manipulation.mvt_pourcentage[3] =  (compteur[0,0] / Manipulation.mvt_pourcentage[0]) * 100
        # Pourcentage des Right uppercut
        Manipulation.mvt_pourcentage[4] =  (compteur[0,1] / Manipulation.mvt_pourcentage[0]) * 100
        
        # Pour détecter les enchainements
        # On parcouru le tenseur coups
        for i in range (0,len(Manipulation.coups),1):
            # Détection et comptage de Jab Jab Cross
            if Manipulation.coups[i] == 3 and Manipulation.coups[i+1] == 3 and Manipulation.coups[i+2] == 4:
                Manipulation.comb[0,0] = Manipulation.comb[0,0] + 1

            # Détection et comptage de  Jab Cross Left_Uppercut
            elif Manipulation.coups[i] == 3 and Manipulation.coups[i+1] == 4 and Manipulation.coups[i+2] == 5:
                Manipulation.comb[0,1] = Manipulation.comb[0,1] + 1
                
            # Détection et comptage de  Jab Cross JAB
            elif Manipulation.coups[i] == 3 and Manipulation.coups[i+1] == 4 and Manipulation.coups[i+2] == 3:
                Manipulation.comb[0,2] = Manipulation.comb[0,2] + 1
                
            #Detection Jab Cross Right_Uppercut
            elif Manipulation.coups[i] == 3 and Manipulation.coups[i+1] == 4 and Manipulation.coups[i+2] == 6:
                Manipulation.comb[0,3] = Manipulation.comb[0,3] + 1
    
    # Fonction qui envoie le bilan aux smartphones 
    def send(self,compteur):
             requests.post('https://api.mynotifier.app', {
              "apiKey": 'b0ad018e-b4fa-4e6b-8977-ffcec28520f5', # à changer par votre propre clé
              "message": "Votre Bilan", 
              "description": """Le nombre total des mouvements effectués est {} ({} JAB , {} CROSS , {} Uppercuts gauches ,{} Uppercuts Droites) \nPourcentages :\n JAB : {:.1f}%\n CROSS : {:.1f}%\n Uppercuts Gauches : {:.1f}% \n Uppercuts Droites : {:.1f}%\n Les Enchainements détectés :\n JAB JAB CROSS : {}\n JAB CROSS Uppercut_gauche : {}\n JAB CROSS JAB :{}\nJAB CROSS Uppercut_droite: {}""".format(int(Manipulation.mvt_pourcentage[0]),int(compteur[0,2]),int(compteur[0,3]),int(compteur[0,0]),int(compteur[0,1]),Manipulation.mvt_pourcentage[1],Manipulation.mvt_pourcentage[2],Manipulation.mvt_pourcentage[3],Manipulation.mvt_pourcentage[4],int(Manipulation.comb[0,0]),int(Manipulation.comb[0,1]),int(Manipulation.comb[0,2]),int(Manipulation.comb[0,3]))})
        
    
    
    
    
    
    
    
    
    
    