import torch

class Mouvements:
    #tenseur stop condition
    stop_condition = torch.ones([4])

    def uppercut(self,y_key,angle,left_right,compteur):
        global stop_condition
        if left_right == 'gauche':
            if  angle < 90 and angle > 0 and y_key[:,9][-1] < y_key[:,0][-1] and Mouvements.stop_condition[0] == 0:
                print("uppercut gauche détéctée")
                Mouvements.stop_condition[0] = 1
                compteur[0,0] = compteur[0,0] + 1
                return 5
            elif y_key[:,7][-1] > y_key[:,0][-1]:
                Mouvements.stop_condition[0] = 0
                
        elif left_right == 'droite':
            if  angle < 90 and angle > 0 and y_key[:,10][-1] < y_key[:,0][-1] and Mouvements.stop_condition[1] == 0:
                print("uppercut droite détéctée")
                Mouvements.stop_condition[1] = 1
                compteur[0,1] = compteur[0,1] + 1
                return 6
            elif y_key[:,8][-1] > y_key[:,0][-1]:
                Mouvements.stop_condition[1] = 0
                
    def JAB(self,angle,y_key,left_right,compteur):
        if left_right == 'gauche':
            if angle <=183 and angle >= 170 and Mouvements.stop_condition[2] == 0:
                    print("JAB détéctée")
                    Mouvements.stop_condition[2] = 1
                    compteur[0,2] = compteur[0,2] + 1
                    return 3
            elif y_key[:,9][-1] > y_key[:,5][-1] :
                    Mouvements.stop_condition[2] = 0
                    
        elif left_right == 'droite':
            if angle <=183 and angle >= 170 and Mouvements.stop_condition[3] == 0:
                    print("Cross détéctée")
                    Mouvements.stop_condition[3] = 1
                    compteur[0,3] = compteur[0,3] + 1
                    return 4
            elif y_key[:,10][-1] > y_key[:,6][-1] :
                    Mouvements.stop_condition[3] = 0

