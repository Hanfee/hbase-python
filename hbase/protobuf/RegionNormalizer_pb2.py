# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RegionNormalizer.proto

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
  name='RegionNormalizer.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x16RegionNormalizer.proto\".\n\x15RegionNormalizerState\x12\x15\n\rnormalizer_on\x18\x01 \x01(\x08\x42I\n*org.apache.hadoop.hbase.protobuf.generatedB\x16RegionNormalizerProtosH\x01\xa0\x01\x01')
)




_REGIONNORMALIZERSTATE = _descriptor.Descriptor(
  name='RegionNormalizerState',
  full_name='RegionNormalizerState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='normalizer_on', full_name='RegionNormalizerState.normalizer_on', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=26,
  serialized_end=72,
)

DESCRIPTOR.message_types_by_name['RegionNormalizerState'] = _REGIONNORMALIZERSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegionNormalizerState = _reflection.GeneratedProtocolMessageType('RegionNormalizerState', (_message.Message,), dict(
  DESCRIPTOR = _REGIONNORMALIZERSTATE,
  __module__ = 'RegionNormalizer_pb2'
  # @@protoc_insertion_point(class_scope:RegionNormalizerState)
  ))
_sym_db.RegisterMessage(RegionNormalizerState)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n*org.apache.hadoop.hbase.protobuf.generatedB\026RegionNormalizerProtosH\001\240\001\001'))
# @@protoc_insertion_point(module_scope)