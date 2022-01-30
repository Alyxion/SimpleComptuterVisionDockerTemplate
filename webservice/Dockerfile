FROM jjanzic/docker-python3-opencv@sha256:4d62a19be279775d9b8938cd097530e1b7102ce50445df0b26d19590a9fea90b as webbaseimage
COPY requirements.txt requirements.txt
RUN apt-get update -y
RUN apt install libgl1-mesa-glx -y
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

FROM webbaseimage as webservice
EXPOSE 5000:5000
ENV FLASK_APP=main.py
ENV FLASK_ENV=development
WORKDIR /app
# TODO Uncomment the COPY . . below and remove the --reload from the start command arguments when you are ready
# TODO to ship your docker container.
# COPY . .
CMD ["gunicorn", "main:app", "-w", "2", "--threads", "4", "-b", "0.0.0.0:5000", "--reload"]