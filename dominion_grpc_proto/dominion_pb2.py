# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dominion.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dominion.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x64ominion.proto\"\x1a\n\nPlayerInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x14\n\x04\x43\x61rd\x12\x0c\n\x04name\x18\x01 \x01(\t\"%\n\x07Message\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\"%\n\x08Response\x12\n\n\x02ok\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"6\n\x0e\x41\x63tionResponse\x12\x13\n\x04\x63\x61rd\x18\x01 \x01(\x0b\x32\x05.Card\x12\x0f\n\x07payload\x18\x02 \x01(\t2\xdc\x01\n\x0e\x44ominionServer\x12!\n\x04Join\x12\x0b.PlayerInfo\x1a\x08.Message\"\x00\x30\x01\x12!\n\x05Start\x12\x0b.PlayerInfo\x1a\t.Response\"\x00\x12\x1e\n\x08PlayCard\x12\x05.Card\x1a\t.Response\"\x00\x12\x19\n\x03\x42uy\x12\x05.Card\x1a\t.Response\"\x00\x12 \n\x04\x44one\x12\x0b.PlayerInfo\x1a\t.Response\"\x00\x12\'\n\x07Respond\x12\x0f.ActionResponse\x1a\t.Response\"\x00\x62\x06proto3'
)




_PLAYERINFO = _descriptor.Descriptor(
  name='PlayerInfo',
  full_name='PlayerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='PlayerInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=18,
  serialized_end=44,
)


_CARD = _descriptor.Descriptor(
  name='Card',
  full_name='Card',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Card.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=46,
  serialized_end=66,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Message.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='Message.data', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=68,
  serialized_end=105,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ok', full_name='Response.ok', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='Response.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=107,
  serialized_end=144,
)


_ACTIONRESPONSE = _descriptor.Descriptor(
  name='ActionResponse',
  full_name='ActionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='card', full_name='ActionResponse.card', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='ActionResponse.payload', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=146,
  serialized_end=200,
)

_ACTIONRESPONSE.fields_by_name['card'].message_type = _CARD
DESCRIPTOR.message_types_by_name['PlayerInfo'] = _PLAYERINFO
DESCRIPTOR.message_types_by_name['Card'] = _CARD
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['ActionResponse'] = _ACTIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlayerInfo = _reflection.GeneratedProtocolMessageType('PlayerInfo', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERINFO,
  '__module__' : 'dominion_pb2'
  # @@protoc_insertion_point(class_scope:PlayerInfo)
  })
_sym_db.RegisterMessage(PlayerInfo)

Card = _reflection.GeneratedProtocolMessageType('Card', (_message.Message,), {
  'DESCRIPTOR' : _CARD,
  '__module__' : 'dominion_pb2'
  # @@protoc_insertion_point(class_scope:Card)
  })
_sym_db.RegisterMessage(Card)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'dominion_pb2'
  # @@protoc_insertion_point(class_scope:Message)
  })
_sym_db.RegisterMessage(Message)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'dominion_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  })
_sym_db.RegisterMessage(Response)

ActionResponse = _reflection.GeneratedProtocolMessageType('ActionResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACTIONRESPONSE,
  '__module__' : 'dominion_pb2'
  # @@protoc_insertion_point(class_scope:ActionResponse)
  })
_sym_db.RegisterMessage(ActionResponse)



_DOMINIONSERVER = _descriptor.ServiceDescriptor(
  name='DominionServer',
  full_name='DominionServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=203,
  serialized_end=423,
  methods=[
  _descriptor.MethodDescriptor(
    name='Join',
    full_name='DominionServer.Join',
    index=0,
    containing_service=None,
    input_type=_PLAYERINFO,
    output_type=_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Start',
    full_name='DominionServer.Start',
    index=1,
    containing_service=None,
    input_type=_PLAYERINFO,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PlayCard',
    full_name='DominionServer.PlayCard',
    index=2,
    containing_service=None,
    input_type=_CARD,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Buy',
    full_name='DominionServer.Buy',
    index=3,
    containing_service=None,
    input_type=_CARD,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Done',
    full_name='DominionServer.Done',
    index=4,
    containing_service=None,
    input_type=_PLAYERINFO,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Respond',
    full_name='DominionServer.Respond',
    index=5,
    containing_service=None,
    input_type=_ACTIONRESPONSE,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DOMINIONSERVER)

DESCRIPTOR.services_by_name['DominionServer'] = _DOMINIONSERVER

# @@protoc_insertion_point(module_scope)
