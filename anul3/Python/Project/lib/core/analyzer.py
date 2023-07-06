from typing import Dict, List

from .logger import Logger

from .packet_builder import DefaultPacket, Layer2Packet, \
    Layer3Packet, Layer4Packet, \
    Layer7Packet

class Analyzer:
    """
    Analyze a new package received from sniffer class.
    This will parse the packet as described here:
    https://www.uv.mx/personal/angelperez/files/2018/10/sniffers_texto.pdf
    """
    def __init__(self, packet_data: bytes) -> None:
        self._packet = packet_data
        self._logger = Logger.get_logger()
        self._parsers : List[DefaultPacket] = [
            Layer2Packet,
            Layer3Packet,
            Layer4Packet,
            Layer7Packet
        ]

    def analyze(self) -> Dict[str, object]:
        """
        Parsing a network package using layers
        """
        packet_data = dict()

        for parser in self._parsers:
            packet_data = packet_data | parser(self._packet).parse()

        self._logger.debug('Successfully parsed packed')
        return packet_data

        