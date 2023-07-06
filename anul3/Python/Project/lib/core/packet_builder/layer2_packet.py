import struct
from socket import htons
from typing import Dict

from .default_packet import DefaultPacket

class Layer2Packet(DefaultPacket):
    """
    Parsing all Layer2 packets (dest_mac, src_mac, protype)
    """
    def __get_mac_string(self, mac_string: bytes) -> str:
        return mac_string.hex(':')

    def parse(self) -> Dict[str, object]:
        data = dict()

        list_buff = struct.unpack('! 6s 6s H', self.packet[:14])
        data = {
            'dest_mac': self.__get_mac_string(list_buff[0]),
            'src_mac': self.__get_mac_string(list_buff[1]),
            'prototype': htons(list_buff[2])
        }
        return data