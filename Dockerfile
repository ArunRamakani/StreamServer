FROM python:2.7

WORKDIR /StreamServer
RUN mkdir /StreamServer/client_blu

ENV PATH "$PATH:/StreamServer"


# Bundle app source
COPY . .


RUN python -m pip install grpcio
RUN python -m pip install grpcio-tools googleapis-common-protos

CMD ["sh", "-c", "python ./server.py ${server}"]

EXPOSE 23333
