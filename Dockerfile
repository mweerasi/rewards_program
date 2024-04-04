FROM mambaorg/micromamba:0.23.0

# install docker-specific dependencies
USER root
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y \
    && apt-get install -y 'ffmpeg' 'libsm6' 'libxext6' 'libgl1-mesa-glx' 'xvfb'\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV DISPLAY :99.0

# logs directory
RUN mkdir -p /var/log

# rename conda/mamba environment to base, install dependencies
COPY environment.yml /tmp/environment.yml
RUN sed -i "1s/rewards-server/base/" /tmp/environment.yml

RUN micromamba install -y -f /tmp/environment.yml && \
    micromamba clean --all --yes

# App directory
WORKDIR /usr/src/app
COPY . .
