# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import datastream_pb2 as datastream__pb2


class GRPCDataStreamStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ClientStreaming = channel.stream_unary(
        '/datastream.GRPCDataStream/ClientStreaming',
        request_serializer=datastream__pb2.Request.SerializeToString,
        response_deserializer=datastream__pb2.Response.FromString,
        )


class GRPCDataStreamServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ClientStreaming(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GRPCDataStreamServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ClientStreaming': grpc.stream_unary_rpc_method_handler(
          servicer.ClientStreaming,
          request_deserializer=datastream__pb2.Request.FromString,
          response_serializer=datastream__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'datastream.GRPCDataStream', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
