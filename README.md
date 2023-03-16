# Détection des mouvements de la boxe anglaise (trt_pose)
Ce dépôt contient tout ce vous avez besoin pour détecter les mouvements et les enchainements de base de la boxe anglaise.

## Introduction
Ce projet est la première étape vers un coach virtuel de la boxe anglaise.il sert à détecter les **JAB** , **CROSS** , **Uppercut Gauche** , **Uppercut Droite** ainsi que les 4 enchainements indisponsables dans ce sport : **Jab/Jab/Cross** , **Jab/Cross/Uppercut Gauche** , **Jab/Cross/JAB** , **Jab/Cross/Uppercut Droite**. Un bilan sera envoyé (à votre smartphone) à la fin de votre séance. 
- **matériels requis** : Jetson Nano 4gb + son module de wifi + camera CSI.
## Comment cela fonctionne-t-il ?
Avec un fichier jupyter `index.ipynb`, on charge le modèle pré-entrainé `mon_modele.pth` pour l'estimation de pose --> on crée deux objets instances à partir de `Mouvements()` et `Manipulation()` --> on extrait les coordonnées des points clés à l'aide de la fonction `get_keypoints`--> on traite ces coordonnées en utilisant plusieurs fonctions --> on envoie le bilan à l'aide de la fonction `send()`.
