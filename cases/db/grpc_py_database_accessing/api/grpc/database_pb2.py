# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: database.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x64\x61tabase.proto\x12\x03\x61pi\"R\n\x0cGetDbRequest\x12\x0f\n\x07\x63olumns\x18\x01 \x01(\t\x12\r\n\x05table\x18\x02 \x01(\t\x12\x11\n\tcondition\x18\x03 \x01(\t\x12\x0f\n\x07\x64\x62_host\x18\x04 \x01(\t\"-\n\rGetDbResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"R\n\x0fInsertDbRequest\x12\r\n\x05table\x18\x01 \x01(\t\x12\x0f\n\x07\x63olumns\x18\x02 \x01(\t\x12\x0e\n\x06values\x18\x03 \x01(\t\x12\x0f\n\x07\x64\x62_host\x18\x04 \x01(\t\"\"\n\x10InsertDbResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"D\n\x0f\x44\x65leteDbRequest\x12\r\n\x05table\x18\x01 \x01(\t\x12\x11\n\tcondition\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x62_host\x18\x03 \x01(\t\"\"\n\x10\x44\x65leteDbResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"T\n\x0fUpdateDbRequest\x12\r\n\x05table\x18\x01 \x01(\t\x12\x0e\n\x06to_set\x18\x02 \x01(\t\x12\x11\n\tcondition\x18\x03 \x01(\t\x12\x0f\n\x07\x64\x62_host\x18\x04 \x01(\t\"\"\n\x10UpdateDbResponse\x12\x0e\n\x06status\x18\x01 \x01(\t2\xed\x01\n\x08\x44\x61tabase\x12\x30\n\x05GetDb\x12\x11.api.GetDbRequest\x1a\x12.api.GetDbResponse\"\x00\x12\x39\n\x08InsertDb\x12\x14.api.InsertDbRequest\x1a\x15.api.InsertDbResponse\"\x00\x12\x39\n\x08\x44\x65leteDb\x12\x14.api.DeleteDbRequest\x1a\x15.api.DeleteDbResponse\"\x00\x12\x39\n\x08UpdateDb\x12\x14.api.UpdateDbRequest\x1a\x15.api.UpdateDbResponse\"\x00\x42\x0cZ\n./api/grpcb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'database_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\n./api/grpc'
  _GETDBREQUEST._serialized_start=23
  _GETDBREQUEST._serialized_end=105
  _GETDBRESPONSE._serialized_start=107
  _GETDBRESPONSE._serialized_end=152
  _INSERTDBREQUEST._serialized_start=154
  _INSERTDBREQUEST._serialized_end=236
  _INSERTDBRESPONSE._serialized_start=238
  _INSERTDBRESPONSE._serialized_end=272
  _DELETEDBREQUEST._serialized_start=274
  _DELETEDBREQUEST._serialized_end=342
  _DELETEDBRESPONSE._serialized_start=344
  _DELETEDBRESPONSE._serialized_end=378
  _UPDATEDBREQUEST._serialized_start=380
  _UPDATEDBREQUEST._serialized_end=464
  _UPDATEDBRESPONSE._serialized_start=466
  _UPDATEDBRESPONSE._serialized_end=500
  _DATABASE._serialized_start=503
  _DATABASE._serialized_end=740
# @@protoc_insertion_point(module_scope)
