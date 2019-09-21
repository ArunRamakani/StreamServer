from concurrent import futures
import threading
import time
import grpc

import datastream_pb2_grpc
import datastream_pb2

import client_blu/client_blu

from sys import argv

SERVER_ADDRESS = '[::]:50051'

script, bluhost = argv
    
client_blu_stub = client_blu.initialize_blu_client(bluhost)


class DataStreamServer(datastream_pb2_grpc.GRPCDataStreamServicer):

    def ClientStreaming(self, request_iterator, context):
        print("ClientStreaming called by client...")
        metadata = context.invocation_metadata()
        metadata_dict = {}
        for c in metadata:
            metadata_dict[c.key] = c.value
            
        if metadata_dict["network-international"] != "643524tr^#sX":
            print("ClientStreaming called failed authentication...")
            response = datastream_pb2.Response(result=datastream_pb2.DataStreamResult.FAILURE)
            return response    
        
        users = []
        
        for request in request_iterator:
            users.append(request.user)
        
        client_blu.server_streaming(client_blu_stub, users)
            
        response = datastream_pb2.Response(result=datastream_pb2.DataStreamResult.SUCCESS)
        return response    
    
def main():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    datastream_pb2_grpc.add_GRPCDataStreamServicer_to_server(DataStreamServer(), server)     
    
    server.add_insecure_port(SERVER_ADDRESS) 
    
    print("------------------start Python GRPC server")
    server.start()
    
    
    
    try:
        while True:
            print("Server Running : threadcount %i" % (threading.active_count()))
            time.sleep(10)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        server.stop(0)
    
    
if __name__ == '__main__':
    main()


