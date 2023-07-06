import signal
import sys

from lib.core.logger import Logger
from lib.sniffers import HTTPSniffer
from lib.gui import UI

def main():
    """
    The entrypoint of the application
    """
    sniffer = HTTPSniffer()

    def signal_handler(status: int, frame: object) -> None:
        """
        Handling keyboard or internal state signals.
        Implemented handlers:
            - SIGINT
        """
        sniffer.set_closing()
        Logger.get_logger().info('Sniffer exitting with status %d. Bye bye!', status)
        sys.exit(0)
    signal.signal(signal.SIGINT, signal_handler)

    ui = UI(sys.argv)
    sniffer.start()
    ui.render()

if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        Logger.get_logger().critical('Failed to start the application. Error: %s', err)
