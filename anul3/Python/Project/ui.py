"""
I use this module to the the GUI on macos (where the sniffer doesn't work because Apple is Apple)
"""
import sys
from lib.gui import UI

ui = UI(sys.argv)
ui.render()
