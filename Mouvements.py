# Importer la Bibiothéque pytorch
import torch

class Mouvements:
    # Tenseur pour annuler la détection dans chaque frame
    stop_condition = torch.ones([4])

    # détecter et compter les uppercuts à partir de l'angle et le tenseur y_key 
    # y_key est un tenseur des coordonnées y des points-clés
    def uppercut(self,y_key,angle,left_right,compteur):
        # Est ce que c'est un uppercut gauche/droite
        if left_right == 'gauche':
            # Vérifier si on n'avait pas une détéction avant de l'uppercut gauche par "stop_condition[0] == 0"
            # Vérifier si l'ordonnée du poignet est plus grand que l'ordonnée du nez
            # Verifier est ce que l'angle faite par le poignet gauche, le coud gauche et l'épaule gauche est < 90
            if  angle < 90 and angle > 0 and y_key[:,9][-1] < y_key[:,0][-1] and Mouvements.stop_condition[0] == 0:
                print("uppercut gauche détéctée")
                # Quand on détécte on change le stop_condition associé à ce mouvement en 1 (on désactive la détection de ce mouvement)
                Mouvements.stop_condition[0] = 1
                # Compteur des uppercuts gauches
                compteur[0,0] = compteur[0,0] + 1
                # Dans le cas de la détéction on renvoie le nombre 5
                return 5
            elif y_key[:,7][-1] > y_key[:,0][-1]:
                # On active la détection "stop_condition[0] = 0" quand le coude gauche est inférieur au nez
                Mouvements.stop_condition[0] = 0
                
        elif left_right == 'droite':
            #Vérifier les conditions
            if  angle < 90 and angle > 0 and y_key[:,10][-1] < y_key[:,0][-1] and Mouvements.stop_condition[1] == 0:
                print("uppercut droite détéctée")
                # Désactiver la détection
                Mouvements.stop_condition[1] = 1
                # Comptage
                compteur[0,1] = compteur[0,1] + 1
                # Renvoyer la valeur 6
                return 6
            elif y_key[:,8][-1] > y_key[:,0][-1]:
            # Activer la détection
                Mouvements.stop_condition[1] = 0
    # Fonction pour la détection du JAB et CROSS            
    def JAB(self,angle,y_key,left_right,compteur):
        # Esdt ce que c'est un JAB ou CROSS
        if left_right == 'gauche':
            # Vérifier les conditions
            if angle <=183 and angle >= 170 and Mouvements.stop_condition[2] == 0:
                    print("JAB détéctée")
                    # Désactiver la détection
                    Mouvements.stop_condition[2] = 1
                    # Comptage
                    compteur[0,2] = compteur[0,2] + 1
                    # Retourner la valeur 3
                    return 3
            elif y_key[:,9][-1] > y_key[:,5][-1] :
                    # Activer la détection
                    Mouvements.stop_condition[2] = 0
                    
        elif left_right == 'droite':
            # Vérifier les conditions
            if angle <=183 and angle >= 170 and Mouvements.stop_condition[3] == 0:
                    print("Cross détéctée")
                    # Désactiver la détection
                    Mouvements.stop_condition[3] = 1
                    # Comptage
                    compteur[0,3] = compteur[0,3] + 1
                    # Retourner la valeur 4
                    return 4
            elif y_key[:,10][-1] > y_key[:,6][-1] :
                    Mouvements.stop_condition[3] = 0
                    # Activer la détection

