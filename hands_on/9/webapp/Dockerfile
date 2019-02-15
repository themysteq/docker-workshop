FROM python:3.6-alpine
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .
ENV FLASK_PORT 5000
CMD [ "python", "app.py" ]
