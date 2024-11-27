from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateCompanyRequest(_message.Message):
    __slots__ = ("legal_entity_registration", "company_id", "company_name")
    LEGAL_ENTITY_REGISTRATION_FIELD_NUMBER: _ClassVar[int]
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    legal_entity_registration: str
    company_id: str
    company_name: str
    def __init__(self, legal_entity_registration: _Optional[str] = ..., company_id: _Optional[str] = ..., company_name: _Optional[str] = ...) -> None: ...

class DeactivateCompanyRequest(_message.Message):
    __slots__ = ("company_id", "reason_code", "reason_text")
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    REASON_TEXT_FIELD_NUMBER: _ClassVar[int]
    company_id: str
    reason_code: str
    reason_text: str
    def __init__(self, company_id: _Optional[str] = ..., reason_code: _Optional[str] = ..., reason_text: _Optional[str] = ...) -> None: ...

class ReactivateCompanyRequest(_message.Message):
    __slots__ = ("company_id", "reason_code", "reason_text")
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    REASON_TEXT_FIELD_NUMBER: _ClassVar[int]
    company_id: str
    reason_code: str
    reason_text: str
    def __init__(self, company_id: _Optional[str] = ..., reason_code: _Optional[str] = ..., reason_text: _Optional[str] = ...) -> None: ...

class CompanyCommandResponse(_message.Message):
    __slots__ = ("command_id",)
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    command_id: str
    def __init__(self, command_id: _Optional[str] = ...) -> None: ...
