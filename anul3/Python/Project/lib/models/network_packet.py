from typing import Dict

from .hw_entity import HWEntity

class NetworkPacket(object):
    """
    A model that represents a network packet already parsed by the analyzer module

    It splits the data into:
    - source: HWEntity
    - destination: HWEntity
    - payload: bytes
    """

    def __init__(self, data: Dict[str, object] = None) -> None:
        if data is None:
            return

        self.source = HWEntity(data['src_mac'], data['src_ip'], data['src_port'])
        self.destination = HWEntity(data['dest_mac'], data['dest_ip'], data['dest_port'])
        self.payload: bytes = data['payload']

    def set_source(self, data: HWEntity) -> None:
        """
        Setter for self.source
        """
        self.source = data

    def set_destiantion(self, data: HWEntity) -> None:
        """
        Setter for self.destination
        """
        self.destination = data

    def set_payload(self, data: bytes) -> None:
        """
        Setter for self.payload
        """
        self.payload = data

    def __str__(self):
        return f"{self.source} -> {self.destination} : {str(self.payload)}"