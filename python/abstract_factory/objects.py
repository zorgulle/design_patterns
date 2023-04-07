import abc


class IButton(abc.ABC):
    @abc.abstractmethod
    def clic(self):
        pass


class FunkyButton(IButton):
    def clic(self):
        print("Funky button")


class NinjaButton(IButton):
    def clic(self):
        print("Ninja button")


class IScrollbar(abc.ABC):
    @abc.abstractmethod
    def scroll(self):
        pass


class FunkyScrollbar(IScrollbar):
    def scroll(self):
        print("Funky scroll bar")


class NinjaScrollbar(IScrollbar):
    def scroll(self):
        print("Ninja scroll bar")
