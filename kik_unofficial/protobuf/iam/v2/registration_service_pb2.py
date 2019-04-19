# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: iam/v2/registration_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import kik_unofficial.protobuf.protobuf_validation_pb2 as protobuf__validation__pb2
from kik_unofficial.protobuf.client.v2 import client_meta_pb2 as client_dot_v2_dot_client__meta__pb2
from kik_unofficial.protobuf.common.v2 import model_pb2 as common_dot_v2_dot_model__pb2
from kik_unofficial.protobuf.google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from kik_unofficial.protobuf.session.v2 import model_pb2 as session_dot_v2_dot_model__pb2
import kik_unofficial.protobuf.common_model_pb2 as common__model__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='iam/v2/registration_service.proto',
  package='mobile.iam.v2',
  syntax='proto3',
  serialized_pb=_b('\n!iam/v2/registration_service.proto\x12\rmobile.iam.v2\x1a\x19protobuf_validation.proto\x1a\x1b\x63lient/v2/client_meta.proto\x1a\x15\x63ommon/v2/model.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x16session/v2/model.proto\x1a\x12\x63ommon_model.proto\"t\n\x1aValidateForRegisterRequest\x12\'\n\x05\x65mail\x18\x01 \x01(\x0b\x32\x10.common.v2.EmailB\x06\xca\x9d%\x02\x08\x00\x12-\n\x08username\x18\x02 \x01(\x0b\x32\x13.common.v2.UsernameB\x06\xca\x9d%\x02\x08\x00\"\x91\x02\n\x1bValidateForRegisterResponse\x12\x41\n\x06result\x18\x01 \x01(\x0e\x32\x31.mobile.iam.v2.ValidateForRegisterResponse.Result\x12S\n\x10invalid_elements\x18\x02 \x03(\x0e\x32\x39.mobile.iam.v2.ValidateForRegisterResponse.InvalidElement\"/\n\x06Result\x12\x06\n\x02OK\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\x12\x11\n\rMISSING_INPUT\x10\x02\")\n\x0eInvalidElement\x12\t\n\x05\x45MAIL\x10\x00\x12\x0c\n\x08USERNAME\x10\x01\"\xd6\x03\n\x0fRegisterRequest\x12\x1d\n\nfirst_name\x18\x01 \x01(\tB\t\xca\x9d%\x05\x08\x01 \xff\x01\x12\x1c\n\tlast_name\x18\x02 \x01(\tB\t\xca\x9d%\x05\x08\x01 \xff\x01\x12-\n\x08username\x18\x03 \x01(\x0b\x32\x13.common.v2.UsernameB\x06\xca\x9d%\x02\x08\x01\x12\'\n\x05\x65mail\x18\x04 \x01(\x0b\x32\x10.common.v2.EmailB\x06\xca\x9d%\x02\x08\x01\x12?\n\x0e\x64\x65vice_details\x18\x05 \x01(\x0b\x32\x1f.common.client.v2.DeviceDetailsB\x06\xca\x9d%\x02\x08\x01\x12\x36\n\x06locale\x18\x06 \x01(\x0b\x32\x1e.common.client.v2.ClientLocaleB\x06\xca\x9d%\x02\x08\x01\x12\x38\n\x07version\x18\x07 \x01(\x0b\x32\x1f.common.client.v2.ClientVersionB\x06\xca\x9d%\x02\x08\x01\x12\x34\n\x08\x62irthday\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x06\xca\x9d%\x02\x08\x01\x12#\n\x10username_passkey\x18\t \x01(\x0c\x42\t\xca\x9d%\x05\x08\x01\x30\x80\x08\x12 \n\remail_passkey\x18\n \x01(\x0c\x42\t\xca\x9d%\x05\x08\x01\x30\x80\x08\"\xcd\x04\n\x10RegisterResponse\x12\x36\n\x06result\x18\x01 \x01(\x0e\x32&.mobile.iam.v2.RegisterResponse.Result\x12H\n\x10invalid_elements\x18\x02 \x03(\x0e\x32..mobile.iam.v2.RegisterResponse.RequestElement\x12Q\n\x19policy_violation_elements\x18\x03 \x03(\x0e\x32..mobile.iam.v2.RegisterResponse.RequestElement\"\x9f\x01\n\x06Result\x12\x06\n\x02OK\x10\x00\x12\x19\n\x15VERIFICATION_REQUIRED\x10\x01\x12\x1d\n\x19\x45RROR_VERIFICATION_FAILED\x10\x02\x12\x18\n\x14\x45RROR_NOT_ACCEPTABLE\x10\x03\x12\x1b\n\x17\x45RROR_VALIDATION_FAILED\x10\x04\x12\x1c\n\x18\x45RROR_ALREADY_REGISTERED\x10\x05\"\xc1\x01\n\x0eRequestElement\x12\t\n\x05OTHER\x10\x00\x12\x0e\n\nFIRST_NAME\x10\x01\x12\r\n\tLAST_NAME\x10\x02\x12\r\n\tFULL_NAME\x10\x03\x12\x0c\n\x08USERNAME\x10\x04\x12\t\n\x05\x45MAIL\x10\x05\x12\r\n\tDEVICE_ID\x10\x06\x12\n\n\x06LOCALE\x10\x07\x12\x0b\n\x07VERSION\x10\x08\x12\x0c\n\x08\x42IRTHDAY\x10\t\x12\x14\n\x10USERNAME_PASSKEY\x10\n\x12\x11\n\rEMAIL_PASSKEY\x10\x0b\x32\xcd\x01\n\x0cRegistration\x12n\n\x13ValidateForRegister\x12).mobile.iam.v2.ValidateForRegisterRequest\x1a*.mobile.iam.v2.ValidateForRegisterResponse\"\x00\x12M\n\x08Register\x12\x1e.mobile.iam.v2.RegisterRequest\x1a\x1f.mobile.iam.v2.RegisterResponse\"\x00\x42k\n\x12\x63om.kik.gen.iam.v2ZDgithub.com/kikinteractive/xiphias-api-mobile/generated/go/iam/v2;iam\xa2\x02\x0eKPBMobileIAMV2b\x06proto3')
  ,
  dependencies=[protobuf__validation__pb2.DESCRIPTOR,client_dot_v2_dot_client__meta__pb2.DESCRIPTOR,common_dot_v2_dot_model__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,session_dot_v2_dot_model__pb2.DESCRIPTOR,common__model__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_VALIDATEFORREGISTERRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mobile.iam.v2.ValidateForRegisterResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_INPUT', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=510,
  serialized_end=557,
)
_sym_db.RegisterEnumDescriptor(_VALIDATEFORREGISTERRESPONSE_RESULT)

