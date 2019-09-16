FROM python:3.6-stretch
RUN wget https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5
WORKDIR /api
COPY . /api
RUN pip install -r /api/requeriments.txt
COPY . .
CMD python /api/app.py