import abc


class ScrollBar(abc.ABC):
    @abc.abstractmethod
    def scroll(self) -> None:
        pass


class TeleportScrollBar(ScrollBar):
    def scroll(self) -> None:
        print("Je me teleporte")


class SmurfScrollBar(ScrollBar):
    def scroll(self) -> None:
        print("Je smurf")
