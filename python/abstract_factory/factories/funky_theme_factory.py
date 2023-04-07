from .abstract_factory import ThemeAbstrastFactory
from objects.scrollbars import ScrollBar, TeleportScrollBar
from objects.buttons import Button, HonkButton


class FunkyTheme(ThemeAbstrastFactory):
    def create_scrollbar(self) -> ScrollBar:
        return TeleportScrollBar()

    def create_button(self) -> Button:
        return HonkButton()
