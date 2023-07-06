from lib.core.logger import Logger

from lib.models import NetworkPacket

from lib.core.exceptions import PacketValidationException

class DefaultFilter(object):
    """
    Custom rules for network packets.
    They can filter anything from source -> destination pairs to payloads
    """

    def __init__(self) -> None:
        self.packet = None
        self._logger = Logger.get_logger()

    def set_packet(self, packet: NetworkPacket) -> 'DefaultFilter':
        """
        Sets the network packet to be filtered
        """
        self.packet = packet
        return self

    def _raise(self, msg: str) -> None:
        raise PacketValidationException(msg)

    def filter(self) -> None:
        """
        Applies a custom rule for a network packet.
        """
        raise NotImplementedError('This method is not implemented yet')
