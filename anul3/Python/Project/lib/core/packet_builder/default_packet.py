from ..logger import Logger
from typing import Dict

class DefaultPacket(object):
    """
    An abstract class that will be inherited by all packet destructors
    """

    def __init__(self, packet_data: bytes) -> None:
        self.packet = packet_data
        self._logger = Logger.get_logger()

    def parse(self) -> Dict[str, object]:
        """
        Parsing a packet based on rules.

        Output:
        A dictionary using a pairs of string -> object
        """
        raise NotImplementedError('This method is not implemented yet.')
