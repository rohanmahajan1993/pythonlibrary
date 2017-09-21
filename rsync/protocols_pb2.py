# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protocols.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protocols.proto',
  package='RSynce',
  syntax='proto3',
  serialized_pb=_b('\n\x0fprotocols.proto\x12\x06RSynce\"O\n\rClientRequest\x12\x15\n\rdirectoryName\x18\x01 \x01(\t\x12\'\n\x0b\x63lientFiles\x18\x02 \x03(\x0b\x32\x12.RSynce.ClientFile\"R\n\nClientFile\x12\x1a\n\x04\x66ile\x18\x01 \x01(\x0b\x32\x0c.RSynce.File\x12(\n\x0c\x63lientHashes\x18\x02 \x03(\x0b\x32\x12.RSynce.ClientHash\"9\n\nClientHash\x12\x12\n\nsimpleHash\x18\x01 \x01(\x05\x12\x17\n\x0f\x63omplicatedHash\x18\x02 \x01(\x0c\"\x80\x01\n\x0eServerResponse\x12!\n\x08newFiles\x18\x01 \x03(\x0b\x32\x0f.RSynce.NewFile\x12\"\n\x0c\x64\x65letedFiles\x18\x02 \x03(\x0b\x32\x0c.RSynce.File\x12\'\n\x0b\x65\x64itedFiles\x18\x03 \x03(\x0b\x32\x12.RSynce.EditedFile\"C\n\nEditedFile\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12#\n\tfileEdits\x18\x02 \x03(\x0b\x32\x10.RSynce.FileEdit\"^\n\x08\x46ileEdit\x12\x15\n\risBlockNumber\x18\x01 \x01(\x08\x12\x13\n\x0b\x62lockNumber\x18\x02 \x01(\x05\x12\x11\n\tnumBlocks\x18\x03 \x01(\x05\x12\x13\n\x0b\x66ileContent\x18\x04 \x01(\x0c\":\n\x07NewFile\x12\x1a\n\x04\x66ile\x18\x01 \x01(\x0b\x32\x0c.RSynce.File\x12\x13\n\x0b\x66ileContent\x18\x02 \x01(\x0c\"-\n\x04\x46ile\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x13\n\x0bisDirectory\x18\x02 \x01(\x08\x32N\n\x0cRsyncService\x12>\n\x0bRsyncMethod\x12\x15.RSynce.ClientRequest\x1a\x16.RSynce.ServerResponse\"\x00\x62\x06proto3')
)




_CLIENTREQUEST = _descriptor.Descriptor(
  name='ClientRequest',
  full_name='RSynce.ClientRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='directoryName', full_name='RSynce.ClientRequest.directoryName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clientFiles', full_name='RSynce.ClientRequest.clientFiles', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=106,
)


_CLIENTFILE = _descriptor.Descriptor(
  name='ClientFile',
  full_name='RSynce.ClientFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file', full_name='RSynce.ClientFile.file', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clientHashes', full_name='RSynce.ClientFile.clientHashes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=190,
)


_CLIENTHASH = _descriptor.Descriptor(
  name='ClientHash',
  full_name='RSynce.ClientHash',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='simpleHash', full_name='RSynce.ClientHash.simpleHash', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='complicatedHash', full_name='RSynce.ClientHash.complicatedHash', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=192,
  serialized_end=249,
)


_SERVERRESPONSE = _descriptor.Descriptor(
  name='ServerResponse',
  full_name='RSynce.ServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='newFiles', full_name='RSynce.ServerResponse.newFiles', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deletedFiles', full_name='RSynce.ServerResponse.deletedFiles', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='editedFiles', full_name='RSynce.ServerResponse.editedFiles', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=252,
  serialized_end=380,
)


_EDITEDFILE = _descriptor.Descriptor(
  name='EditedFile',
  full_name='RSynce.EditedFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='RSynce.EditedFile.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fileEdits', full_name='RSynce.EditedFile.fileEdits', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=382,
  serialized_end=449,
)


_FILEEDIT = _descriptor.Descriptor(
  name='FileEdit',
  full_name='RSynce.FileEdit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isBlockNumber', full_name='RSynce.FileEdit.isBlockNumber', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blockNumber', full_name='RSynce.FileEdit.blockNumber', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numBlocks', full_name='RSynce.FileEdit.numBlocks', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fileContent', full_name='RSynce.FileEdit.fileContent', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=451,
  serialized_end=545,
)


_NEWFILE = _descriptor.Descriptor(
  name='NewFile',
  full_name='RSynce.NewFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file', full_name='RSynce.NewFile.file', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fileContent', full_name='RSynce.NewFile.fileContent', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=547,
  serialized_end=605,
)


_FILE = _descriptor.Descriptor(
  name='File',
  full_name='RSynce.File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='RSynce.File.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isDirectory', full_name='RSynce.File.isDirectory', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=607,
  serialized_end=652,
)

