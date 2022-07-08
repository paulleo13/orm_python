from enum import Enum


class CreateEnum(Enum):
    DATABASE = "database"
    TABLE = "table"
    INDEX = "index"
    VIEW = "view"


class DropEnum(Enum):
    DATABASE = "database"
    TABLE = "table"
    INDEX = "index"


class JoinEnum(Enum):
    INNER_JOIN = "inner_join"
    RIGHT_JOIN = "right_join"
    LEFT_JOIN = "left_join"
    FULL_JOIN = "full_join"