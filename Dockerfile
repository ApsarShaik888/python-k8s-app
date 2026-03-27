#import a python image from dockerhub
FROM python:3.9-alpine

#set working directory inside of container
WORKDIR /app

#copying the file to destination path /app
COPY app.py .

RUN chmod +x app.py
#command to run inside of container
CMD [ "python","-u","app.py" ]


