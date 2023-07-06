from typing import Dict

from ..exceptions import PacketAnalyzerException

from .default_packet import DefaultPacket


class Layer7Packet(DefaultPacket):
    """
    Parsing all Layer7 packets (a.k.a the payload)
    """

    def parse(self) -> Dict[str, object]:
        packet_len = len(self.packet)
        if packet_len <= 66:
            raise PacketAnalyzerException(
                f'Packet has a smaller length then required: {packet_len} <= 66')
        return {
            'payload': self.packet[66:],
        }
