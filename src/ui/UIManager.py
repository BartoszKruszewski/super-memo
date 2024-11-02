import os
from src.ui.UIStateEnum import UIStateEnum
from src.ui.UIDesigner import UIDesigner


class UIManager:
    def print(self, ui_state: UIStateEnum):
        self._cls()
        print(UIDesigner(ui_state))

    def _cls(self):
        os.system('cls' if os.name == 'nt' else "clear")
