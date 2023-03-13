ARG BASE_IMAGE=nvcr.io/nvidia/dli/dli-nano-ai:v2.0.2-r32.7.1
FROM ${BASE_IMAGE}

RUN git clone https://github.com/NVIDIA-AI-IOT/torch2trt && \
    WORKDIR "/torch2trt" && \
    python3 setup.py install

RUN pip3 install tqdm cython pycocotools

RUN apt-get install python3-matplotlib

RUN git clone https://github.com/NVIDIA-AI-IOT/trt_pose && \
	WORKDIR "/trt_pose" && \
	python3 setup.py install