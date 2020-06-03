import pytest
import runpy
import os

from tiepy.check.overrides import OverridesChecker


def test_overrides():
    module = runpy.run_path(os.path.join(os.path.dirname(__file__), "_testable_modules", "overrides_1.py"))
    issues = OverridesChecker().check_module(module)
    assert len(issues) == 0
