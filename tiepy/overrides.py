"""
Allows marking of a function as overriding a parent or a function which shouldn't be overridden as final
"""
from typing import TypeVar
from types import FunctionType


_WrappedMethod = TypeVar("_WrappedMethod", bound=FunctionType)


def overrides(method: _WrappedMethod) -> _WrappedMethod:
    """
    Marks a method as overriding the same-named method on its parent
    TiePy checking will fail if the decorated method doesn't override a parent method
    """
    method.__tiepy_overrides = True
    return method


def final(method: _WrappedMethod) -> _WrappedMethod:
    """
    Marks a method as not allowed to be overridden by any child classes
    TiePy checking will fail if any child classes override this function
    """
    method.__tiepy_final = True
    return method


def not_overrides(method: _WrappedMethod) -> _WrappedMethod:
    """
    Marks a method as not overriding anything on the parent
    TiePy checking will fail if the decorated method appears on a parent class
    """
    method.__tiepy_not_overrides = True
    return method
