###########
# BUILDER #
###########

FROM python:3.8-slim-buster as builder

RUN apt-get -y update

RUN apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-base-dev \
    libavcodec-dev \
    libavformat-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    software-properties-common \
    zip \
    gcc \
    musl-dev \
    netcat \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN cd ~ && \
    mkdir -p dlib && \
    git clone https://github.com/davisking/dlib.git dlib/ && \
    cd  dlib/ && \
    python3 setup.py install

WORKDIR /usr/src/py_face_recognition

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/py_face_recognition/wheels -r requirements.txt

#########
# FINAL #
#########

FROM python:3.8-slim-buster

RUN apt-get -y update

RUN apt-get install -y --fix-missing \
    netcat \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-base-dev \
    libavcodec-dev \
    libavformat-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    software-properties-common

COPY --from=builder /usr/src/py_face_recognition/wheels /wheels
COPY --from=builder /usr/src/py_face_recognition/requirements.txt .
RUN pip install --no-cache /wheels/*

COPY ./entrypoint.sh .

COPY . .

ENTRYPOINT ["/usr/src/py_face_recognition/entrypoint.sh"]
