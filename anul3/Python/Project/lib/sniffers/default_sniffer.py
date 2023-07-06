import asyncio
from threading import Thread
from typing import List

from lib.core import Sniffer
from lib.core.logger import Logger
from lib.core.exceptions import PacketInvalidPortException, \
    PacketValidationException

from lib.filters import DefaultFilter
from lib.models import NetworkPacket

class DefaultSniffer(object):
    """
    A wrapper class that will use the core.sniffer package

    It can be personalized for multiple types
    """
    def __init__(self, interface: str = None):
        self._logger = Logger.get_logger()
        self._sniffer = Sniffer(interface)
        self._event = False
        self._task = None
        self._state = None

    def get_filters(self) -> List[DefaultFilter]:
        """
        Adding all filters for NetworkPacket (this are pre request filters,
        to get only the NetworkPackets in scope)
        """
        raise NotImplementedError()

    def handle_packet(self, packet: NetworkPacket) -> None:
        """
        Getting only the important packets, here you can handle them how you like
        """
        raise NotImplementedError()

    def get_event(self):
        """
        This is for internal usage, to check wether we should close the sniffer or not
        """
        return self._event

    def set_closing(self):
        """
        This is for internal usage, to set the sniffer to shutdown
        """
        self._event = True

    def start(self) -> None:
        """
        Starts the sniffer in an async mode
        """
        self._logger.info("Starting %s sniffer", self.__class__.__name__)
        loop = asyncio.get_event_loop()

        t = Thread(target=self.__start_background_loop, args=(loop,), daemon=True)
        t.start()

        task = asyncio.run_coroutine_threadsafe(self.__sniff(), loop)
        
        try:
            task.result(1)
        except Exception:
            pass
        # self._task = asyncio.wait([self.__sniff()])
        # loop.run_until_complete(self._task)

    def __start_background_loop(self, loop) -> None:
        asyncio.set_event_loop(loop)
        loop.run_forever()

    async def __sniff(self) -> None:
        async for packet in self._sniffer.start():
            if self.get_event():
                self._logger.info('Closing %s sequence started', self.__class__.__name__)
                self._sniffer.set_closing()
                break
            try:
                for filt in self.get_filters():
                    filt.set_packet(packet)
                    filt.filter()

                self.handle_packet(packet)
            except PacketInvalidPortException:
                pass
            except PacketValidationException as err:
                self._logger.debug('Packet validation failed due to %s', err)
