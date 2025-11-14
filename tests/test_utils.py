"""Tests for kebab_it.utils module.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

import os

from kebab_it.utils import expand_path


def test_expand_path_simple() -> None:
    """Test simple path expansion."""
    result = expand_path("/path/to/file")
    assert result == "/path/to/file"


def test_expand_path_with_tilde() -> None:
    """Test path expansion with tilde."""
    result = expand_path("~/file.txt")
    assert result.startswith(os.path.expanduser("~"))
    assert result.endswith("file.txt")


def test_expand_path_with_env_var() -> None:
    """Test path expansion with environment variable."""
    os.environ["TEST_VAR"] = "/test/path"
    result = expand_path("$TEST_VAR/file.txt")
    assert result == "/test/path/file.txt"
