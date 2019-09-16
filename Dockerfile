FROM python:3.6-stretch
WORKDIR /api
COPY . /api
RUN wget https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5
RUN pip install -r /api/requeriments.txt
COPY . .
CMD python /api/app.py