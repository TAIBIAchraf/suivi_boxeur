class Mouvements:
    stop_condition,stop_condition_1 = 1,1
    stop_condition_2,stop_condition_3 = 1,1
    upperg_cpt,uperd_cpt,D_cpt,J_cpt = 0,0,0,0

    def uppercut(self,y_key,angle,left_right,compteur):
        global stop_condition,stop_condition_1
        if left_right == 'gauche':
            if  angle < 90 and angle > 0 and y_key[:,9][-1] < y_key[:,0][-1] and Mouvements.stop_condition == 0:
                print("uppercut gauche détéctée")
                Mouvements.stop_condition = 1
                Mouvements.upperg_cpt = Mouvements.upperg_cpt + 1
                compteur[0,0] = Mouvements.upperg_cpt
                return 5
            elif y_key[:,7][-1] > y_key[:,0][-1]:
                Mouvements.stop_condition = 0
                
        elif left_right == 'droite':
            if  angle < 90 and angle > 0 and y_key[:,10][-1] < y_key[:,0][-1] and Mouvements.stop_condition_1 == 0:
                print("uppercut droite détéctée")
                Mouvements.stop_condition_1 = 1
                Mouvements.uperd_cpt = Mouvements.uperd_cpt + 1
                compteur[0,1] = Mouvements.uperd_cpt
                return 6
            elif y_key[:,8][-1] > y_key[:,0][-1]:
                Mouvements.stop_condition_1 = 0
                
    def JAB(self,angle,y_key,left_right,compteur):
        if left_right == 'gauche':
            if angle <=183 and angle >= 170 and Mouvements.stop_condition_2 == 0:
                    print("JAB détéctée")
                    Mouvements.stop_condition_2 = 1
                    Mouvements.J_cpt = Mouvements.J_cpt + 1
                    compteur[0,2] = Mouvements.J_cpt
                    return 3
            elif y_key[:,9][-1] > y_key[:,5][-1] :
                    Mouvements.stop_condition_2 = 0
                    
        elif left_right == 'droite':
            if angle <=183 and angle >= 170 and Mouvements.stop_condition_3 == 0:
                    print("Droite détéctée")
                    Mouvements.stop_condition_3 = 1
                    Mouvements.D_cpt = Mouvements.D_cpt + 1
                    compteur[0,3] = Mouvements.D_cpt
                    return 4
            elif y_key[:,10][-1] > y_key[:,6][-1] :
                    Mouvements.stop_condition_3 = 0

