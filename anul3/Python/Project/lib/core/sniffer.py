"""
Sniffer engine, the core of the application
"""
from os import geteuid
from socket import AF_PACKET, SOCK_RAW, ntohs, socket
from typing import AsyncGenerator

from lib.models import NetworkPacket

from .exceptions import PacketAnalyzerException
from .logger import Logger
from .analyzer import Analyzer

class Sniffer:
    """
    Reading all the packets from the network using the custom builf sniffer engine
    """
    ETH_P_ALL = ntohs(0x0003)
    BUFFER_SIZE = 65535

    def __init__(self, interface: str = None) -> None:
        self.__require_root()

        self._logger = Logger.get_logger()
        self._socket = socket(AF_PACKET, SOCK_RAW, Sniffer.ETH_P_ALL)
        self.__closing = False

        if interface is not None:
            self._socket.bind((interface, 0))

    def set_closing(self):
        """
        Greacefully uninit the class
        """
        self.__closing = True

    def __require_root(self) -> None:
        if geteuid() != 0:
            raise Exception('You must be running as root to start the sniffer!')

    def __close(self):
        self._socket.close()

    async def __get_packets(self) -> AsyncGenerator[bytes, None]:
        while not self.__closing:
            try:
                yield self._socket.recvfrom(Sniffer.BUFFER_SIZE)[0]
            finally:
                if self.__closing:
                    self.__close()
    
    async def start(self) -> AsyncGenerator[NetworkPacket, None]:
        """
        Starting to read all the data from the network using coroutines
        """
        async for packet in self.__get_packets():
            if self.__closing:
                self.__close()
                break
            try:
                self._logger.debug('Got a new packet from socket.')
                analyzer = Analyzer(packet)
                destructed_packet = analyzer.analyze()

                packet = NetworkPacket(destructed_packet)
                yield packet
            except PacketAnalyzerException as err:
                self._logger.debug("Failed to analyze packet. Error: %s", err)
