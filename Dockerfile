FROM mongo:5
RUN mkdir -p /opt/keyfile
RUN openssl rand -base64 756 > /opt/keyfile/keyfile
RUN chmod 600 /opt/keyfile/keyfile
RUN chown 999 /opt/keyfile/keyfile
RUN chgrp 999 /opt/keyfile/keyfile

CMD ["mongod", "--replSet", "rs0", "--bind_ip_all", "--keyFile", "/opt/keyfile/keyfile"]
