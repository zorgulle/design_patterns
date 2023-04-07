import abc

from objects import (
    FunkyButton,
    FunkyScrollbar,
    IButton,
    IScrollbar,
    NinjaButton,
    NinjaScrollbar,
)


class IThemeAbstractFactory(abc.ABC):
    @abc.abstractmethod
    def create_scrollbar(self) -> IScrollbar:
        pass

    @abc.abstractmethod
    def create_button(self) -> IButton:
        pass


class NinjaThemeFactory(IThemeAbstractFactory):
    def create_scrollbar(self) -> IScrollbar:
        return NinjaScrollbar()

    def create_button(self) -> IButton:
        return NinjaButton()


class FunkyThemeFactory(IThemeAbstractFactory):
    def create_scrollbar(self) -> IScrollbar:
        return FunkyScrollbar()

    def create_button(self) -> IButton:
        return FunkyButton()
