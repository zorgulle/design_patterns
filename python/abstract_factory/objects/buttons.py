import abc


class Button(abc.ABC):
    @abc.abstractmethod
    def clic(self) -> None:
        pass


class HonkButton(Button):
    def clic(self) -> None:
        print("Honk Honk")


class HornButton(Button):
    def clic(self) -> None:
        print("Horn Horn")
