from concurrent import futures
import threading
import time
import grpc

import datastream_pb2_grpc
import datastream_pb2

SERVER_ADDRESS = '[::]:50051'


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
        
        for request in request_iterator:
            print("Name = %s" % (request.user.name))
            print("User ID = %s" % (request.user.id))
            print("Message from User = %s" % (request.user.message))
            print("==================")
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


