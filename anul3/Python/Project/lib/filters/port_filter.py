from typing import List

from lib.core.exceptions import PacketInvalidPortException

from .default_filter import DefaultFilter

class PortFilter(DefaultFilter):
    """
    Filtering the ports from packets. With this filter you can allow or disallow specific ports
    """
    def __init__(self, port_list: List[int], allow: bool = True) -> None:
        """
        Params:
        port_list: a list of all ports
        allow: wether to allow only packets that contain that port or disallow those.

        For exampel [22, 1337], allow will return only packets that have on src or dest that port.
        """
        super().__init__()
        self._port_list = port_list
        self._allow = allow

    def filter(self) -> None:
        """
        Checks wether all ports from packet are allowed or not
        """
        packet_ports = [self.packet.source.port, self.packet.destination.port]

        for port in self._port_list:
            if port not in packet_ports:
                continue

            if self._allow:
                continue

            raise PacketInvalidPortException(f'Port {port} has been filtered out. Dropping package')
