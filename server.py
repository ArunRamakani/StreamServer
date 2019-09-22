
import threading
import time
import grpc

import datastream_pb2_grpc
import datastream_pb2
from concurrent import futures
from sys import argv

import sys
sys.path.insert(1, './client_blu')

import client_blu

# Host where teh server starts 
SERVER_ADDRESS = '[::]:50052'

# Receive business logic unit host adress as service discovery
script, bluhost = argv

# GRPC Service implementation class
class DataStreamServer(datastream_pb2_grpc.GRPCDataStreamServicer):

    # ClientStreaming Service implementation function
    def ClientStreaming(self, request_iterator, context):
        print("ClientStreaming called by client...")
        
        # Extract the security token from GRPC reguest - from metadata 
        metadata = context.invocation_metadata()
        metadata_dict = {}
        for c in metadata:
            metadata_dict[c.key] = c.value
        
        # Validate the security token and return failure on error
        if metadata_dict["network-international"] != "643524tr^#sX":
            print("ClientStreaming called failed authentication...")
            return datastream_pb2.Response(result=datastream_pb2.DataStreamResult.FAILURE)
         
        # Validate the streaming request and collect the usr object in an array
        users = []
        for request in request_iterator:
            #validate if the usr id is a proper integer
            try:
                request.user.id += 1
            except TypeError:
                return datastream_pb2.Response(result=datastream_pb2.DataStreamResult.FAILURE)
            # append users to array
            users.append(request.user)
        
        # call the grpc business logic unit client
        client_blu.server_streaming_method(bluhost, users)
    
   
        #  respond back to the client with success
        response = datastream_pb2.Response(result=datastream_pb2.DataStreamResult.SUCCESS)
        return response    

# Function to start the GRPC server and load GRP implementation call
def main():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    datastream_pb2_grpc.add_GRPCDataStreamServicer_to_server(DataStreamServer(), server)     
    
    server.add_insecure_port(SERVER_ADDRESS) 
    
    print("------------------start Python GRPC server")
    server.start()
    
    # Kill the server on interaprions and keep it alive
    try:
        while True:
            print("Server Running : threadcount %i" % (threading.active_count()))
            time.sleep(10)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        server.stop(0)
    

# The execution start point
if __name__ == '__main__':
    main()


