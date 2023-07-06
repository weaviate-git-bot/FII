import json
from typing import List

from lib.enums import HttpDirections

class HTTPModel:
    """
    Parsing an http payload
    """
    METHODS = [
        "GET",
        "POST",
        "PUT",
        "PATCH",
        "DELETE",
        "OPTIONS",
        "HEAD",
        "COPY"
    ]

    def __init__(self, data: bytes) -> None:
        self._request = data.decode('utf-8').replace('\r\n','\n')

        self._direction = HttpDirections.UNKOWN
        self._method = ''
        self._path = ''
        self._http_version = ''
        self._headers = dict()
        self._payload = ''
        self._status = ''
        self._status_description = ''

        self.__build()

    def get_data(self) -> dict:
        """
        Returns the data of the http payload
        """
        return {
            'request_type': str(self._direction),
            'method': self._method,
            'path': self._path,
            'status_code': self._status,
            'status_code_description': self._status_description,
            'http_version': self._http_version,
            'headers': self._headers,
            'payload': self._payload
        }

    def __build(self) -> None:
        lines: List[str] = [x for x in self._request.split('\n') if len(x) > 0]

        if len(lines) <= 0:
            raise Exception('Payload body is empty')

        self._direction = self.__get_direction(lines[0])

        {
            HttpDirections.PAYLOAD: self.__build_payload,
            HttpDirections.REQUEST: self.__build_request,
            HttpDirections.RESPONSE: self.__build_response
        }[self._direction](lines)

    def __get_direction(self, first_line: str) -> HttpDirections:
        if first_line.startswith('HTTP/1.'):
            return HttpDirections.RESPONSE

        for method in HTTPModel.METHODS:
            if first_line.startswith(method):
                return HttpDirections.REQUEST

        return HttpDirections.PAYLOAD

    def __build_payload(self, lines) -> None:
        self._payload = self._request

    def __build_request(self, lines) -> None:
        self._method, self._path, self._http_version = lines[0].split(' ')
        offset = 0
        if self._method == 'POST':
            self._payload = lines[-1]
            offset = 1

        self.__build_headers(lines, offset)

    def __build_response(self, lines) -> None:
        self._http_version, self._status, self._status_description = lines[0].split(' ',2)
        self.__build_headers(lines)

    def __build_headers(self, lines: List[str], offset: int = 0) -> None:
        for header in lines[1:-1 - offset]:
            if header.find(':') == -1:
                return
            key, value = header.split(':', 1)
            self._headers[key] = value.strip()

    def __str__(self) -> str:
        return json.dumps(self.get_data(), indent=2)
