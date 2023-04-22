from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteDbRequest(_message.Message):
    __slots__ = ["condition", "db_host", "table"]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    DB_HOST_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    condition: str
    db_host: str
    table: str
    def __init__(self, table: _Optional[str] = ..., condition: _Optional[str] = ..., db_host: _Optional[str] = ...) -> None: ...

class DeleteDbResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class GetDbRequest(_message.Message):
    __slots__ = ["columns", "condition", "db_host", "table"]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    DB_HOST_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    columns: str
    condition: str
    db_host: str
    table: str
    def __init__(self, columns: _Optional[str] = ..., table: _Optional[str] = ..., condition: _Optional[str] = ..., db_host: _Optional[str] = ...) -> None: ...

class GetDbResponse(_message.Message):
    __slots__ = ["data", "status"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    status: str
    def __init__(self, status: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class InsertDbRequest(_message.Message):
    __slots__ = ["columns", "db_host", "table", "values"]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    DB_HOST_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    columns: str
    db_host: str
    table: str
    values: str
    def __init__(self, table: _Optional[str] = ..., columns: _Optional[str] = ..., values: _Optional[str] = ..., db_host: _Optional[str] = ...) -> None: ...

class InsertDbResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class UpdateDbRequest(_message.Message):
    __slots__ = ["condition", "db_host", "table", "to_set"]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    DB_HOST_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    TO_SET_FIELD_NUMBER: _ClassVar[int]
    condition: str
    db_host: str
    table: str
    to_set: str
    def __init__(self, table: _Optional[str] = ..., to_set: _Optional[str] = ..., condition: _Optional[str] = ..., db_host: _Optional[str] = ...) -> None: ...

class UpdateDbResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...
