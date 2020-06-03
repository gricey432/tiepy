from types import ModuleType, FunctionType
from typing import List, Dict, Any
import inspect

from tiepy.check import Issue, Checker
from tiepy.overrides import overrides, final


class OverridesChecker(Checker):
    """
    Checks for issues relating to `overrides` and `final` decorators
    """

    @overrides
    def check_module(self, module: Dict[str, Any]) -> List[Issue]:
        issues: List[Issue] = []
        for module_member_name, module_member in module.items():
            if inspect.isclass(module_member):
                for class_member_name, class_member in inspect.getmembers(module_member):
                    if inspect.isfunction(class_member):
                        issues.extend(self.check_function(module_member, class_member, class_member_name))
        return issues

    def check_function(self, cls: type, function: FunctionType, name: str) -> List[Issue]:
        decorated_overrides = getattr(function, "__tiepy_overrides", False)
        decorated_not_overrides = getattr(function, "__tiepy_not_overrides", False)
        _, lineno = inspect.getsourcelines(function)
        issues: List[Issue] = []

        if decorated_overrides and decorated_not_overrides:
            issues.append(Issue(
                filename=inspect.getfile(function),
                line_no=lineno,
                message="@overrides and @not_overrides can't both be on the same function",
            ))

        found_overridden_parent = False
        for parent_cls in cls.mro()[1:]:  # Skip current class
            if hasattr(parent_cls, name):
                found_overridden_parent = True
                if decorated_not_overrides:
                    issues.append(Issue(
                        filename=inspect.getfile(function),
                        line_no=lineno,
                        message=f"@no_overrides function overrides parent {parent_cls.__name__}",
                    ))
                if getattr(getattr(parent_cls, name), "__tiepy_final", False):
                    issues.append(Issue(
                        filename=inspect.getfile(function),
                        line_no=lineno,
                        message=f"@final function overrides parent {parent_cls.__name__}",
                    ))
        if decorated_overrides and not found_overridden_parent:
            issues.append(Issue(
                filename=inspect.getfile(function),
                line_no=lineno,
                message=f"@overrides function doesn't override parent",
            ))

        return issues
