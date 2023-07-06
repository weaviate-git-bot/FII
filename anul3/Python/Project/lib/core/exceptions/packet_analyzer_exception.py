"""
Packet analyzing exception
"""

class PacketAnalyzerException(Exception):
    """
    The specific packet has failed the parsing due to a specific reason
    """

    def __init__(self, message):
        super().__init__(message)
