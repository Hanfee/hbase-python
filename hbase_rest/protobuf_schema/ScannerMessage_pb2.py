# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ScannerMessage.proto

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
  name='ScannerMessage.proto',
  package='org.apache.hadoop.hbase_rest.rest.protobuf.generated',
  syntax='proto2',
  serialized_pb=_b('\n\x14ScannerMessage.proto\x12/org.apache.hadoop.hbase_rest.rest.protobuf.generated\"\xca\x01\n\x07Scanner\x12\x10\n\x08startRow\x18\x01 \x01(\x0c\x12\x0e\n\x06\x65ndRow\x18\x02 \x01(\x0c\x12\x0f\n\x07\x63olumns\x18\x03 \x03(\x0c\x12\r\n\x05\x62\x61tch\x18\x04 \x01(\x05\x12\x11\n\tstartTime\x18\x05 \x01(\x03\x12\x0f\n\x07\x65ndTime\x18\x06 \x01(\x03\x12\x13\n\x0bmaxVersions\x18\x07 \x01(\x05\x12\x0e\n\x06\x66ilter\x18\x08 \x01(\t\x12\x0f\n\x07\x63\x61\x63hing\x18\t \x01(\x05\x12\x0e\n\x06labels\x18\n \x03(\t\x12\x13\n\x0b\x63\x61\x63heBlocks\x18\x0b \x01(\x08')
)




_SCANNER = _descriptor.Descriptor(
  name='Scanner',
  full_name='org.apache.hadoop.hbase_rest.rest.protobuf.generated.Scanner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='startRow', full_name='org.apache.hadoop.hbase_rest.rest.protobuf.generated.Scanner.startRow', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endRow', full_name='org.apache.hadoop.hbase_rest.rest.protobuf.generated.Scanner.endRow', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='columns', full_name='org.apache.hadoop.hbase_rest.rest.protobuf.generated.Scanner.columns', index=2,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch', full_name='org.apache.hadoop.hbase_rest.rest.protobuf.generated.Scanner.batch', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='org.apache.hadoop.hbase_rest.rest.protobuf.generated.Scanner.startTime', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='org.apache.hadoop.hbase_rest.rest.protobuf.generated.Scanner.endTime', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxVersions', full_name='org.apache.hadoop.hbase_rest.rest.protobuf.generated.Scanner.maxVersions', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='org.apache.hadoop.hbase_rest.rest.protobuf.generated.Scanner.filter', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='caching', full_name='org.apache.hadoop.hbase_rest.rest.protobuf.generated.Scanner.caching', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='org.apache.hadoop.hbase_rest.rest.protobuf.generated.Scanner.labels', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cacheBlocks', full_name='org.apache.hadoop.hbase_rest.rest.protobuf.generated.Scanner.cacheBlocks', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=276,
)

DESCRIPTOR.message_types_by_name['Scanner'] = _SCANNER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Scanner = _reflection.GeneratedProtocolMessageType('Scanner', (_message.Message,), dict(
  DESCRIPTOR = _SCANNER,
  __module__ = 'ScannerMessage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.hadoop.hbase_rest.rest.protobuf.generated.Scanner)
  ))
_sym_db.RegisterMessage(Scanner)


# @@protoc_insertion_point(module_scope)