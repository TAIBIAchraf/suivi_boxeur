# Détection des mouvements de la boxe anglaise (trt_pose)
Ce dépôt contient tout ce vous avez besoin pour détecter les mouvements et les enchainements de base de la boxe anglaise.

## Introduction
Ce projet est la première étape vers un coach virtuel de la boxe anglaise.il sert à détecter les **JAB** , **CROSS** , **Uppercut Gauche** , **Uppercut Droite** ainsi que les 4 enchainements indisponsables dans ce sport : **Jab/Jab/Cross** , **Jab/Cross/Uppercut Gauche** , **Jab/Cross/JAB** , **Jab/Cross/Uppercut Droite**. Un bilan sera envoyé (à votre smartphone) à la fin de votre séance. 
- **matériels requis** : Jetson Nano 4gb (minimum) + son module de wifi + camera CSI.
## Comment cela fonctionne-t-il ?
Avec un fichier jupyter `index.ipynb`, on charge le modèle pré-entrainé `mon_modele.pth` pour l'estimation de pose --> on crée deux objets instances à partir de `Mouvements()` et `Manipulation()` --> on extrait les coordonnées des points clés à l'aide de la fonction `get_keypoints`--> on traite ces coordonnées en utilisant plusieurs fonctions --> on envoie le bilan à l'aide de la fonction `send()`.
> **Remarque:** pour plus d'informations sur les fonctions utilisées, veuillez consulter les fichiers `Manipulation.py`,`Mouvements.py` et `index.ipynb`.

## Tutorial étape par étape
- **Étape 1 - Augmenter la mémoire SWAP de la jetson nano à 4GB :** 
Ouvrez le terminal et tapez les commandes suivantes:
```shell
git clone https://github.com/JetsonHacksNano/resizeSwapMemory
cd resizeSwapMemory
./setSwapMemorySize -g 4
```
> **Remarque:** Veuillez redémarrer votre carte après cette étape. 
- **Étape 2 - Activer l'acces au CUDA lors de la construction du docker:** 

Ouvrez le fichier `/etc/docker/daemon.json` et ajouter `"default-runtime": "nvidia"`, comme ceci :
```shell
{
    "runtimes": {
        "nvidia": {
            "path": "nvidia-container-runtime",
            "runtimeArgs": []
        }
    },

    "default-runtime": "nvidia"
}
```
> **Remarque:** Veuillez redémarrer encore une fois votre carte après cette étape. 

- **Étape 3 - Créer l'image**

Ouvrez le terminal et tapez les commandes suivantes:
```shell
#cloner mon dépot
git clone https://github.com/TAIBIAchraf/suivi_boxeur
#Ouvrez le dossier 
cd suivi_boxeur
#Construire le docker image
docker build -t Boxing_project .
```
> Après avoir créé notre image, nous devons maintenant procéder à la construction du conteneur.

- **Étape 4 - Créer le conteneur**
sur votre terminal vous tapez les commandes suivantes :











