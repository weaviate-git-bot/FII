import struct
from typing import Dict

from ..exceptions import PacketAnalyzerException

from .default_packet import DefaultPacket


class Layer4Packet(DefaultPacket):
    """
    Parsing all Layer4 packets (src & dest ports)
    """

    def parse(self) -> Dict[str, object]:
        data = dict()

        packet_len = len(self.packet)
        if packet_len < 66:
            raise PacketAnalyzerException(
                f'Packet has a smaller length then required: {packet_len} < 66')

        list_buff = struct.unpack('!HH28s', self.packet[34:66])

        data = {
            'src_port': list_buff[0],
            'dest_port': list_buff[1]
        }

        return data