_VALIDATEFORREGISTERRESPONSE_INVALIDELEMENT = _descriptor.EnumDescriptor(
  name='InvalidElement',
  full_name='mobile.iam.v2.ValidateForRegisterResponse.InvalidElement',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EMAIL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USERNAME', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=559,
  serialized_end=600,
)
_sym_db.RegisterEnumDescriptor(_VALIDATEFORREGISTERRESPONSE_INVALIDELEMENT)

_REGISTERRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mobile.iam.v2.RegisterResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERIFICATION_REQUIRED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_VERIFICATION_FAILED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NOT_ACCEPTABLE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_VALIDATION_FAILED', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_ALREADY_REGISTERED', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1310,
  serialized_end=1469,
)
_sym_db.RegisterEnumDescriptor(_REGISTERRESPONSE_RESULT)

_REGISTERRESPONSE_REQUESTELEMENT = _descriptor.EnumDescriptor(
  name='RequestElement',
  full_name='mobile.iam.v2.RegisterResponse.RequestElement',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIRST_NAME', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LAST_NAME', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FULL_NAME', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USERNAME', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMAIL', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_ID', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCALE', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERSION', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BIRTHDAY', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USERNAME_PASSKEY', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMAIL_PASSKEY', index=11, number=11,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1472,
  serialized_end=1665,
)
_sym_db.RegisterEnumDescriptor(_REGISTERRESPONSE_REQUESTELEMENT)


_VALIDATEFORREGISTERREQUEST = _descriptor.Descriptor(
  name='ValidateForRegisterRequest',
  full_name='mobile.iam.v2.ValidateForRegisterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='mobile.iam.v2.ValidateForRegisterRequest.email', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\000'))),
    _descriptor.FieldDescriptor(
      name='username', full_name='mobile.iam.v2.ValidateForRegisterRequest.username', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\000'))),
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
  serialized_start=208,
  serialized_end=324,
)


