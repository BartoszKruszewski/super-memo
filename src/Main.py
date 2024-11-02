from src.data_loader.DataLoader import DataLoader
from src.ui.UIManager import UIManager
from src.ui.UIStateEnum import UIStateEnum


class Main:
    def __init__(self):
        self._is_running = False
        self._lessons = DataLoader().run()
        self._ui_manager = UIManager()
        self._ui_state = UIStateEnum.MAIN_MENU

    def run(self):
        self._is_running = True

        while self._is_running:
            self._ui_manager.print(self._ui_state)
        self._handle_input()

    def _handle_input(self):
        {
            (UIStateEnum.MAIN_MENU): self._in__main_menu,
            (UIStateEnum.NEW_SESSION): self._in__new_session,
            (UIStateEnum.LESSONS_TREE): self._in__lessons_tree,
            (UIStateEnum.QUESTION): self._in__question,
            (UIStateEnum.ANSWER): self._in__answear,
        }[self._ui_state](input())

    def _in__main_menu(self, input: str):
        match input:
            case "1":
                self._ui_state = UIStateEnum.NEW_SESSION
            case "2":
                self._ui_state = UIStateEnum.LESSONS_TREE
            case "3":
                self._is_running = False

    def _in__new_session(self, input):
        pass

    def _in__lessons_tree(self, input):
        pass

    def _in__question(self, input):
        pass

    def _in__answear(self, input):
        pass
