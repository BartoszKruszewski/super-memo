from pathlib import Path
import json

from src.common.Config import Config
from src.data_loader.LessonGroup import LessonGroup
from src.data_loader.Lesson import Lesson


class DataLoader:
    def run(self) -> LessonGroup:
        return self._load_lesson_group(Config.data_dir)

    def _load_lesson_group(self, group_path: Path) -> LessonGroup:
        lessons = []
        for path in group_path.glob("*"):
            if path.is_dir():
                lessons.append(self._load_lesson_group(path))
            elif path.suffix == ".json":
                lessons.append(self._load_lesson(path))
            else:
                raise ValueError(f"File {path} is not .json file!")
        return LessonGroup(name=group_path.stem, lessons=lessons)

    def _load_lesson(self, json_file_path: Path) -> Lesson:
        with open(json_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return Lesson(**data)
