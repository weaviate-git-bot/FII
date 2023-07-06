class HWEntity(object):
    """
    Getting all the necesary fields for a hardware entity
    """

    def __init__(self, mac: str, ip: str, port: int) -> None:
        self.mac = mac
        self.ip = ip
        self.port = port

    def __str__(self):
        return f"HWEntity({self.mac}, {self.ip}, {self.port})"
