from os import path
from typing import List
from threading import Lock, Event as ThreadingEvent

from lib.core.exceptions import PacketValidationException
from lib.core.logger import Logger
from lib.models import NetworkPacket
from lib.filters import DefaultFilter
from lib.core.logger import Logger

class MessageBus(object):
    """
    A singleton instance that handles the communication between CUI (Console UI) and Sniffer
    """
    __INSTANCE__ = None
    MAX_PACKETS_LENGTHS = 10000
    DUMP_DIRECTORY = 'packets'

    def __init__(self) -> None:
        if MessageBus.__INSTANCE__ is not None:
            raise Exception("Class must be a singleton")

        self.__mutex_guard = Lock()

        self.__event = ThreadingEvent()

        self._packets = []
        self._filters = []
        self._filtered_packets = []

        self.packet_counter = 0
        self.__logger = Logger.get_logger()

        MessageBus.__INSTANCE__ = self

    @staticmethod
    def get_class() -> 'MessageBus':
        """
        Get the class if it's instanciated, otherwise it creates
        a new one and then it returns it.
        """
        if MessageBus.__INSTANCE__ is None:
            MessageBus()

        return MessageBus.__INSTANCE__

    def add_packet(self, packet: NetworkPacket) -> None:
        """
        Adds a new NetworkPacket to the list
        """
        self.__logger.info("Got new packet: %s", str(packet))

        self.__mutex_guard.acquire()

        self._packets.append(packet)

        self.__check_packet(packet)
        self.__dump_packet(packet)
        self.__clean_packets()

        self.__event.set()
        self.__mutex_guard.release()

    def get_packet_counter(self) -> int:
        """
        Gets the number of packets
        """
        return len(self._packets)

    def get_packets(self) -> List[NetworkPacket]:
        """
        Gets all the filtered packets
        """
        return self._filtered_packets

    def add_new_filter(self, filt: DefaultFilter) -> None:
        """
        Adds a new filter for the packets
        """
        self.__mutex_guard.acquire()
        while True:
            if filt in self._filters:
                break
            
            self._filters.append(filt)
            self.__logger.info('Added new filter: %s', filt.__class__.__name__)
            
            break
        self.__mutex_guard.release()

        self.filter()

    def clear_filters(self) -> None:
        """
        Removes all the existing filters
        """
        self.__mutex_guard.acquire()
        self._filters = []
        self.__mutex_guard.release()

        self.__logger.info('Cleared all filters')

        self.filter()

    def filter(self) -> None:
        """
        Removes all the packets from the list when new filters are applied
        """
        self.__mutex_guard.acquire()
        self._filtered_packets = []
        for packet in self._packets:
            self.__check_packet(packet)

        self.__mutex_guard.release()

    def check_event(self) -> bool:
        """
        Checks if the event is set (and clears it automatically if true)
        """
        if self.__event.is_set():
            self.__event.clear()
            return True

        return False

    def __clean_packets(self) -> None:
        if len(self._packets) < MessageBus.MAX_PACKETS_LENGTHS:
            return

        # here we want to make sure we don't run this code each and every time because it
        # cost to much so we will pop the first 10% of the items from the array
        self._packets = self._packets[MessageBus.MAX_PACKETS_LENGTHS * 0.1:]

    def __check_packet(self, packet: NetworkPacket) -> None:
        passed_all_filters = True
        for filt in self._filters:
            try:
                filt.set_packet(packet)
                filt.filter()
            except PacketValidationException:
                passed_all_filters = False
                break

        if passed_all_filters:
            self._filtered_packets.append(packet)

    def __dump_packet(self, packet: NetworkPacket) -> None:
        if not path.exists(MessageBus.DUMP_DIRECTORY):
            self.__logger.warning("Dump directory doesn't exist, please create it")
            return

        with open(path.join(MessageBus.DUMP_DIRECTORY, f"http_{str(self.packet_counter)}.txt"), 'w', encoding='utf-8') as df:
            df.write(str(packet))
            self.packet_counter += 1
        