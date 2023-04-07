from factories.abstract_factory import ThemeAbstrastFactory
from factories.funky_theme_factory import FunkyTheme
from objects.buttons import Button
from objects.scrollbars import ScrollBar


def main():
    factory: ThemeAbstrastFactory = FunkyTheme()

    button: Button = factory.create_button()
    scrollbar: ScrollBar = factory.create_scrollbar()

    button.clic()
    scrollbar.scroll()


if __name__ == "__main__":
    main()
