import time
import grpc

import datastreamblu_pb2_grpc
import datastreamblu_pb2

from grpc._cython.cygrpc import CompressionAlgorithm
from grpc._cython.cygrpc import CompressionLevel

def server_streaming(arr):
    
    print("--------------Call ClientStreaming Method Begin--------------")
    
    def request_messages(stub, messageArr):
    for i in range(len(messageArr)):
        request = datastreamblu_pb2.Request(user=(datastreamblu_pb2.User(id=messageArr[i].id, name=messageArr[i].name, message=messageArr[i].message)))
        yield request

    response = stub.ServerStreaming(request_messages(arr))
    
    print("resp from server with status=%s" % (response.result))
    
    if response.result == 0:
        print("--------------Call ServerStreaming Over With Success---------------")
    else:
        print("--------------Call ServerStreaming Over With Failure---------------")


def initialize_blu_client(bluhost):
    chan_ops = [('grpc.default_compression_algorithm', CompressionAlgorithm.gzip),
            ('grpc.grpc.default_compression_level', CompressionLevel.high)]
 
    print(bluhost)
    with grpc.insecure_channel(bluhost, chan_ops) as channel:
        return datastreamblu_pb2_grpc.GRPCDataStreamBLUStub(channel)



            
            