import sys
import logging
import re
import importlib.util
import runpy
from typing import List
from pathlib import Path

import click

from tiepy import __version__
from tiepy.check import Issue
from tiepy.check.overrides import OverridesChecker


_s3_path_re = re.compile(r"s3://(.+?)/(.+)?$")


@click.command()
@click.argument('target', type=click.Path(exists=True))
@click.option('-v', '--verbose', is_flag=True)
def tiepy(
    target: str,
    verbose: bool,
):
    target = Path(target).absolute()
    click.echo(click.style("TiePy", fg="cyan", bold=True) + f" {__version__} checking {target}")

    if target.is_file():
        paths = [target]
    else:
        paths = target.rglob("*.py")

    issues: List[Issue] = []

    # Overrides
    overrides_checker = OverridesChecker()
    for path in paths:
        if verbose:
            click.echo(f"Checking {path}")
        module = runpy.run_path(str(path))
        issues.extend(overrides_checker.check_module(module))

    # Results
    issues.sort(key=lambda x: (x.filename, x.line_no))
    for issue in issues:
        click.echo(issue.to_print_str())
    click.echo(f"Found {len(issues)} issues")


def main():
    logging.basicConfig(level=logging.INFO)
    tiepy(sys.argv[1:])


if __name__ == "__main__":
    main()
