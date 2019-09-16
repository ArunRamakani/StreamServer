FROM python:2.7

WORKDIR /StreamServer

ENV PATH "$PATH:/StreamServer"


COPY server.py /StreamServer
COPY datastream_pb2_grpc.py /StreamServer
COPY datastream_pb2.py /StreamServer
COPY datastream.proto /StreamServer


RUN python -m pip install grpcio
RUN python -m pip install grpcio-tools googleapis-common-protos

CMD ["python", "./server.py"]

EXPOSE 23333
