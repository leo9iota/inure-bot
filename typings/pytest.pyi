from typing import Any, Callable, Optional, TypeVar, overload

_T = TypeVar("_T")
_F = TypeVar("_F", bound=Callable[..., Any])

class FixtureRequest:
    param: Any

class Config:
    pass

class Function:
    pass

class Parser:
    pass

class FixtureManager:
    pass

class Session:
    config: Config
    
def fixture(
    scope: str = "function",
    params: Optional[Any] = None,
    autouse: bool = False,
    ids: Optional[Any] = None,
    name: Optional[str] = None,
) -> Callable[[_F], _F]: ...

@overload
def mark(name: str, *args: Any, **kwargs: Any) -> Any: ...

@overload
def mark(__name: str) -> Any: ...

@overload
def raises(expected_exception: Any, *args: Any, **kwargs: Any) -> Any: ...

@overload
def raises(expected_exception: Any) -> Any: ...

def skip(reason: str = "") -> Any: ...

def fail(reason: str = "", pytrace: bool = True) -> Any: ...

def importorskip(modname: str, minversion: Optional[str] = None) -> Any: ...

def yield_fixture(
    scope: str = "function",
    params: Optional[Any] = None,
    autouse: bool = False,
    ids: Optional[Any] = None,
    name: Optional[str] = None,
) -> Callable[[_F], _F]: ...

def hookimpl(
    function: Optional[Callable[..., Any]] = None,
    firstresult: bool = False,
    tryfirst: bool = False,
    trylast: bool = False,
    hookwrapper: bool = False,
    optionalhook: bool = False,
    specname: Optional[str] = None,
) -> Any: ...

def param(*values: Any, id: Optional[str] = None, marks: Any = None) -> Any: ...
