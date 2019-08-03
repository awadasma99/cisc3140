FROM python:3

RUN apt-get update -y && \
    apt-get install -y python3 python3-dev python3-pip

COPY requirements.txt /app/requirements.txt
COPY /python_app/app.py /app/app.py

WORKDIR /app
ADD /python_app /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
