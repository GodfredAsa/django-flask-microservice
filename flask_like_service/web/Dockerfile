#FROM python:3.9
#WORKDIR /web
#COPY requirements.txt .
#RUN pip install -r requirements.txt
#COPY . .
#CMD python web.py

FROM python:3.9
WORKDIR usr/usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
#CMD python app.py