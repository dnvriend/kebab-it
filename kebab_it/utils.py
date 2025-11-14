"""Utility functions for kebab-it.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

import os


def expand_path(path: str) -> str:
    """Expand a path with tilde and environment variables.

    Args:
        path: Path to expand

    Returns:
        str: Expanded path
    """
    return os.path.expanduser(os.path.expandvars(path))
