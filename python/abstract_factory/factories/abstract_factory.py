import abc

from objects.scrollbars import ScrollBar
from objects.buttons import Button


class ThemeAbstrastFactory(abc.ABC):
    """Abstract factory class define methode to build object that must work together"""

    @abc.abstractmethod
    def create_scrollbar(self) -> ScrollBar:
        pass

    @abc.abstractmethod
    def create_button(self) -> Button:
        pass
