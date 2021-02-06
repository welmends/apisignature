FROM python:3.8-slim

LABEL maintainer="NONE"

ENV TZ=America/Fortaleza

COPY . /home/code

RUN apt update ; \
    apt install libgl1-mesa-glx -y ; \
    apt install libgtk2.0-dev -y ; \
    apt install g++ -y

RUN pip install --no-cache-dir scikit-build ; pip install -r /home/code/requirements.txt

RUN apt clean

EXPOSE 9090

CMD ["python3", "/home/code/server.py", "release"]
