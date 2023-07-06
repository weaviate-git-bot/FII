"""
Packet validation exception
"""

class PacketInvalidPortException(Exception):
    """
    The specific packet has failed validation due to port being out of interest zone
    """

    def __init__(self, message):
        super().__init__(message)
