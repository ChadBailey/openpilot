"""
OpenPilot constants, holds things which do not need to be frequently changed, if
ever changed at all.
"""

# Terminal Constants - for stylizing the terminal
from enum import Enum, auto
from string import Template
from typing import Dict

class TERM_COLORS:
    """
    Numerical terminal color codes, can not be used in isolation without 
    additional control characters.
    
    Note that all colors assume using basic color range only

    Refer to `TERM_THEMES` for ready-to-use themes

    ## Color Ranges
        Basic color range:      30-37
        High contrast range:    90-97
        xterm-256 colors:       0-255
    Further reading: http://jafrog.com/2013/11/23/colors-in-terminal.html
    """
    BLACK       = "30"
    RED         = "31"
    GREEN       = "32"
    YELLOW      = "33"
    DARK_BLUE   = "34"
    """Blue, but difficult to read on many monitors"""
    MAGENTA     = "35"
    LIGHT_BLUE  = "36"


class TERM_STYLES:
    """Terminal styles, i.e. bold, underline, color the background."""
    NONE        = ""
    BOLD        = ";1"
    BACKGROUND  = ";3"
    UNDERLINE   = ";4"

class TERM_CONTROL_CHARS:
    _e = "\u001b"
    """Escape sequence ascii code - prefixes all terminal control chars"""
    ESCAPE_CODE     = _e + "["
    """Escape sequence ascii code"""
    END_MARKER      = "m"
    """Marker that makes the end of control char input"""
    CLEAR           = f"{ESCAPE_CODE}0{END_MARKER}"
    COLOR_TEMPLATE = Template(ESCAPE_CODE + "${color}" + END_MARKER + "${text}" + CLEAR)

class TERM_THEMES(Enum):
    NONE = auto()
    RUNNING = auto()
    STOPPED = auto()

class TERM_TEMPLATES:
    NONE: Template = Template("$text")
    RUNNING: Template = Template(TERM_CONTROL_CHARS.COLOR_TEMPLATE.substitute(color=TERM_COLORS.GREEN,text="${process_name}"))
    # NOTE: Stopped theme prefixes with asterisk for color blindness accessibility
    STOPPED: Template = Template(TERM_CONTROL_CHARS.COLOR_TEMPLATE.substitute(color=TERM_COLORS.RED,text="*${process_name}"))
