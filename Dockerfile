FROM python:3-slim
WORKDIR /programas/ingesta
RUN pip3 install boto3 pandas pymysql cryptography sqlalchemy
COPY . .
CMD [ "python3", "./ingesta.py" ]
