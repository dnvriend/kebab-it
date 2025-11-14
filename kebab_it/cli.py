"""CLI entry point for kebab-it.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

import glob
import os
import sys
from pathlib import Path

import click

from kebab_it.renamer import rename_files


def expand_glob_pattern(pattern: str) -> list[Path]:
    """Expand a glob pattern to a list of file paths.

    Handles:
    - Tilde expansion (~)
    - Environment variable expansion
    - Relative paths
    - Recursive globs (**)

    Args:
        pattern: Glob pattern to expand

    Returns:
        list[Path]: List of matching file paths
    """
    # Expand tilde and environment variables
    expanded_pattern = os.path.expanduser(os.path.expandvars(pattern))

    # Use glob to find matching files
    matches = glob.glob(expanded_pattern, recursive=True)

    # Convert to Path objects and filter to only files (not directories)
    file_paths = [Path(match) for match in matches if os.path.isfile(match)]

    return file_paths


@click.command()
@click.argument("patterns", nargs=-1, required=True, metavar="PATTERN...")
@click.option(
    "--execute",
    "-e",
    is_flag=True,
    help="Actually rename files (default is dry-run/preview mode)",
)
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    help="Show detailed output",
)
@click.option(
    "--force",
    "-f",
    is_flag=True,
    help="Overwrite existing files (only with --execute)",
)
@click.version_option(version="0.1.0")
def main(patterns: tuple[str, ...], execute: bool, verbose: bool, force: bool) -> None:
    """Rename files to kebab-case using glob patterns.

    By default, runs in PREVIEW MODE (dry-run). Use --execute to actually rename files.

    PATTERN can be any glob pattern like:
      - *.md (all markdown files in current directory)
      - **/*.py (all Python files recursively)
      - ~/Documents/*.txt (files in home directory)

    Examples:
      kebab-it "*.md"                    # Preview changes
      kebab-it "*.md" --execute          # Actually rename
      kebab-it "**/*.py" --verbose       # Preview with details
      kebab-it "*.txt" --execute --force # Rename and overwrite
    """
    # Expand all glob patterns
    all_files: list[Path] = []
    for pattern in patterns:
        matching_files = expand_glob_pattern(pattern)
        all_files.extend(matching_files)

    # Remove duplicates while preserving order
    seen = set()
    unique_files = []
    for file_path in all_files:
        if file_path not in seen:
            seen.add(file_path)
            unique_files.append(file_path)

    # Check if any files were found
    if not unique_files:
        click.echo("No files matched the given patterns.", err=True)
        sys.exit(1)

    # Determine if this is a dry-run (default) or actual execution
    dry_run = not execute

    # Rename files
    stats = rename_files(unique_files, dry_run, force, verbose)

    # Print summary
    stats.print_summary()

    # Exit with error code if there were errors
    if stats.errors > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
