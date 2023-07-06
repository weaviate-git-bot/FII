from lib.filters import DefaultFilter

class AllowOnlyGet(DefaultFilter):
    """
    Checks for the method of the packet to be GET, otherwise it returns false
    """
    def filter(self):
        if self.packet.payload.get_data().get('method', '') == 'GET':
            return True
        
        self._raise('method is not get')