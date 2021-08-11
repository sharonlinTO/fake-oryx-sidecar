FROM python:3.9

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5324

ENTRYPOINT ["python"]

CMD ["app.py"]