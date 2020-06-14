FROM python:3.6.4

RUN apt-get install bash
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

# download the cloudsql proxy
RUN wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O /usr/src/app/cloud_sql_proxy
# make cloudsql proxy executable
RUN chmod +x /usr/src/app/cloud_sql_proxy

RUN ln -sf /dev/stdout /var/log/access.log && \
    ln -sf /dev/stderr /var/log/error.log

ADD . /usr/src/app
RUN chmod +x run.sh
CMD ["./run.sh"]
