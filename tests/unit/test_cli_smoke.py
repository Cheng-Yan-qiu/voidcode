"""Smoke tests for the CLI entrypoints."""

from __future__ import annotations

import subprocess
import sys


def test_python_module_help_works() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "voidcode", "--help"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert "usage:" in result.stdout.lower()


def test_console_script_help_works() -> None:
    result = subprocess.run(
        ["voidcode", "--help"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert "usage:" in result.stdout.lower()
