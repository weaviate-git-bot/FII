from functools import partial
from PyQt6.uic.load_ui import loadUi
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt6.QtCore import QTimer, Qt

from lib.message_bus import MessageBus
from lib.filters.http import FILTERS_LIST

from .packetlist import PacketList

class MainWindow(QWidget):
    """
    The main UI window that shows the packets
    """
    def __init__(self):
        super().__init__()
        loadUi('lib/gui/ui/main_window.ui', self)
        self.message_bus = MessageBus().get_class()
        self.__config_window()
        self.__add_packet()
        self.__add_filters()

        self.counter = 0
        self.timer_to_update_packets = QTimer(self)
        self.timer_to_update_packets.setInterval(500) #.5 seconds

        self.timer_to_update_packets.timeout.connect(self.read_packets)
        self.timer_to_update_packets.start()

    def read_packets(self) -> None:
        """
        Updates the UI in case a new packet is received
        """
        for idx in reversed(range(self.vbox.count())): 
            self.vbox.itemAt(idx).widget().setParent(None)
        self.counter = 0
        for packet in self.message_bus.get_packets():
            self.vbox.addWidget(PacketList(packet))
            self.counter += 1
        self.current_packets.setText(f'Current Packets: {self.counter}')

    def __config_window(self) -> None:
        self.setWindowTitle("HTTP - The Sniffer")
        self.version.setText('Version: 1.0')
        self.interface_2.setText('Interface: any')

    def __add_packet(self) -> None:
        self.vbox = QVBoxLayout()
        self.scroll_packets.setLayout(self.vbox)

        self.list_packets.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.list_packets.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.list_packets.setWidgetResizable(True)
        self.list_packets.setWidget(self.scroll_packets)

    def __add_filters(self) -> None:
        self.vbox_filters = QVBoxLayout()
        idx = 0
        
        for filt in FILTERS_LIST:
            btn = QPushButton(filt.__name__)
            btn.clicked.connect(partial(self.message_bus.add_new_filter, filt()))
            idx += 1
            btn.setMinimumHeight(50)
            btn.setToolTip(filt.__doc__)
            self.vbox_filters.addWidget(btn)

        self.scroll_filters.setLayout(self.vbox_filters)

        self.list_filters.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.list_filters.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.list_filters.setWidgetResizable(True)
        self.list_filters.setWidget(self.scroll_filters)

        self.reset_filters.clicked.connect(self.message_bus.clear_filters)

    def __hello(self, idx) -> None:
        print('Cliecked Hello at ', idx)