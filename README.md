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

- **Étape 3 - Créer l'image Docker**

Ouvrez le terminal et tapez les commandes suivantes:
```shell
#cloner mon dépot
git clone https://github.com/TAIBIAchraf/suivi_boxeur
#Ouvrez le dossier 
cd suivi_boxeur
#Construire l'image Docker
docker build -t Boxing_project .
```
> Après avoir créé notre image, nous devons maintenant procéder à la construction du conteneur.

- **Étape 4 - Créer et lancer le conteneur**

Ouvrez le terminal et tapez les commandes suivantes: 
```shell
sudo docker run --runtime nvidia -it --network host --name Boxing_project \
# (Optionnel) crée un lien entre un dossier local ~/mon_dossier et le dossier /nvdli-nano/data dans le conteneur
#--volume ~/mon_dossier:/nvdli-nano/data \
# Permettre le conteneur d'accéder à la caméra de la jetson nano
--volume /tmp/argus_socket:/tmp/argus_socket \
# Exposer le périphérique `/dev/video0` à l'intérieur du conteneur
--device /dev/video0 \
# Le nom et la version de l'image Docker construite
Boxing_project:latest
```

- **Étape 5 - Lancer le DEMO**
 
 Sur votre terminal vous allez au dossier `suivi_boxeur` vous lancer le `script.sh` par la commande suivante `./script.sh`. Vous ouvrez votre navigateur, vous allez à l'adresse suivante `http://localhost:8888`, vous saisissez le mot de passe suivant : `dlinano`. Vous lancez le DEMO dans le répértoire `/trt_pose/tasks/human_pose/index.ipynb`

 ## Références
 
[Machine Learning Containers for Jetson and JetPack](https://github.com/dusty-nv/jetson-containers)

[DLI Getting Started with AI on Jetson Nano](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/dli/containers/dli-nano-ai)

[Real-time pose estimation on NVIDIA Jetson (trt_pose)](https://github.com/NVIDIA-AI-IOT/trt_pose)

[Resize the size of swap memory on the Jetson Nano](https://github.com/JetsonHacksNano/resizeSwapMemory)








