from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateCompanyRequest(_message.Message):
    __slots__ = ("legal_entity_registration", "company_id", "company_name", "trade_name")
    LEGAL_ENTITY_REGISTRATION_FIELD_NUMBER: _ClassVar[int]
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    TRADE_NAME_FIELD_NUMBER: _ClassVar[int]
    legal_entity_registration: str
    company_id: str
    company_name: str
    trade_name: str
    def __init__(self, legal_entity_registration: _Optional[str] = ..., company_id: _Optional[str] = ..., company_name: _Optional[str] = ..., trade_name: _Optional[str] = ...) -> None: ...

class CreateCompanyResponse(_message.Message):
    __slots__ = ("status", "description", "command_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    status: str
    description: str
    command_id: str
    def __init__(self, status: _Optional[str] = ..., description: _Optional[str] = ..., command_id: _Optional[str] = ...) -> None: ...

class DeactivateCompanyRequest(_message.Message):
    __slots__ = ("company_id", "reason")
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    company_id: str
    reason: str
    def __init__(self, company_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class DeactivateCompanyResponse(_message.Message):
    __slots__ = ("status", "description", "command_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    status: str
    description: str
    command_id: str
    def __init__(self, status: _Optional[str] = ..., description: _Optional[str] = ..., command_id: _Optional[str] = ...) -> None: ...

class ReactivateCompanyRequest(_message.Message):
    __slots__ = ("company_id", "reason")
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    company_id: str
    reason: str
    def __init__(self, company_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class ReactivateCompanyResponse(_message.Message):
    __slots__ = ("status", "description", "command_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    status: str
    description: str
    command_id: str
    def __init__(self, status: _Optional[str] = ..., description: _Optional[str] = ..., command_id: _Optional[str] = ...) -> None: ...
