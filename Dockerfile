FROM alpine:3.17

RUN apk add --no-cache python3-dev py3-pip \
    && pip install --upgrade pip

WORKDIR /home/app

COPY . /home/app

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["python", "src/app.py"]
