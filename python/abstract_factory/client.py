from factorie import IThemeAbstractFactory, NinjaThemeFactory
from objects import IButton, IScrollbar


def main():
    theme_factory: IThemeAbstractFactory = NinjaThemeFactory()

    scrollbar: IScrollbar = theme_factory.create_scrollbar()
    button: IButton = theme_factory.create_button()

    scrollbar.scroll()
    button.clic()


if __name__ == "__main__":
    main()
