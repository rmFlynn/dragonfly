#
# This file is part of Dragonfly.
# (c) Copyright 2007, 2008 by Christo Butcher
# Licensed under the LGPL.
#
#   Dragonfly is free software: you can redistribute it and/or modify it
#   under the terms of the GNU Lesser General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Dragonfly is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   Lesser General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public
#   License along with Dragonfly.  If not, see
#   <http://www.gnu.org/licenses/>.
#

import sys

# --------------------------------------------------------------------------

from .actions           import (ActionBase, DynStrActionBase, ActionError,
                                Repeat, Key, Text, Mouse, Paste, Pause,
                                WaitWindow, FocusWindow,
                                Function, StartApp, BringApp, PlaySound,
                                Typeable, Keyboard, typeables, RunCommand,
                                ContextAction)

if sys.platform.startswith("win"):
    from .actions       import (KeyboardInput, MouseInput, HardwareInput,
                                make_input_array, send_input_array)

# --------------------------------------------------------------------------

from .util              import Clipboard

# --------------------------------------------------------------------------

from .windows.rectangle import Rectangle, unit
from .windows.point     import Point
from .windows           import Window, Monitor, monitors

# --------------------------------------------------------------------------
from .accessibility     import (CursorPosition, TextQuery,
                                get_accessibility_controller,
                                get_stopping_accessibility_controller)
