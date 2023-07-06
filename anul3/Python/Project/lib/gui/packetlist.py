import json

from PyQt6.QtWidgets import QGroupBox, QHBoxLayout, QLabel, QDialog, QVBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal

class PacketList(QGroupBox):
    """
    The packet list that shows the packets (on the UI)
    """
    clicked = pyqtSignal(str, object)

    def __init__(self, packet, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setGeometry(10,10, 461, 65)
        self.setMinimumSize(461, 65)
        self.setMaximumSize(461, 65)
        self.packet = packet
        self.__layout = QHBoxLayout()
        self.__setup_layout(packet)

        self.setLayout(self.__layout)
        self.clicked.connect(self.mousePressEvent)

    def __setup_layout(self, packet) -> None:
        data =  packet.payload.get_data()
        
        label_text = [
            f'SOURCE: {packet.source.ip}:{packet.source.port:<4}'
            f'DEST: {packet.destination.ip}:{packet.destination.port:<4}'
        ]

        if data.get('method', '') != '':
            label_text.append(f'TYPE: {data["method"]} {data["path"]}')
        else:
            label_text.append(f'TYPE: {data["request_type"]}')

        for text in label_text:
            label = QLabel(text)
            label.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
            self.__layout.addWidget(label)

    # pylint: disable=invalid-name
    def mousePressEvent(self, event):
        """
        Shows the packet details when the packet is clicked
        """
        dlg = QDialog()
        dlg.setWindowTitle('Packet Details')
        dlg.setMinimumSize(500, 300)
        vbox = QVBoxLayout()
        label = QLabel(json.dumps({
            'source': str(self.packet.source),
            'destination': str(self.packet.destination),
            'payload': self.packet.payload.get_data()
        }, indent=2))
        label.setGeometry(100, 100, 450,250)
        label.setWordWrap(True)
        vbox.addWidget(label)
        dlg.setLayout(vbox)
        dlg.exec()