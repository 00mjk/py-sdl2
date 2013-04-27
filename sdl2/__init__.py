"""SDL2 wrapper package"""
from .dll import get_dll_file, _bind
from ctypes import c_int as _cint


#__all__ = ["SDL_INIT_TIMER", "SDL_INIT_AUDIO", "SDL_INIT_VIDEO",
#           "SDL_INIT_JOYSTICK", "SDL_INIT_HAPTIC", "SDL_INIT_GAMECONTROLLER",
#           "SDL_INIT_NOPARACHUTE", "SDL_INIT_EVERYTHING", "SDL_Init",
#           "SDL_InitSubSystem", "SDL_QuitSubSystem", "SDL_WasInit", "SDL_Quit",
#           "version_info"
#           ]


from .audio import *
from .blendmode import *
from .clipboard import *
from .cpuinfo import *
from .endian import *
from .error import *
from .events import *
from .gamecontroller import *
from .gesture import *
from .haptic import *
from .hints import *
from .joystick import *
from .keyboard import *
from .loadso import *
from .log import *
from .messagebox import *
from .mouse import *
from .pixels import *
from .platform import *
from .power import *
from .rect import *
from .render import *
from .rwops import *
from .shape import *
from .stdinc import *
from .surface import *
from .syswm import *
from .timer import *
from .touch import *
from .version import *
from .video import *

from .keycode import *
from .scancode import *

SDL_INIT_TIMER = 0x00000001
SDL_INIT_AUDIO = 0x00000010
SDL_INIT_VIDEO = 0x00000020
SDL_INIT_JOYSTICK = 0x00000200
SDL_INIT_HAPTIC = 0x00001000
SDL_INIT_GAMECONTROLLER = 0x00002000
SDL_INIT_NOPARACHUTE = 0x00100000
SDL_INIT_EVERYTHING = 0x0000FFFF

SDL_Init = _bind("SDL_Init", [Uint32], _cint)
SDL_InitSubSystem = _bind("SDL_InitSubSystem", [Uint32], _cint)
SDL_QuitSubSystem = _bind("SDL_QuitSubSystem", [Uint32])
SDL_WasInit = _bind("SDL_WasInit", [Uint32], Uint32)
SDL_Quit = _bind("SDL_Quit")

__version__ = "0.2.0"
version_info = (0, 2, 0, "")