FROM python:3.6-alpine
WORKDIR /usr/src/app
ENV FLASK_PORT 8080
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app .
EXPOSE $FLASK_PORT
CMD [ "python", "app.py" ]
