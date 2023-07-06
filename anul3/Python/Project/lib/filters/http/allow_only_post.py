from lib.filters import DefaultFilter

class AllowOnlyPost(DefaultFilter):
    """
    Checks for the method of the packet to be POST, otherwise it returns false
    """
    def filter(self):
        if self.packet.payload.get_data().get('method', '') == 'POST':
            return True
        
        self._raise('method is not post')