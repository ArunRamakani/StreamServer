FROM python:2.7

WORKDIR /StreamServer
MKDIR /StreamServer/client_blu

ENV PATH "$PATH:/StreamServer"


COPY server.py /StreamServer
COPY datastream_pb2_grpc.py /StreamServer
COPY datastream_pb2.py /StreamServer
COPY datastream.proto /StreamServer

COPY ./client_blu/client_blu.proto /StreamServer/client_blu
COPY ./client_blu/datastreamblu_pb2_grpc.py /StreamServer/client_blu
COPY ./client_blu/datastreamblu_pb2.py /StreamServer/client_blu
COPY ./client_blu/datastreamblu.proto /StreamServer/client_blu


RUN python -m pip install grpcio
RUN python -m pip install grpcio-tools googleapis-common-protos

CMD ["sh", "-c", "python ./server.py ${server}"]

EXPOSE 23333
