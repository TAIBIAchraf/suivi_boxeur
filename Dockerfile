# Choisir l'image de base à laquelle nous allons rajouter trt_pose
ARG BASE_IMAGE=nvcr.io/nvidia/dli/dli-nano-ai:v2.0.2-r32.7.1
FROM ${BASE_IMAGE}

# Cloner mon projet
RUN git clone https://github.com/TAIBIAchraf/suivi_boxeur.git

# Cloner Jetcam
RUN git clone https://github.com/NVIDIA-AI-IOT/jetcam

# Installer Pillow qui correspond à la version python 3.6
RUN pip3 install Pillow==8.4.0

# Cloner et installer torch2trt
RUN git clone https://github.com/NVIDIA-AI-IOT/torch2trt && \
	cd torch2trt && \
	python3 setup.py install && \
	cd ..

# Installer les Bibliothéques requises
RUN pip3 install tqdm cython pycocotools

# Cloner et installer trt_pose
RUN git clone https://github.com/NVIDIA-AI-IOT/trt_pose && \
	cd trt_pose && \
	python3 setup.py install && \
	cd ..
