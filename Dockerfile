FROM python:3.7
WORKDIR /python/cowserve
COPY requirements.txt . 
RUN pip install -r requirements.txt
RUN git clone -b library https://github.com/noaoh/pysay.git
COPY . /python/cowserve
EXPOSE 3031
EXPOSE 9191
CMD [ "/usr/local/bin/uwsgi", "--socket", "0.0.0.0:3031", "--wsgi-file",\
"rpc-cowsay-server.py", "--callable", "app", "--processes","4",\
"--threads", "2", "--stats", "0.0.0.0:9191", "--protocol=http" ]
