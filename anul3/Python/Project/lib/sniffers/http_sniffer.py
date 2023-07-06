from typing import List

from lib.filters import DefaultFilter, HTTPFilter, PortFilter
from lib.models import NetworkPacket, HTTPModel, NetworkPacketHTTP
from lib.message_bus import MessageBus

from .default_sniffer import DefaultSniffer

class HTTPSniffer(DefaultSniffer):
    """
    A specialized sniffer that handles only HTTP traffic.

    To apply filters please use packet filters.http
    """

    def get_filters(self) -> List[DefaultFilter]:
        return [
            PortFilter([22, 5353, 35659], False),
            HTTPFilter()
        ]

    def handle_packet(self, packet: NetworkPacket) -> None:
        # building the HTTP Payload
        http_model = HTTPModel(packet.payload)

        # creating a new packet with the HTTP Payload
        new_packet = NetworkPacketHTTP()
        new_packet.set_destiantion(packet.destination)
        new_packet.set_source(packet.source)
        new_packet.set_payload(http_model)

        # working with the message bus to display it
        msg_bus = MessageBus.get_class()
        msg_bus.add_packet(new_packet)
