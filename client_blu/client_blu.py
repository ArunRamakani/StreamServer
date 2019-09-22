import time
import grpc

import datastreamblu_pb2_grpc
import datastreamblu_pb2

from grpc._cython.cygrpc import CompressionAlgorithm
from grpc._cython.cygrpc import CompressionLevel

 #  BLU GRPC server call
def server_streaming(stub, messageArr):
    print("--------------Call server_streaming Method Begin--------------")

    # loop the request for  BLU GRPC server request streaming
    def request_messages(messageArr):
        for mess in messageArr:
            request = datastreamblu_pb2.Request(user=(datastreamblu_pb2.User(id=mess.id, name=mess.name, message=mess.message)))
            yield request
            
            
    response = stub.ServerStreaming(request_messages(messageArr))
    print("resp from server with status=%s" % (response.result))
    if response.result == 0:
        print("--------------Call ClientStreamingMethod Over With Success---------------")
    else:
        print("--------------Call ClientStreamingMethod Over With Failure---------------")

# Entry point for BLU GRPC client
def server_streaming_method(bluhost, messageArr):
    # options to compress the request
    chan_ops = [('grpc.default_compression_algorithm', CompressionAlgorithm.gzip),
            ('grpc.grpc.default_compression_level', CompressionLevel.high)]
 
    print(bluhost)
    # connect BLU GRPC server
    with grpc.insecure_channel(bluhost, chan_ops) as channel:
        stub = datastreamblu_pb2_grpc.GRPCDataStreamBLUStub(channel)
        server_streaming(stub, messageArr)
        

            
            