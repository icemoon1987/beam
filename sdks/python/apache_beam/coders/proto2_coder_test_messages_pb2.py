#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sdks/java/core/src/main/proto/proto2_coder_test_messages.proto

import sys

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2

_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
  name='apache_beam/coders/proto2_coder_test_messages.proto',
  package='proto2_coder_test_messages',
  syntax='proto2',
  serialized_pb=_b('\n3apache_beam/coders/proto2_coder_test_messages.proto\x12\x1aproto2_coder_test_messages\"P\n\x08MessageA\x12\x0e\n\x06\x66ield1\x18\x01 \x01(\t\x12\x34\n\x06\x66ield2\x18\x02 \x03(\x0b\x32$.proto2_coder_test_messages.MessageB\"\x1a\n\x08MessageB\x12\x0e\n\x06\x66ield1\x18\x01 \x01(\x08\"\x10\n\x08MessageC*\x04\x08\x64\x10j\"\xad\x01\n\x0eMessageWithMap\x12\x46\n\x06\x66ield1\x18\x01 \x03(\x0b\x32\x36.proto2_coder_test_messages.MessageWithMap.Field1Entry\x1aS\n\x0b\x46ield1Entry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32$.proto2_coder_test_messages.MessageA:\x02\x38\x01\"V\n\x18ReferencesMessageWithMap\x12:\n\x06\x66ield1\x18\x01 \x03(\x0b\x32*.proto2_coder_test_messages.MessageWithMap:Z\n\x06\x66ield1\x12$.proto2_coder_test_messages.MessageC\x18\x65 \x01(\x0b\x32$.proto2_coder_test_messages.MessageA:Z\n\x06\x66ield2\x12$.proto2_coder_test_messages.MessageC\x18\x66 \x01(\x0b\x32$.proto2_coder_test_messages.MessageBB\x1c\n\x1aorg.apache.beam.sdk.coders')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


FIELD1_FIELD_NUMBER = 101
field1 = _descriptor.FieldDescriptor(
  name='field1', full_name='proto2_coder_test_messages.field1', index=0,
  number=101, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
FIELD2_FIELD_NUMBER = 102
field2 = _descriptor.FieldDescriptor(
  name='field2', full_name='proto2_coder_test_messages.field2', index=1,
  number=102, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_MESSAGEA = _descriptor.Descriptor(
  name='MessageA',
  full_name='proto2_coder_test_messages.MessageA',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field1', full_name='proto2_coder_test_messages.MessageA.field1', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field2', full_name='proto2_coder_test_messages.MessageA.field2', index=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=163,
)


_MESSAGEB = _descriptor.Descriptor(
  name='MessageB',
  full_name='proto2_coder_test_messages.MessageB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field1', full_name='proto2_coder_test_messages.MessageB.field1', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=165,
  serialized_end=191,
)


_MESSAGEC = _descriptor.Descriptor(
  name='MessageC',
  full_name='proto2_coder_test_messages.MessageC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(100, 106), ],
  oneofs=[
  ],
  serialized_start=193,
  serialized_end=209,
)


_MESSAGEWITHMAP_FIELD1ENTRY = _descriptor.Descriptor(
  name='Field1Entry',
  full_name='proto2_coder_test_messages.MessageWithMap.Field1Entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='proto2_coder_test_messages.MessageWithMap.Field1Entry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto2_coder_test_messages.MessageWithMap.Field1Entry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=302,
  serialized_end=385,
)

_MESSAGEWITHMAP = _descriptor.Descriptor(
  name='MessageWithMap',
  full_name='proto2_coder_test_messages.MessageWithMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field1', full_name='proto2_coder_test_messages.MessageWithMap.field1', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MESSAGEWITHMAP_FIELD1ENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=212,
  serialized_end=385,
)


_REFERENCESMESSAGEWITHMAP = _descriptor.Descriptor(
  name='ReferencesMessageWithMap',
  full_name='proto2_coder_test_messages.ReferencesMessageWithMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field1', full_name='proto2_coder_test_messages.ReferencesMessageWithMap.field1', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=387,
  serialized_end=473,
)

_MESSAGEA.fields_by_name['field2'].message_type = _MESSAGEB
_MESSAGEWITHMAP_FIELD1ENTRY.fields_by_name['value'].message_type = _MESSAGEA
_MESSAGEWITHMAP_FIELD1ENTRY.containing_type = _MESSAGEWITHMAP
_MESSAGEWITHMAP.fields_by_name['field1'].message_type = _MESSAGEWITHMAP_FIELD1ENTRY
_REFERENCESMESSAGEWITHMAP.fields_by_name['field1'].message_type = _MESSAGEWITHMAP
DESCRIPTOR.message_types_by_name['MessageA'] = _MESSAGEA
DESCRIPTOR.message_types_by_name['MessageB'] = _MESSAGEB
DESCRIPTOR.message_types_by_name['MessageC'] = _MESSAGEC
DESCRIPTOR.message_types_by_name['MessageWithMap'] = _MESSAGEWITHMAP
DESCRIPTOR.message_types_by_name['ReferencesMessageWithMap'] = _REFERENCESMESSAGEWITHMAP
DESCRIPTOR.extensions_by_name['field1'] = field1
DESCRIPTOR.extensions_by_name['field2'] = field2

MessageA = _reflection.GeneratedProtocolMessageType('MessageA', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGEA,
  __module__ = 'apache_beam.coders.proto2_coder_test_messages_pb2'
  # @@protoc_insertion_point(class_scope:proto2_coder_test_messages.MessageA)
  ))
_sym_db.RegisterMessage(MessageA)

MessageB = _reflection.GeneratedProtocolMessageType('MessageB', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGEB,
  __module__ = 'apache_beam.coders.proto2_coder_test_messages_pb2'
  # @@protoc_insertion_point(class_scope:proto2_coder_test_messages.MessageB)
  ))
