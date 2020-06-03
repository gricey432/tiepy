from abc import ABC, abstractmethod
from typing import List, Dict, Any
from dataclasses import dataclass


@dataclass
class Issue:
    """A finding with a module"""
    filename: str
    line_no: int
    message: str

    def to_print_str(self) -> str:
        return f"{self.filename}:{self.line_no} {self.message}"


class Checker(ABC):
    @abstractmethod
    def check_module(self, module: Dict[str, Any]) -> List[Issue]:
        pass
