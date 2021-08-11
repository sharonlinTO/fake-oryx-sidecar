# Need Go base image in order to run go build later
FROM golang:1.16-alpine3.14

# Add enough to get Python flask app
RUN apk update \
    && apk upgrade \  
    && apk add python3 \
    && apk add py3-pip

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["app.py"]