from lib.filters import DefaultFilter

class AllowTrafficOnlyOnPort(DefaultFilter):
    """
    Allows the traffic only if it's made on port 80. Other ports will be dropped

    NOTE: The port 80 must be either on source or destination to return true
    """
    def filter(self):
        if (self.packet.source.port == 80 or self.packet.destination.port == 80):
            return True
        
        self._raise('Traffic is originating or going to other ports')