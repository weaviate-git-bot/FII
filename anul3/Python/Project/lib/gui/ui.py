from typing import List
from PyQt6.QtWidgets import QApplication

from .main_window import MainWindow

class UI:
    """
    The UI for the sniffer core application (it will use the MessageBus to communicate)
    """
    def __init__(self, argv: List[str]):
        self.__application = QApplication(argv)
        self.__application.setApplicationName("HTTP - The Sniffer")

    def render(self):
        """
        Starts the UI to render the main window
        """
        window = MainWindow()
        window.show()
        self.__application.exec()