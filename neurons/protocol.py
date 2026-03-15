"""Lucid Subnet Protocol — defines query and response formats."""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class LucidQuery:
    query_type: str = "package"
    name: str = ""
    registry: str = "npm"

    def to_dict(self) -> dict:
        return {
            "type": self.query_type,
            "name": self.name,
            "registry": self.registry,
        }


@dataclass
class LucidResponse:
    name: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    error: Optional[str] = None
    response_time_ms: float = 0.0

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "error": self.error,
            "response_time_ms": self.response_time_ms,
        }
