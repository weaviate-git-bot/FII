from lib.models import HTTPModel
from .network_packet import NetworkPacket

class NetworkPacketHTTP(NetworkPacket):
    """
    Same as the NetworkPacket class but the type of payload is now specialized,
    being a HTTPModel
    """
    def set_payload(self, data: HTTPModel) -> None:
        """
        Setting the payload to be HTTPModel
        """
        self.payload = data
