# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import ChatRPC_pb2 as ChatRPC__pb2


class ChatServidorStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ChatStream = channel.unary_stream(
        '/grpc.ChatServidor/ChatStream',
        request_serializer=ChatRPC__pb2.Vacio.SerializeToString,
        response_deserializer=ChatRPC__pb2.Mensaje.FromString,
        )
    self.EnviarMensaje = channel.unary_unary(
        '/grpc.ChatServidor/EnviarMensaje',
        request_serializer=ChatRPC__pb2.Mensaje.SerializeToString,
        response_deserializer=ChatRPC__pb2.Vacio.FromString,
        )
    self.HistorialChat = channel.unary_unary(
        '/grpc.ChatServidor/HistorialChat',
        request_serializer=ChatRPC__pb2.Mensaje.SerializeToString,
        response_deserializer=ChatRPC__pb2.Vacio.FromString,
        )
    self.ListaClientes = channel.unary_unary(
        '/grpc.ChatServidor/ListaClientes',
        request_serializer=ChatRPC__pb2.Mensaje.SerializeToString,
        response_deserializer=ChatRPC__pb2.Vacio.FromString,
        )


class ChatServidorServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ChatStream(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EnviarMensaje(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HistorialChat(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListaClientes(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ChatServidorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ChatStream': grpc.unary_stream_rpc_method_handler(
          servicer.ChatStream,
          request_deserializer=ChatRPC__pb2.Vacio.FromString,
          response_serializer=ChatRPC__pb2.Mensaje.SerializeToString,
      ),
      'EnviarMensaje': grpc.unary_unary_rpc_method_handler(
          servicer.EnviarMensaje,
          request_deserializer=ChatRPC__pb2.Mensaje.FromString,
          response_serializer=ChatRPC__pb2.Vacio.SerializeToString,
      ),
      'HistorialChat': grpc.unary_unary_rpc_method_handler(
          servicer.HistorialChat,
          request_deserializer=ChatRPC__pb2.Mensaje.FromString,
          response_serializer=ChatRPC__pb2.Vacio.SerializeToString,
      ),
      'ListaClientes': grpc.unary_unary_rpc_method_handler(
          servicer.ListaClientes,
          request_deserializer=ChatRPC__pb2.Mensaje.FromString,
          response_serializer=ChatRPC__pb2.Vacio.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc.ChatServidor', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
