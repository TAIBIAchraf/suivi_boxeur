import math
import torch
class Manipulation:
    #initialisation du tenseur des combinaisons
    comb = torch.tensor([])
    JAB_JAB_Cross,JAB_CROSS_leftuppercut,JAB_CROSS_JAB = 0,0,0
    total,Jab_percentage,Cross_percentage,Left_upper_percentage,Right_upper_percentage = 0,0,0,0,0

    def getAngle(self,mon_x_temp, mon_y_temp,a,b,c):
        global ang
        ang = 0
        if(mon_y_temp[:,c][-1]!=mon_y_temp[:,c][-2] and mon_y_temp[:,b][-1] != mon_y_temp[:,b][-2] and 
           mon_y_temp[:,a][-1] !=mon_y_temp[:,a][-2] and mon_x_temp[:,c][-1] != mon_x_temp[:,c][-2] and 
           mon_x_temp[:,b][-1] != mon_x_temp[:,b][-2] and mon_x_temp[:,a][-1] !=mon_x_temp[:,a][-2]):
            
            ang = math.degrees(math.atan2(mon_y_temp[:,c][-1]-mon_y_temp[:,b][-1], mon_x_temp[:,c][-1]-mon_x_temp[:,b][-1]) - math.atan2(mon_y_temp[:,a][-1]-mon_y_temp[:,b][-1], mon_x_temp[:,a][-1]-mon_x_temp[:,b][-1]))
            if ang < 0:
                ang = ang + 360
                return ang
            else:
                return ang
        else:
            return ang


    def combinaisons(self,gauche,droite,upper_gauche,upper_droite): 
        global comb
        if droite == 4:
            Manipulation.comb = torch.cat((Manipulation.comb,torch.tensor([4])),0)
        elif gauche == 3: 
            Manipulation.comb = torch.cat((Manipulation.comb,torch.tensor([3])),0)
        elif upper_gauche == 5: 
            Manipulation.comb = torch.cat((Manipulation.comb,torch.tensor([5])),0)
        elif upper_droite == 6: 
            Manipulation.comb = torch.cat((Manipulation.comb,torch.tensor([6])),0)
    
    def statistiques(self,compteur,combinaisons):
        #le nombre totale des coups
        Manipulation.total = compteur[0,3] + compteur[0,2] + compteur[0,1] + compteur[0,0]
        #Pourcentage des Jab
        Manipulation.Jab_percentage =  (compteur[0,2] / total) * 100
        #Pourcentage des Cross
        Manipulation.Cross_percentage =  (compteur[0,3] / total) * 100
        #Pourcentage des Left uppercut
        Manipulation.Left_upper_percentage =  (compteur[0,0] / total) * 100
        #Pourcentage des Right uppercut
        Manipulation.Right_upper_percentage =  (compteur[0,1] / total) * 100

        for i in range (0,len(Manipulation.comb),3):
            global JAB_JAB_Cross,JAB_CROSS_leftuppercut,JAB_CROSS_JAB
            if Manipulation.comb[i] == 3 and Manipulation.comb[i+1] == 3 and Manipulation.comb[i+2] == 4:
                Manipulation.JAB_JAB_Cross = Manipulation.JAB_JAB_Cross + 1
            elif Manipulation.comb[i] == 3 and Manipulation.comb[i+1] == 4 and Manipulation.comb[i+2] == 6:
                Manipulation.JAB_CROSS_leftuppercut = Manipulation.JAB_CROSS_leftuppercut + 1
            elif Manipulation.comb[i] == 3 and Manipulation.comb[i+1] == 4 and Manipulation.comb[i+2] == 3:
                Manipulation.JAB_CROSS_JAB = Manipulation.JAB_CROSS_JAB + 1
    
    
    
    
    
    
    
    
    
    
    
    