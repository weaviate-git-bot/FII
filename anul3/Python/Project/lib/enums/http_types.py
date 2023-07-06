from enum import Enum

class HttpDirections(Enum):
    """
    Listing all types of HTTP Directions for packets
    """
    UNKOWN = 0
    REQUEST = 1
    RESPONSE = 2
    PAYLOAD = 3

    def __str__(self):
        return {
            0: 'Unknown',
            1: 'Request',
            2: 'Response',
            3: 'Payload'
        }[self.value]
