FROM python:3.6-stretch
WORKDIR /api
COPY . /api
RUN pip install -r /api/requeriments.txt
COPY . .
CMD python /api/app.py