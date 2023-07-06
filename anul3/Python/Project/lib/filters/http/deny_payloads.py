from lib.filters import DefaultFilter
from lib.enums import HttpDirections

class DenyPayloads(DefaultFilter):
    """
    Denies all types of payloads (e.g. reponse body)
    """
    def filter(self):
        if self.packet.payload.get_data().get('request_type', '') != str(HttpDirections.PAYLOAD):
            return True
        
        self._raise('method is not get')