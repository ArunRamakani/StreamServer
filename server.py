from concurrent import futures
import threading
import time
import grpc

import datastream_pb2_grpc
import datastream_pb2

SERVER_ADDRESS = 'localhost:23333'


class DataStreamServer(datastream_pb2_grpc.GRPCDataStreamServicer):

    def ClientStreaming(self, request_iterator, context):
        print("ClientStreaming called by client...")
        for request in request_iterator:
            print("Name = %s" % (request.user.name))
            print("User ID = %s" % (request.user.id))
            print("Message from User = %s" % (request.user.message))
            print("==================")
        response = datastream_pb2.Response(result=datastream_pb2.DataStreamResult.SUCCESS)
        return response    
    
def main():
    
    with open('server.key', 'rb') as f:
        private_key = f.read()
    with open('server.crt', 'rb') as f:
        cert_chain = f.read()
    server_creds = grpc.ssl_server_credentials( ( (private_key, cert_chain), ) )
    
    server = grpc.server(futures.ThreadPoolExecutor())
    datastream_pb2_grpc.add_GRPCDataStreamServicer_to_server(DataStreamServer(), server)     
    
    server.add_secure_port(SERVER_ADDRESS,server_creds) 
    
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


