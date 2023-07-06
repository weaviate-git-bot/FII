import struct
from ipaddress import IPv4Address
from typing import Dict

from ..exceptions import PacketAnalyzerException
from .default_packet import DefaultPacket


class Layer3Packet(DefaultPacket):
    """
    Parsing all Layer3 packets (version, source an destination ips)
    """
    SUPPORTED_VERSIONS = [
        0x45, # IP
    ]

    def parse(self) -> Dict[str, object]:
        data = dict()
        list_buff = struct.unpack('B11s4s4s', self.packet[14:34])

        data = {
            'version': list_buff[0],
            'src_ip': IPv4Address(list_buff[2]).compressed,
            'dest_ip': IPv4Address(list_buff[3]).compressed,
        }

        if data['version'] not in Layer3Packet.SUPPORTED_VERSIONS:
            raise PacketAnalyzerException(f"Layer3 version {data['version']} is not supported yet!")

        return data
