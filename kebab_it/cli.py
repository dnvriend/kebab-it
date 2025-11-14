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
    The tool converts filenames to lowercase with hyphens, preserving file extensions.

    Conversion examples:
      - "My File Name.md" → "my-file-name.md"
      - "Study_Notes_2024.md" → "study-notes-2024.md"
      - "MO - 1.2 - Strategie.md" → "mo-1-2-strategie.md"

    Examples:

    \b
        # Preview changes for all markdown files in current directory
        kebab-it "*.md"

    \b
        # Actually rename markdown files (requires --execute flag)
        kebab-it "*.md" --execute

    \b
        # Preview with detailed output showing each rename operation
        kebab-it "*.md" --verbose

    \b
        # Recursively rename all Python files in subdirectories
        kebab-it "**/*.py" --execute

    \b
        # Multiple patterns can be provided
        kebab-it "*.md" "*.txt" --execute

    \b
        # Rename files in home directory
        kebab-it "~/Documents/*.txt" --execute

    \b
        # Rename and overwrite if target file already exists
        kebab-it "*.txt" --execute --force

    \b
        # Complex: rename multiple file types with verbose output
        kebab-it "**/*.md" "**/*.txt" \\
            --execute \\
            --verbose \\
            --force

    \b
    Output Format:
        The tool displays a summary with statistics:

        Summary:
          Total files matched: 42
          Successfully renamed: 38
          Skipped (no change): 2
          Skipped (exists): 1
          Errors: 1

        Exit codes:
        - 0: Success (all files processed without errors)
        - 1: Error (no files found or errors during renaming)
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
