FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install watchdog

COPY . /app/

RUN apt-get update \
    && apt-get install -y --no-install-recommends dialog openssh-server redis-server \
    && echo "root:Docker!" | chpasswd \
    && chmod u+x /app/entrypoint.sh
COPY sshd_config /etc/ssh/

RUN apt install -y redis-server tini

EXPOSE 80

CMD [ "/bin/bash", "/app/entrypoint.sh" ]