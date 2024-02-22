from gettext import gettext as _

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import pygame

from sugar3.activity.activity import Activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import StopButton, ActivityToolbarButton


import sugargame.canvas
import main

DESCRIPTION = """Number Guessing is a mathematical game. You have to think of a number lying between 1 and 100 (both inclusive).
After that, you need to press on "Yes" or "No" depending on whether the number you thought of is present on the screen or not.
Your number will be guessed correctly after you repeat this task 7 times. You can press on "Reset" at any point to think of another number.
"""

class NumberGuessingActivity(Activity):

    def __init__(self, handle):
        Activity.__init__(self, handle)

        self.game = main.NumberGuessing()
        self.metadata['description'] = DESCRIPTION
        
        self.build_toolbar()
        self._pygamecanvas = sugargame.canvas.PygameCanvas(self, main=self.game.run, modules=[pygame.display])

        self.set_canvas(self._pygamecanvas)
        self._pygamecanvas.grab_focus()

    def build_toolbar(self):
        toolbar_box = ToolbarBox()
        
        activity_button = ActivityToolbarButton(self)
        toolbar_box.toolbar.insert(activity_button, 0)
        activity_button.show()

        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()
        stop_button.connect('clicked', self._stop_cb)

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

    def _stop_cb(self, button):
        self.game.is_running = False
