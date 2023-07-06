from .default_filter import DefaultFilter

class HTTPFilter(DefaultFilter):
    """
    Filtering only the packets that contain some readable HTTP content
    """

    def filter(self) -> None:
        """
        Checks wether we can find at least one of the following keywards:
        HTTP/, User-Agent, GET, POST, PUT, PATCH, DELETE, OPTIONS, HEAD, COPY, Content-Type, Host,
        """

        guessing_if_is_http = [
            "HTTP/", "User-Agent", "GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "HEAD", "COPY", 
            "Content-Type", "Host",
        ]

        try:
            decoded_packet = self.packet.payload.decode('utf-8')
            for verb in guessing_if_is_http:
                if verb in decoded_packet:
                    return True
            raise ValueError('not a verb')
        except UnicodeDecodeError:
            self._logger.debug('Payload is not unicode encoded')
            self._raise('The package is not an HTTP package. Reason: can\'t decode the payload')
        except ValueError:
            self._raise('The package is not an HTTP package. Reason: no verb found')
