from dataclasses import dataclass, field
from typing import Dict
from datetime import datetime


@dataclass
class Lesson:
    name: str
    date: datetime = field(default_factory=lambda raw: datetime.strptime(raw, '%d-%m-%Y'))
    origin_language: str
    translation_language: str
    words: Dict[str, str]

    def __str__(self) -> str:
        return f"{self.name} [{self.date}]"
