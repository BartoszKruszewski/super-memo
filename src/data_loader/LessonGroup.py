from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union
from src.data_loader.Lesson import Lesson


@dataclass
class LessonGroup:
    name: str
    lessons: List[Union[Lesson, LessonGroup]]

    def __str__(self) -> str:
        def _rec(lesson_group: LessonGroup, indent: int = 0) -> str:
            return "\n".join([
                f"{' ' * indent}{lesson_group.name} ({len(lesson_group.lessons)})",
                *[
                    _rec(lesson, indent + 1)
                    if isinstance(lesson, LessonGroup)
                    else f"{' ' * indent}- {lesson}]"
                    for lesson in lesson_group.lessons
                ]
            ])

        return _rec(self.lessons)
