FROM python:3.7
WORKDIR /python/cowserve
COPY ./pysay/cows /usr/share/cows
COPY requirements.txt . 
RUN pip install -r requirements.txt
RUN git clone -b library https://github.com/noaoh/pysay.git
COPY . /python/cowserve
