#!/bin/bash

# Copier la classe Mouvements
cp Mouvements.py ../trt_pose/tasks/human_pose/
# Copier la classe Manipulation
cp Manipulation.py ../trt_pose/tasks/human_pose/
# Copier le fichier JUPYTER
cp index.ipynb ../trt_pose/tasks/human_pose/
# Importer le model optimisé
wget https://www.dropbox.com/s/ftx84e6nvvvbipx/resnet18_baseline_att_224x224_A_epoch_249_trt.pth?dl=1
# Déplacer le model
mv resnet18_baseline_att_224x224_A_epoch_249_trt.pth?dl=1 ../trt_pose/tasks/human_pose/mon_model.pth
# Supprimer l'ancien fichier d'installation de la csi
rm ../jetcam/jetcam/csi_camera.py
# Importer la nouvelle (pour faire une rotation de l'image de 180)
cp csi_camera.py ../jetcam/jetcam/
# Installer jetcam
cd ../jetcam/
python3 setup.py install
