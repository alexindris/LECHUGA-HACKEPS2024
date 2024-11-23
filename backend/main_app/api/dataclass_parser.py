from typing import Any, Dict, Optional, TypeVar, Type, get_origin, get_args
from dataclasses import is_dataclass, fields
import pytest

O = TypeVar(
    "O",
)


def parse_response(cls: Type[O], data: Dict[str, Any]) -> O:
    assert is_dataclass(cls), f"{cls} must be a dataclass"

    field_types = {f.name: f.type for f in fields(cls)}
    field_values = {}
    for field_name, field_type in field_types.items():
        value = data[field_name] if field_name in data else None

        if value is not None and get_origin(field_type) is list:
            list_type = get_args(field_type)[0]
            assert isinstance(
                value, list
            ), f"Field {field_name} is expected to be a list in response {data}"

            field_values[field_name] = [
                parse_response(list_type, item) if is_dataclass(list_type) else item
                for item in value
            ]

        elif value is not None and is_dataclass(field_type):
            assert isinstance(
                value, dict
            ), f"Field {field_name} is not a dict from response {data}"
            field_values[field_name] = parse_response(field_type, value)  # type: ignore

        else:
            field_values[field_name] = value

    return cls(**field_values)  # type: ignore