_CLIENTREQUEST.fields_by_name['clientFiles'].message_type = _CLIENTFILE
_CLIENTFILE.fields_by_name['file'].message_type = _FILE
_CLIENTFILE.fields_by_name['clientHashes'].message_type = _CLIENTHASH
_SERVERRESPONSE.fields_by_name['newFiles'].message_type = _NEWFILE
_SERVERRESPONSE.fields_by_name['deletedFiles'].message_type = _FILE
_SERVERRESPONSE.fields_by_name['editedFiles'].message_type = _EDITEDFILE
_EDITEDFILE.fields_by_name['fileEdits'].message_type = _FILEEDIT
_NEWFILE.fields_by_name['file'].message_type = _FILE
DESCRIPTOR.message_types_by_name['ClientRequest'] = _CLIENTREQUEST
DESCRIPTOR.message_types_by_name['ClientFile'] = _CLIENTFILE
DESCRIPTOR.message_types_by_name['ClientHash'] = _CLIENTHASH
DESCRIPTOR.message_types_by_name['ServerResponse'] = _SERVERRESPONSE
DESCRIPTOR.message_types_by_name['EditedFile'] = _EDITEDFILE
DESCRIPTOR.message_types_by_name['FileEdit'] = _FILEEDIT
DESCRIPTOR.message_types_by_name['NewFile'] = _NEWFILE
DESCRIPTOR.message_types_by_name['File'] = _FILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientRequest = _reflection.GeneratedProtocolMessageType('ClientRequest', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTREQUEST,
  __module__ = 'protocols_pb2'
  # @@protoc_insertion_point(class_scope:RSynce.ClientRequest)
  ))
_sym_db.RegisterMessage(ClientRequest)

ClientFile = _reflection.GeneratedProtocolMessageType('ClientFile', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTFILE,
  __module__ = 'protocols_pb2'
  # @@protoc_insertion_point(class_scope:RSynce.ClientFile)
  ))
_sym_db.RegisterMessage(ClientFile)

ClientHash = _reflection.GeneratedProtocolMessageType('ClientHash', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTHASH,
  __module__ = 'protocols_pb2'
  # @@protoc_insertion_point(class_scope:RSynce.ClientHash)
  ))
_sym_db.RegisterMessage(ClientHash)

ServerResponse = _reflection.GeneratedProtocolMessageType('ServerResponse', (_message.Message,), dict(
  DESCRIPTOR = _SERVERRESPONSE,
  __module__ = 'protocols_pb2'
  # @@protoc_insertion_point(class_scope:RSynce.ServerResponse)
  ))
_sym_db.RegisterMessage(ServerResponse)

EditedFile = _reflection.GeneratedProtocolMessageType('EditedFile', (_message.Message,), dict(
  DESCRIPTOR = _EDITEDFILE,
  __module__ = 'protocols_pb2'
  # @@protoc_insertion_point(class_scope:RSynce.EditedFile)
  ))
_sym_db.RegisterMessage(EditedFile)

FileEdit = _reflection.GeneratedProtocolMessageType('FileEdit', (_message.Message,), dict(
  DESCRIPTOR = _FILEEDIT,
  __module__ = 'protocols_pb2'
  # @@protoc_insertion_point(class_scope:RSynce.FileEdit)
  ))
_sym_db.RegisterMessage(FileEdit)

NewFile = _reflection.GeneratedProtocolMessageType('NewFile', (_message.Message,), dict(
  DESCRIPTOR = _NEWFILE,
  __module__ = 'protocols_pb2'
  # @@protoc_insertion_point(class_scope:RSynce.NewFile)
  ))
_sym_db.RegisterMessage(NewFile)

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), dict(
  DESCRIPTOR = _FILE,
  __module__ = 'protocols_pb2'
  # @@protoc_insertion_point(class_scope:RSynce.File)
  ))
_sym_db.RegisterMessage(File)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class RsyncServiceStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.RsyncMethod = channel.unary_unary(
          '/RSynce.RsyncService/RsyncMethod',
          request_serializer=ClientRequest.SerializeToString,
          response_deserializer=ServerResponse.FromString,
          )


  class RsyncServiceServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def RsyncMethod(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_RsyncServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'RsyncMethod': grpc.unary_unary_rpc_method_handler(
            servicer.RsyncMethod,
            request_deserializer=ClientRequest.FromString,
            response_serializer=ServerResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'RSynce.RsyncService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaRsyncServiceServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def RsyncMethod(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaRsyncServiceStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def RsyncMethod(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    RsyncMethod.future = None


  def beta_create_RsyncService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('RSynce.RsyncService', 'RsyncMethod'): ClientRequest.FromString,
    }
    response_serializers = {
      ('RSynce.RsyncService', 'RsyncMethod'): ServerResponse.SerializeToString,
    }
    method_implementations = {
      ('RSynce.RsyncService', 'RsyncMethod'): face_utilities.unary_unary_inline(servicer.RsyncMethod),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_RsyncService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('RSynce.RsyncService', 'RsyncMethod'): ClientRequest.SerializeToString,
    }
    response_deserializers = {
      ('RSynce.RsyncService', 'RsyncMethod'): ServerResponse.FromString,
    }
    cardinalities = {
      'RsyncMethod': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'RSynce.RsyncService', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
