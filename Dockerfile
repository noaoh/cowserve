FROM python:3.6
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN git clone -b library https://github.com/noaoh/pysay.git
COPY  ./app /app
EXPOSE 443
EXPOSE 9191
CMD [ "/usr/local/bin/uwsgi", "--socket", "0.0.0.0:443", "--wsgi-file",\
"main.py", "--callable", "app", "--processes", "4",\
"--threads", "2", "--stats", "0.0.0.0:9191", "--protocol=http" ]
