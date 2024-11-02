from src.ui.UIStateEnum import UIStateEnum


class UIDesigner:
    def __call__(self, ui_state) -> str:
        return {
            UIStateEnum.MAIN_MENU: self._ui__main_menu,
            UIStateEnum.NEW_SESSION: self._ui__new_session,
            UIStateEnum.LESSONS_TREE: self._ui__lessons_tree,
            UIStateEnum.QUESTION: self._ui__question,
            UIStateEnum.ANSWER: self._ui__answer,
        }[ui_state]

    @property
    def _ui__main_menu(self) -> str:
        return ""

    @property
    def _ui__new_session(self) -> str:
        return ""

    @property
    def _ui__lessons_tree(self) -> str:
        return ""

    @property
    def _ui__question(self) -> str:
        return ""

    @property
    def _ui__answer(self) -> str:
        return ""