_VALIDATEFORREGISTERRESPONSE = _descriptor.Descriptor(
  name='ValidateForRegisterResponse',
  full_name='mobile.iam.v2.ValidateForRegisterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mobile.iam.v2.ValidateForRegisterResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='invalid_elements', full_name='mobile.iam.v2.ValidateForRegisterResponse.invalid_elements', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VALIDATEFORREGISTERRESPONSE_RESULT,
    _VALIDATEFORREGISTERRESPONSE_INVALIDELEMENT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=327,
  serialized_end=600,
)


_REGISTERREQUEST = _descriptor.Descriptor(
  name='RegisterRequest',
  full_name='mobile.iam.v2.RegisterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_name', full_name='mobile.iam.v2.RegisterRequest.first_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\005\010\001 \377\001'))),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='mobile.iam.v2.RegisterRequest.last_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\005\010\001 \377\001'))),
    _descriptor.FieldDescriptor(
      name='username', full_name='mobile.iam.v2.RegisterRequest.username', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='email', full_name='mobile.iam.v2.RegisterRequest.email', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='device_details', full_name='mobile.iam.v2.RegisterRequest.device_details', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='locale', full_name='mobile.iam.v2.RegisterRequest.locale', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='version', full_name='mobile.iam.v2.RegisterRequest.version', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='birthday', full_name='mobile.iam.v2.RegisterRequest.birthday', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='username_passkey', full_name='mobile.iam.v2.RegisterRequest.username_passkey', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\005\010\0010\200\010'))),
    _descriptor.FieldDescriptor(
      name='email_passkey', full_name='mobile.iam.v2.RegisterRequest.email_passkey', index=9,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\005\010\0010\200\010'))),
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
  serialized_start=603,
  serialized_end=1073,
)


_REGISTERRESPONSE = _descriptor.Descriptor(
  name='RegisterResponse',
  full_name='mobile.iam.v2.RegisterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mobile.iam.v2.RegisterResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='invalid_elements', full_name='mobile.iam.v2.RegisterResponse.invalid_elements', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='policy_violation_elements', full_name='mobile.iam.v2.RegisterResponse.policy_violation_elements', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REGISTERRESPONSE_RESULT,
    _REGISTERRESPONSE_REQUESTELEMENT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1076,
  serialized_end=1665,
)

_VALIDATEFORREGISTERREQUEST.fields_by_name['email'].message_type = common_dot_v2_dot_model__pb2._EMAIL
_VALIDATEFORREGISTERREQUEST.fields_by_name['username'].message_type = common_dot_v2_dot_model__pb2._USERNAME
_VALIDATEFORREGISTERRESPONSE.fields_by_name['result'].enum_type = _VALIDATEFORREGISTERRESPONSE_RESULT
_VALIDATEFORREGISTERRESPONSE.fields_by_name['invalid_elements'].enum_type = _VALIDATEFORREGISTERRESPONSE_INVALIDELEMENT
_VALIDATEFORREGISTERRESPONSE_RESULT.containing_type = _VALIDATEFORREGISTERRESPONSE
_VALIDATEFORREGISTERRESPONSE_INVALIDELEMENT.containing_type = _VALIDATEFORREGISTERRESPONSE
_REGISTERREQUEST.fields_by_name['username'].message_type = common_dot_v2_dot_model__pb2._USERNAME
_REGISTERREQUEST.fields_by_name['email'].message_type = common_dot_v2_dot_model__pb2._EMAIL
_REGISTERREQUEST.fields_by_name['device_details'].message_type = client_dot_v2_dot_client__meta__pb2._DEVICEDETAILS
_REGISTERREQUEST.fields_by_name['locale'].message_type = client_dot_v2_dot_client__meta__pb2._CLIENTLOCALE
_REGISTERREQUEST.fields_by_name['version'].message_type = client_dot_v2_dot_client__meta__pb2._CLIENTVERSION
_REGISTERREQUEST.fields_by_name['birthday'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_REGISTERRESPONSE.fields_by_name['result'].enum_type = _REGISTERRESPONSE_RESULT
_REGISTERRESPONSE.fields_by_name['invalid_elements'].enum_type = _REGISTERRESPONSE_REQUESTELEMENT
_REGISTERRESPONSE.fields_by_name['policy_violation_elements'].enum_type = _REGISTERRESPONSE_REQUESTELEMENT
_REGISTERRESPONSE_RESULT.containing_type = _REGISTERRESPONSE
_REGISTERRESPONSE_REQUESTELEMENT.containing_type = _REGISTERRESPONSE
DESCRIPTOR.message_types_by_name['ValidateForRegisterRequest'] = _VALIDATEFORREGISTERREQUEST
DESCRIPTOR.message_types_by_name['ValidateForRegisterResponse'] = _VALIDATEFORREGISTERRESPONSE
DESCRIPTOR.message_types_by_name['RegisterRequest'] = _REGISTERREQUEST
DESCRIPTOR.message_types_by_name['RegisterResponse'] = _REGISTERRESPONSE

ValidateForRegisterRequest = _reflection.GeneratedProtocolMessageType('ValidateForRegisterRequest', (_message.Message,), dict(
  DESCRIPTOR = _VALIDATEFORREGISTERREQUEST,
  __module__ = 'iam.v2.registration_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.iam.v2.ValidateForRegisterRequest)
  ))
_sym_db.RegisterMessage(ValidateForRegisterRequest)

ValidateForRegisterResponse = _reflection.GeneratedProtocolMessageType('ValidateForRegisterResponse', (_message.Message,), dict(
  DESCRIPTOR = _VALIDATEFORREGISTERRESPONSE,
  __module__ = 'iam.v2.registration_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.iam.v2.ValidateForRegisterResponse)
  ))
_sym_db.RegisterMessage(ValidateForRegisterResponse)

RegisterRequest = _reflection.GeneratedProtocolMessageType('RegisterRequest', (_message.Message,), dict(
  DESCRIPTOR = _REGISTERREQUEST,
  __module__ = 'iam.v2.registration_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.iam.v2.RegisterRequest)
  ))
_sym_db.RegisterMessage(RegisterRequest)

RegisterResponse = _reflection.GeneratedProtocolMessageType('RegisterResponse', (_message.Message,), dict(
  DESCRIPTOR = _REGISTERRESPONSE,
  __module__ = 'iam.v2.registration_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.iam.v2.RegisterResponse)
  ))
_sym_db.RegisterMessage(RegisterResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\022com.kik.gen.iam.v2ZDgithub.com/kikinteractive/xiphias-api-mobile/generated/go/iam/v2;iam\242\002\016KPBMobileIAMV2'))
_VALIDATEFORREGISTERREQUEST.fields_by_name['email'].has_options = True
_VALIDATEFORREGISTERREQUEST.fields_by_name['email']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\000'))
_VALIDATEFORREGISTERREQUEST.fields_by_name['username'].has_options = True
_VALIDATEFORREGISTERREQUEST.fields_by_name['username']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\000'))
_REGISTERREQUEST.fields_by_name['first_name'].has_options = True
_REGISTERREQUEST.fields_by_name['first_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\005\010\001 \377\001'))
_REGISTERREQUEST.fields_by_name['last_name'].has_options = True
_REGISTERREQUEST.fields_by_name['last_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\005\010\001 \377\001'))
_REGISTERREQUEST.fields_by_name['username'].has_options = True
_REGISTERREQUEST.fields_by_name['username']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
_REGISTERREQUEST.fields_by_name['email'].has_options = True
_REGISTERREQUEST.fields_by_name['email']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
_REGISTERREQUEST.fields_by_name['device_details'].has_options = True
_REGISTERREQUEST.fields_by_name['device_details']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
_REGISTERREQUEST.fields_by_name['locale'].has_options = True
_REGISTERREQUEST.fields_by_name['locale']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
_REGISTERREQUEST.fields_by_name['version'].has_options = True
_REGISTERREQUEST.fields_by_name['version']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
_REGISTERREQUEST.fields_by_name['birthday'].has_options = True
_REGISTERREQUEST.fields_by_name['birthday']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
_REGISTERREQUEST.fields_by_name['username_passkey'].has_options = True
_REGISTERREQUEST.fields_by_name['username_passkey']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\005\010\0010\200\010'))
_REGISTERREQUEST.fields_by_name['email_passkey'].has_options = True
_REGISTERREQUEST.fields_by_name['email_passkey']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\005\010\0010\200\010'))
# @@protoc_insertion_point(module_scope)