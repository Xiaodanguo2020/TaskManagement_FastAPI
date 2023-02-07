from pydantic import BaseModel
from enum import Enum
from typing import List


class Languages (str, Enum):
    c = "c"
    python = "python"
    javascript = "javascript"
    b = "b"
    java = "java"


class Programmer (BaseModel):
    id: int
    name: str
    languages: List[Languages]
