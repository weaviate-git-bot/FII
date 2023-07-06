"""
Packet validation exception
"""

class PacketValidationException(Exception):
    """
    The specific packet has failed validation due to a specific reason
    """

    def __init__(self, message):
        super().__init__(message)
