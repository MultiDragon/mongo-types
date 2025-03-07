from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    Callable,
    Container,
    Dict,
    Generic,
    Iterable,
    Iterator,
    List,
    Optional,
    Pattern,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)
from uuid import UUID

from bson import ObjectId
from mongoengine.base import BaseField, ComplexBaseField
from mongoengine.document import Document
from typing_extensions import Literal

_T = TypeVar("_T")

_ST = TypeVar("_ST")
_GT = TypeVar("_GT")

class ObjectIdField(Generic[_ST, _GT], BaseField):
    # ObjectIdField()
    @overload
    def __new__(
        cls,
        *,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: None = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[ObjectId]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> ObjectIdField[Optional[ObjectId], Optional[ObjectId]]: ...
    # ObjectIdField(default=ObjectId)
    @overload
    def __new__(
        cls,
        *,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: Union[ObjectId, Callable[[], ObjectId]],
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[ObjectId]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> ObjectIdField[Optional[ObjectId], ObjectId]: ...
    # ObjectIdField(required=True)
    @overload
    def __new__(
        cls,
        *,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True],
        default: None = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[ObjectId]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> ObjectIdField[ObjectId, ObjectId]: ...
    # ObjectIdField(required=True, default=ObjectId)
    @overload
    def __new__(
        cls,
        *,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True],
        default: Union[ObjectId, Callable[[], ObjectId]],
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[ObjectId]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> ObjectIdField[Optional[ObjectId], ObjectId]: ...
    # ObjectIdField(primiary_key=True)
    @overload
    def __new__(
        cls,
        *,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: bool = ...,
        default: Union[ObjectId, None, Callable[[], ObjectId]] = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[True],
        choices: Optional[Iterable[ObjectId]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> ObjectIdField[ObjectId, ObjectId]: ...
    def __set__(self, instance: Any, value: _ST) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> _GT: ...

class StringField(Generic[_ST, _GT], BaseField):
    # StringField()
    @overload
    def __new__(
        cls,
        *,
        regex: Optional[str] = ...,
        max_length: Optional[int] = ...,
        min_length: Optional[int] = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: None = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[str]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> StringField[Optional[str], Optional[str]]: ...
    # StringField(default="foo")
    @overload
    def __new__(
        cls,
        *,
        regex: Optional[str] = ...,
        max_length: Optional[int] = ...,
        min_length: Optional[int] = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: Union[str, Callable[[], str]],
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[str]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> StringField[Optional[str], str]: ...
    # StringField(required=True)
    @overload
    def __new__(
        cls,
        *,
        regex: Optional[str] = ...,
        max_length: Optional[int] = ...,
        min_length: Optional[int] = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True],
        default: None = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[str]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> StringField[str, str]: ...
    # StringField(required=True, default="foo")
    @overload
    def __new__(
        cls,
        *,
        regex: Optional[str] = ...,
        max_length: Optional[int] = ...,
        min_length: Optional[int] = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True],
        default: Union[str, Callable[[], str]],
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[str]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> StringField[Optional[str], str]: ...
    # StringField(primary_key=True)
    @overload
    def __new__(
        cls,
        *,
        regex: Optional[str] = ...,
        max_length: Optional[int] = ...,
        min_length: Optional[int] = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: bool = ...,
        default: Union[str, Callable[[], str], None] = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[True],
        choices: Optional[Iterable[str]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> StringField[str, str]: ...
    def __set__(self, instance: Any, value: _ST) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> _GT: ...

class EmailField(StringField[_ST, _GT]):
    @overload
    def __new__(
        cls,
        *,
        domain_whitelist: Optional[List[str]] = ...,
        allow_utf8_user: bool = ...,
        allow_ip_domain: bool = ...,
        regex: Optional[str] = ...,
        max_length: Optional[int] = ...,
        min_length: Optional[int] = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: None = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[str]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> EmailField[Optional[str], Optional[str]]: ...
    @overload
    def __new__(
        cls,
        *,
        domain_whitelist: Optional[List[str]] = ...,
        allow_utf8_user: bool = ...,
        allow_ip_domain: bool = ...,
        regex: Optional[str] = ...,
        max_length: Optional[int] = ...,
        min_length: Optional[int] = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: Union[str, Callable[[], str]],
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[str]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> EmailField[Optional[str], str]: ...
    @overload
    def __new__(
        cls,
        *,
        domain_whitelist: Optional[List[str]] = ...,
        allow_utf8_user: bool = ...,
        allow_ip_domain: bool = ...,
        regex: Optional[str] = ...,
        max_length: Optional[int] = ...,
        min_length: Optional[int] = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True],
        default: None = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[str]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> EmailField[str, str]: ...
    @overload
    def __new__(
        cls,
        *,
        domain_whitelist: Optional[List[str]] = ...,
        allow_utf8_user: bool = ...,
        allow_ip_domain: bool = ...,
        regex: Optional[str] = ...,
        max_length: Optional[int] = ...,
        min_length: Optional[int] = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True],
        default: Union[str, Callable[[], str]],
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[str]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> EmailField[Optional[str], str]: ...
    @overload
    def __new__(
        cls,
        *,
        domain_whitelist: Optional[List[str]] = ...,
        allow_utf8_user: bool = ...,
        allow_ip_domain: bool = ...,
        regex: Optional[str] = ...,
        max_length: Optional[int] = ...,
        min_length: Optional[int] = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: bool = ...,
        default: Union[str, Callable[[], str], None] = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[True],
        choices: Optional[Iterable[str]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> EmailField[str, str]: ...
    def __set__(self, instance: Any, value: _ST) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> _GT: ...

class IntField(Generic[_ST, _GT], BaseField):
    @overload
    def __new__(
        cls,
        *,
        min_value: int = ...,
        max_value: int = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: None = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[int]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> IntField[Optional[int], Optional[int]]: ...
    @overload
    def __new__(
        cls,
        *,
        min_value: int = ...,
        max_value: int = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: Union[int, Callable[[], int]],
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[int]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> IntField[Optional[int], int]: ...
    @overload
    def __new__(
        cls,
        *,
        min_value: int = ...,
        max_value: int = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True],
        default: None = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[int]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> IntField[int, int]: ...
    @overload
    def __new__(
        cls,
        *,
        min_value: int = ...,
        max_value: int = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True],
        default: Union[int, Callable[[], int]],
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[int]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> IntField[Optional[int], int]: ...
    @overload
    def __new__(
        cls,
        *,
        min_value: int = ...,
        max_value: int = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: bool = ...,
        default: Union[int, Callable[[], int], None] = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[True],
        choices: Optional[Iterable[int]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> IntField[int, int]: ...
    def __set__(self, instance: Any, value: _ST) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> _GT: ...

class FloatField(Generic[_ST, _GT], BaseField):
    @overload
    def __new__(
        cls,
        *,
        min_value: float = ...,
        max_value: float = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: None = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[float]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> FloatField[Optional[float], Optional[float]]: ...
    @overload
    def __new__(
        cls,
        *,
        min_value: float = ...,
        max_value: float = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: Union[float, Callable[[], float]],
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[float]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> FloatField[Optional[float], float]: ...
    @overload
    def __new__(
        cls,
        *,
        min_value: float = ...,
        max_value: float = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True],
        default: None = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[float]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> FloatField[float, float]: ...
    @overload
    def __new__(
        cls,
        *,
        min_value: float = ...,
        max_value: float = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True],
        default: Union[float, Callable[[], float]],
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[float]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> FloatField[Optional[float], float]: ...
    @overload
    def __new__(
        cls,
        *,
        min_value: float = ...,
        max_value: float = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: bool = ...,
        default: Union[float, Callable[[], float], None] = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[True],
        choices: Optional[Iterable[float]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> FloatField[float, float]: ...
    def __set__(self, instance: Any, value: _ST) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> _GT: ...

class DecimalField(Generic[_ST, _GT], BaseField):
    @overload
    def __new__(
        cls,
        *,
        min_value: Decimal = ...,
        max_value: Decimal = ...,
        force_string: bool = ...,
        precision: int = ...,
        rounding: str = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: None = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[Decimal]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> DecimalField[Optional[Decimal], Optional[Decimal]]: ...
    @overload
    def __new__(
        cls,
        *,
        min_value: Decimal = ...,
        max_value: Decimal = ...,
        force_string: bool = ...,
        precision: int = ...,
        rounding: str = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: Union[Decimal, Callable[[], Decimal]],
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[Decimal]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> DecimalField[Optional[Decimal], Decimal]: ...
    @overload
    def __new__(
        cls,
        *,
        min_value: Decimal = ...,
        max_value: Decimal = ...,
        force_string: bool = ...,
        precision: int = ...,
        rounding: str = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True],
        default: None = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[Decimal]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> DecimalField[Decimal, Decimal]: ...
    @overload
    def __new__(
        cls,
        *,
        min_value: Decimal = ...,
        max_value: Decimal = ...,
        force_string: bool = ...,
        precision: int = ...,
        rounding: str = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True],
        default: Union[Decimal, Callable[[], Decimal]],
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[Decimal]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> DecimalField[Optional[Decimal], Decimal]: ...
    @overload
    def __new__(
        cls,
        *,
        min_value: Decimal = ...,
        max_value: Decimal = ...,
        force_string: bool = ...,
        precision: int = ...,
        rounding: str = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: bool = ...,
        default: Union[Decimal, Callable[[], Decimal], None] = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[True],
        choices: Optional[Iterable[Decimal]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> DecimalField[Decimal, Decimal]: ...
    def __set__(self, instance: Any, value: _ST) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> _GT: ...

class BooleanField(Generic[_ST, _GT], BaseField):
    @overload
    def __new__(
        cls,
        *,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: None = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[bool]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> BooleanField[Optional[bool], Optional[bool]]: ...
    @overload
    def __new__(
        cls,
        *,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: Union[bool, Callable[[], bool]],
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[bool]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> BooleanField[Optional[bool], bool]: ...
    @overload
    def __new__(
        cls,
        *,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True],
        default: None = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[bool]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> BooleanField[bool, bool]: ...
    @overload
    def __new__(
        cls,
        *,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True],
        default: Union[bool, Callable[[], bool]],
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[bool]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> BooleanField[Optional[bool], bool]: ...
    @overload
    def __new__(
        cls,
        *,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: bool = ...,
        default: Union[bool, None, Callable[[], bool]] = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[True],
        choices: Optional[Iterable[bool]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> BooleanField[bool, bool]: ...
    def __set__(self, instance: Any, value: _ST) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> _GT: ...

class DateTimeField(Generic[_ST, _GT], BaseField):
    @overload
    def __new__(
        cls,
        *,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: None = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[datetime]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> DateTimeField[Optional[datetime], Optional[datetime]]: ...
    @overload
    def __new__(
        cls,
        *,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: Union[datetime, Callable[[], datetime]],
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[datetime]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> DateTimeField[Optional[datetime], datetime]: ...
    @overload
    def __new__(
        cls,
        *,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True],
        default: None = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[datetime]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> DateTimeField[datetime, datetime]: ...
    @overload
    def __new__(
        cls,
        *,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True],
        default: Union[datetime, Callable[[], datetime]],
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[datetime]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> DateTimeField[Optional[datetime], datetime]: ...
    @overload
    def __new__(
        cls,
        *,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: bool = ...,
        default: Union[datetime, None, Callable[[], datetime]] = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[True],
        choices: Optional[Iterable[datetime]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> DateTimeField[datetime, datetime]: ...
    def __set__(self, instance: Any, value: _ST) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> _GT: ...

class EmbeddedDocumentField(Generic[_ST, _GT], BaseField):
    @overload
    def __new__(
        cls,
        document_type: Type[_T],
        required: Literal[False] = ...,
        help_text: str = ...,
    ) -> EmbeddedDocumentField[Optional[_T], Optional[_T]]: ...
    @overload
    def __new__(
        cls,
        document_type: Type[_T],
        required: Literal[False] = ...,
        *,
        default: Union[_T, Callable[[], _T]],
        help_text: str = ...,
    ) -> EmbeddedDocumentField[Optional[_T], _T]: ...
    @overload
    def __new__(
        cls,
        document_type: Type[_T],
        *,
        required: Literal[True],
        help_text: str = ...,
    ) -> EmbeddedDocumentField[_T, _T]: ...
    @overload
    def __new__(
        cls,
        document_type: Type[_T],
        *,
        required: Literal[True],
        default: Union[_T, Callable[[], _T]],
        help_text: str = ...,
    ) -> EmbeddedDocumentField[Optional[_T], _T]: ...
    def __set__(
        self: EmbeddedDocumentField[_ST, Any], instance: Any, value: _ST
    ) -> None: ...
    def __get__(
        self: EmbeddedDocumentField[Any, _GT], instance: Any, owner: Any
    ) -> _GT: ...

class DynamicField(BaseField): ...

class ListField(Generic[_T], ComplexBaseField):
    # see: https://github.com/python/mypy/issues/4236#issuecomment-521628880
    @overload
    def __new__(
        cls,
        field: StringField[Any, Any] = ...,
        required: bool = ...,
        default: Optional[Union[List[Any], Callable[[], List[Any]]]] = ...,
        verbose_name: str = ...,
        help_text: str = ...,
        null: bool = ...,
    ) -> ListField[StringField[Any, Any]]: ...
    @overload
    def __new__(
        cls,
        field: DictField[Any],
        required: bool = ...,
        default: Optional[Union[List[Any], Callable[[], List[Any]]]] = ...,
        verbose_name: str = ...,
        help_text: str = ...,
        null: bool = ...,
    ) -> ListField[DictField[Any]]: ...
    @overload
    def __new__(
        cls,
        field: Any,
        required: bool = ...,
        default: Optional[Union[List[Any], Callable[[], List[Any]]]] = ...,
        verbose_name: str = ...,
        help_text: str = ...,
        null: bool = ...,
    ) -> ListField[Any]: ...
    def __getitem__(self, arg: Any) -> _T: ...
    def __iter__(self) -> Iterator[_T]: ...
    @overload
    def __set__(
        self: ListField[StringField[Any, Any]],
        instance: Any,
        value: Optional[List[str]],
    ) -> None: ...
    @overload
    def __set__(
        self: ListField[DictField[Any]], instance: Any, value: List[Dict[str, Any]]
    ) -> None: ...
    @overload
    def __set__(self: ListField[_T], instance: Any, value: List[_T]) -> None: ...
    @overload
    def __get__(
        self: ListField[DynamicField], instance: Any, owner: Any
    ) -> List[Any]: ...
    @overload
    def __get__(
        self: ListField[StringField[Any, Any]], instance: Any, owner: Any
    ) -> List[str]: ...
    @overload
    def __get__(
        self: ListField[DictField[Any]], instance: Any, owner: Any
    ) -> List[Dict[str, Any]]: ...

class DictField(Generic[_T], ComplexBaseField):
    # not sure we need the init method overloads
    @overload
    def __new__(  # type: ignore
        cls,
        field: _T = ...,
        required: bool = ...,
        name: Optional[str] = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: bool = ...,
        help_text: Optional[str] = ...,
        default: Union[Dict[str, str], None, Callable[[], Dict[str, str]]] = ...,
        choices: Optional[Iterable[Dict[str, str]]] = ...,
        verbose_name: Optional[str] = ...,
        db_field: str = ...,
    ) -> DictField[StringField[Any, Any]]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        field: _T = ...,
        required: bool = ...,
        name: Optional[str] = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: bool = ...,
        help_text: Optional[str] = ...,
        default: Union[
            Dict[str, List[str]], None, Callable[[], Dict[str, List[str]]]
        ] = ...,
        choices: Optional[Iterable[Dict[str, List[str]]]] = ...,
        verbose_name: Optional[str] = ...,
        db_field: str = ...,
    ) -> DictField[ListField[StringField[Any, Any]]]: ...
    @overload
    def __new__(
        cls,
        field: _T = ...,
        required: bool = ...,
        name: Optional[str] = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: bool = ...,
        help_text: Optional[str] = ...,
        default: Union[Dict[str, Any], None, Callable[[], Dict[str, Any]]] = ...,
        choices: Optional[Iterable[Dict[str, Any]]] = ...,
        verbose_name: Optional[str] = ...,
        db_field: str = ...,
    ) -> DictField[_T]: ...
    # TODO(sbdchd): use overloads to ensure we can only use nulls when
    # null=True is passed in
    @overload
    def __set__(
        self: DictField[StringField[Any, Any]],
        instance: object,
        value: Optional[Dict[str, str]],
    ) -> None: ...
    @overload
    def __set__(
        self: DictField[ListField[StringField[Any, Any]]],
        instance: object,
        value: Optional[Dict[str, List[str]]],
    ) -> None: ...
    @overload
    def __set__(
        self: DictField[_T], instance: object, value: Optional[Dict[str, _T]]
    ) -> None: ...
    @overload
    def __set__(
        self: DictField[Any], instance: object, value: Optional[Dict[str, Any]]
    ) -> None: ...
    @overload
    def __get__(
        self: DictField[DynamicField], instance: object, owner: object
    ) -> Dict[str, Any]: ...
    @overload
    def __get__(
        self: DictField[StringField[Any, Any]], instance: object, owner: object
    ) -> Dict[str, str]: ...
    @overload
    def __get__(
        self: DictField[ListField[StringField[Any, Any]]],
        instance: object,
        owner: object,
    ) -> Dict[str, List[str]]: ...
    def __getitem__(self, arg: Any) -> _T: ...

class EmbeddedDocumentListField(Generic[_T], BaseField):
    def __new__(
        cls,
        kind: Type[_T],
        required: bool = ...,
        default: Optional[Any] = ...,
        help_text: str = ...,
    ) -> EmbeddedDocumentListField[_T]: ...
    def __getitem__(self, arg: Any) -> _T: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __set__(self, instance: Any, value: List[_T]) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> List[_T]: ...

class LazyReference(Generic[_T], BaseField):
    def __getitem__(self, arg: Any) -> LazyReference[_T]: ...

class LazyReferenceField(BaseField):
    def __init__(
        self,
        name: Union[str, Type[Document]],
        unique: bool = ...,
        required: bool = ...,
        help_text: Optional[str] = ...,
        reverse_delete_rule: Union[0, 1, 2, 3, 4] = ...,
    ) -> None: ...
    def __getitem__(self, arg: Any) -> LazyReference[Any]: ...

class URLField(Generic[_ST, _GT], StringField[_ST, _GT]):
    # URLField()
    @overload
    def __new__(
        cls,
        *,
        verify_exists: bool = ...,
        url_regex: Optional[Pattern[str]] = ...,
        schemas: Optional[Container[str]] = ...,
        regex: Optional[str] = ...,
        max_length: Optional[int] = ...,
        min_length: Optional[int] = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: None = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[str]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> URLField[Optional[str], Optional[str]]: ...
    # URLField(default="foo")
    @overload
    def __new__(
        cls,
        *,
        verify_exists: bool = ...,
        url_regex: Optional[Pattern[str]] = ...,
        schemas: Optional[Container[str]] = ...,
        regex: Optional[str] = ...,
        max_length: Optional[int] = ...,
        min_length: Optional[int] = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: Union[str, Callable[[], str]],
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[str]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> URLField[Optional[str], str]: ...
    # URLField(required=True)
    @overload
    def __new__(
        cls,
        *,
        verify_exists: bool = ...,
        url_regex: Optional[Pattern[str]] = ...,
        schemas: Optional[Container[str]] = ...,
        regex: Optional[str] = ...,
        max_length: Optional[int] = ...,
        min_length: Optional[int] = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True],
        default: None = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[str]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> URLField[str, str]: ...
    # URLField(required=True, default="foo")
    @overload
    def __new__(
        cls,
        *,
        verify_exists: bool = ...,
        url_regex: Optional[Pattern[str]] = ...,
        schemas: Optional[Container[str]] = ...,
        regex: Optional[str] = ...,
        max_length: Optional[int] = ...,
        min_length: Optional[int] = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True],
        default: Union[str, Callable[[], str]],
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[str]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> URLField[Optional[str], str]: ...
    def __set__(self, instance: Any, value: _ST) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> _GT: ...

class UUIDField(Generic[_ST, _GT], BaseField):
    @overload
    def __new__(
        cls,
        *,
        binary: bool = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: None = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[UUID]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> UUIDField[Optional[UUID], Optional[UUID]]: ...
    @overload
    def __new__(
        cls,
        *,
        binary: bool = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: Union[UUID, Callable[[], UUID]],
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[UUID]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> UUIDField[Optional[UUID], UUID]: ...
    @overload
    def __new__(
        cls,
        *,
        binary: bool = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True],
        default: None = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[UUID]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> UUIDField[UUID, UUID]: ...
    @overload
    def __new__(
        cls,
        *,
        binary: bool = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True],
        default: Union[UUID, Callable[[], UUID]],
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[UUID]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> UUIDField[Optional[UUID], UUID]: ...
    @overload
    def __new__(
        cls,
        *,
        binary: bool = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True] = ...,
        default: Union[UUID, None, Callable[[], UUID]] = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[True],
        choices: Optional[Iterable[UUID]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> UUIDField[UUID, UUID]: ...
    def __set__(self, instance: Any, value: _ST) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> _GT: ...

_Tuple2Like = Union[Tuple[Union[float, int], Union[float, int]], List[float], List[int]]

class GeoPointField(Generic[_ST, _GT], BaseField):
    @overload
    def __new__(
        cls,
        *,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: None = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[str]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> GeoPointField[_Tuple2Like | None, list[float] | None]: ...
    @overload
    def __new__(
        cls,
        *,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: Union[_Tuple2Like, Callable[[], _Tuple2Like]],
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[str]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> GeoPointField[_Tuple2Like | None, list[float]]: ...
    @overload
    def __new__(
        cls,
        *,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True],
        default: None = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[str]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> GeoPointField[_Tuple2Like, list[float]]: ...
    @overload
    def __new__(
        cls,
        *,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True],
        default: Union[_Tuple2Like, Callable[[], _Tuple2Like]],
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[str]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> GeoPointField[_Tuple2Like | None, list[float]]: ...
    def __set__(self, instance: Any, value: _ST) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> _GT: ...

_MapType = Dict[str, Any]

class MapField(DictField[_T]):
    pass

# TODO(sbdchd): we can make this generic if we want better typing for assignment
#     workflow = fields.ReferenceField("Dialog")
# if we monkey patch we can make this generic like:
#     workflow = fields.ReferenceField[Dialog]("Dialog")

class ReferenceField(BaseField):
    def __init__(
        self,
        model: str,
        required: bool = ...,
        name: Optional[str] = ...,
        help_text: Optional[str] = ...,
        blank: bool = ...,
    ) -> None: ...
    def __getitem__(self, arg: Any) -> Any: ...

_T_ENUM = TypeVar("_T_ENUM", bound=Enum)

class EnumField(Generic[_ST, _GT], BaseField):
    # EnumField(Foo)
    @overload
    def __new__(
        cls,
        enum: Type[_T_ENUM],
        *,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: None = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[_T_ENUM]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> EnumField[Optional[_T_ENUM], Optional[_T_ENUM]]: ...
    # EnumField(Foo, default=Foo.Bar)
    @overload
    def __new__(
        cls,
        enum: Type[_T_ENUM],
        *,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: Union[_T_ENUM, Callable[[], _T_ENUM]],
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[_T_ENUM]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> EnumField[Optional[_T_ENUM], _T_ENUM]: ...
    # EnumField(Foo, required=True)
    @overload
    def __new__(
        cls,
        enum: Type[_T_ENUM],
        *,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True],
        default: None = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[_T_ENUM]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> EnumField[_T_ENUM, _T_ENUM]: ...
    # EnumField(Foo, required=True, default=Foo.Bar)
    @overload
    def __new__(
        cls,
        enum: Type[_T_ENUM],
        *,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True],
        default: Union[_T_ENUM, Callable[[], _T_ENUM]],
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[Iterable[_T_ENUM]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> EnumField[Optional[_T_ENUM], _T_ENUM]: ...
    def __set__(self, instance: Any, value: Union[_ST, _T_ENUM]) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> _GT: ...
