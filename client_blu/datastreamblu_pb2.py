# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: datastreamblu.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='datastreamblu.proto',
  package='datastreamblu',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13\x64\x61tastreamblu.proto\x12\rdatastreamblu\"1\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\",\n\x07Request\x12!\n\x04user\x18\x01 \x01(\x0b\x32\x13.datastreamblu.User\";\n\x08Response\x12/\n\x06result\x18\x01 \x01(\x0e\x32\x1f.datastreamblu.DataStreamResult*,\n\x10\x44\x61taStreamResult\x12\x0b\n\x07SUCCESS\x10\x00\x12\x0b\n\x07\x46\x41ILURE\x10\x01\x32Y\n\x11GRPCDataStreamBLU\x12\x44\n\x0fServerStreaming\x12\x16.datastreamblu.Request\x1a\x17.datastreamblu.Response(\x01\x62\x06proto3')
)

_DATASTREAMRESULT = _descriptor.EnumDescriptor(
  name='DataStreamResult',
  full_name='datastreamblu.DataStreamResult',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=196,
  serialized_end=240,
)
_sym_db.RegisterEnumDescriptor(_DATASTREAMRESULT)

DataStreamResult = enum_type_wrapper.EnumTypeWrapper(_DATASTREAMRESULT)
SUCCESS = 0
FAILURE = 1



_USER = _descriptor.Descriptor(
  name='User',
  full_name='datastreamblu.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='datastreamblu.User.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='datastreamblu.User.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='datastreamblu.User.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=87,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='datastreamblu.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='datastreamblu.Request.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=133,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='datastreamblu.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='datastreamblu.Response.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=194,
)

_REQUEST.fields_by_name['user'].message_type = _USER
_RESPONSE.fields_by_name['result'].enum_type = _DATASTREAMRESULT
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.enum_types_by_name['DataStreamResult'] = _DATASTREAMRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), dict(
  DESCRIPTOR = _USER,
  __module__ = 'datastreamblu_pb2'
  # @@protoc_insertion_point(class_scope:datastreamblu.User)
  ))
_sym_db.RegisterMessage(User)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'datastreamblu_pb2'
  # @@protoc_insertion_point(class_scope:datastreamblu.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'datastreamblu_pb2'
  # @@protoc_insertion_point(class_scope:datastreamblu.Response)
  ))
_sym_db.RegisterMessage(Response)



_GRPCDATASTREAMBLU = _descriptor.ServiceDescriptor(
  name='GRPCDataStreamBLU',
  full_name='datastreamblu.GRPCDataStreamBLU',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=242,
  serialized_end=331,
  methods=[
  _descriptor.MethodDescriptor(
    name='ServerStreaming',
    full_name='datastreamblu.GRPCDataStreamBLU.ServerStreaming',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GRPCDATASTREAMBLU)

DESCRIPTOR.services_by_name['GRPCDataStreamBLU'] = _GRPCDATASTREAMBLU

# @@protoc_insertion_point(module_scope)
