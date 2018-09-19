from enum import Enum

from CorePrint import CorePrint


class Color(Enum):
    red = 1
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    indigo = 6
    purple = 7



CorePrint.print_info(Color(1))
CorePrint.print_info(Color['red'])

subtype = Enum('subtype', ('plain', 'html'))

CorePrint.print_info(subtype.plain.value)