# Stubs for parser.parser (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from hachoir_py3.field import Parser as GenericParser
from typing import Any

class ValidateError(Exception): ...

class HachoirParser:
    def __init__(self, stream: Any, **args: Any) -> None: ...
    def createDescription(self): ...
    def createMimeType(self): ...
    def validate(self) -> None: ...
    description: Any = ...
    mime_type: Any = ...
    def createContentSize(self) -> None: ...
    content_size: Any = ...
    def createFilenameSuffix(self): ...
    filename_suffix: Any = ...
    @classmethod
    def getParserTags(cls): ...
    @classmethod
    def print_(cls, out: Any, verbose: Any) -> None: ...
    autofix: Any = ...

class Parser(HachoirParser, GenericParser):
    def __init__(self, stream: Any, **args: Any) -> None: ...


# Stubs for parser.guess (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class QueryParser:
    fallback: Any = ...
    other: Any = ...
    validate: bool = ...
    use_fallback: bool = ...
    parser_args: Any = ...
    db: Any = ...
    parsers: Any = ...
    def __init__(self, tags: Any) -> None: ...
    def __iter__(self): ...
    def translate(self, name: Any, value: Any): ...
    def parse(self, stream: Any, fallback: bool = ...): ...
    def doparse(self, stream: Any, fallback: bool = ...): ...

def guessParser(stream: Any): ...
def createParser(filename: Any, real_filename: Optional[Any] = ..., tags: Optional[Any] = ...): ...