_sym_db.RegisterMessage(MessageB)

MessageC = _reflection.GeneratedProtocolMessageType('MessageC', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGEC,
  __module__ = 'apache_beam.coders.proto2_coder_test_messages_pb2'
  # @@protoc_insertion_point(class_scope:proto2_coder_test_messages.MessageC)
  ))
_sym_db.RegisterMessage(MessageC)

MessageWithMap = _reflection.GeneratedProtocolMessageType('MessageWithMap', (_message.Message,), dict(

  Field1Entry = _reflection.GeneratedProtocolMessageType('Field1Entry', (_message.Message,), dict(
    DESCRIPTOR = _MESSAGEWITHMAP_FIELD1ENTRY,
    __module__ = 'apache_beam.coders.proto2_coder_test_messages_pb2'
    # @@protoc_insertion_point(class_scope:proto2_coder_test_messages.MessageWithMap.Field1Entry)
    ))
  ,
  DESCRIPTOR = _MESSAGEWITHMAP,
  __module__ = 'apache_beam.coders.proto2_coder_test_messages_pb2'
  # @@protoc_insertion_point(class_scope:proto2_coder_test_messages.MessageWithMap)
  ))
_sym_db.RegisterMessage(MessageWithMap)
_sym_db.RegisterMessage(MessageWithMap.Field1Entry)

ReferencesMessageWithMap = _reflection.GeneratedProtocolMessageType('ReferencesMessageWithMap', (_message.Message,), dict(
  DESCRIPTOR = _REFERENCESMESSAGEWITHMAP,
  __module__ = 'apache_beam.coders.proto2_coder_test_messages_pb2'
  # @@protoc_insertion_point(class_scope:proto2_coder_test_messages.ReferencesMessageWithMap)
  ))
_sym_db.RegisterMessage(ReferencesMessageWithMap)

field1.message_type = _MESSAGEA
MessageC.RegisterExtension(field1)
field2.message_type = _MESSAGEB
MessageC.RegisterExtension(field2)

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032org.apache.beam.sdk.coders'))
_MESSAGEWITHMAP_FIELD1ENTRY.has_options = True
_MESSAGEWITHMAP_FIELD1ENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
