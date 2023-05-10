from enum import Enum

class VC(Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4

class VI(Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3

class SBBE(Enum):
    ZERO = 0
    NON_ZERO = 1

class SIT(Enum):
    FALSE = 0
    TRUE = 1

class DA(Enum):
    FALSE = 0
    TRUE = 1

class DTA(Enum):
    ZERO = 0
    ONE = 1

class GR(Enum):
    ZERO = 0
    ONE = 1
    TWO = 2


class SCT(Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4

INPUTS = [VC, SBBE, SIT, DA, DTA, VI, GR]

OUTPUTS = [SCT]
