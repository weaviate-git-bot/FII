from PyQt6.QtWidgets import QLabel, QHBoxLayout


class Header:
    """
    The header from the main window. Here we will have some navigation buttons
    """
    def __init__(self) -> None:
        self.__layout = None

        self.__setup_layout()
    
    def __setup_layout(self) -> None:
        self.__layout = QHBoxLayout()
        self.__layout.addWidget(QLabel("Header"))

    def get_layout(self) -> QHBoxLayout:
        return self.__layout