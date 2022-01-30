FROM jjanzic/docker-python3-opencv@sha256:4d62a19be279775d9b8938cd097530e1b7102ce50445df0b26d19590a9fea90b as streamlitbase
WORKDIR /app
COPY requirements.txt requirements.txt
RUN apt-get update -y
RUN apt install libgl1-mesa-glx -y
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

FROM streamlitbase as uiwebservice
EXPOSE 5002:5002
WORKDIR /root
COPY .streamlit .streamlit
RUN echo $HOME
RUN ls $HOME
WORKDIR /app
# TODO: Uncomment the line below when you want to ship this container
# COPY ./source .
CMD ["streamlit", "run", "frontend.py", "--server.port", "5002"]