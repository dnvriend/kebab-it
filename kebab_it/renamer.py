"""Core file renaming logic for kebab-it.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

import logging
import os
from pathlib import Path

from slugify import slugify

from kebab_it.stats import RenameStats

logger = logging.getLogger(__name__)


def to_kebab_case(filename: str) -> str:
    """Convert a filename to kebab-case.

    Args:
        filename: The filename to convert (with extension)

    Returns:
        str: The kebab-case filename with preserved extension
    """
    # Split filename and extension
    name, ext = os.path.splitext(filename)

    # Convert to kebab-case using slugify
    kebab_name = slugify(name, separator="-")

    # Return with extension
    return f"{kebab_name}{ext}"


def rename_file(
    file_path: Path, dry_run: bool, force: bool, verbose: bool | int, stats: RenameStats
) -> None:
    """Rename a single file to kebab-case.

    Args:
        file_path: Path to the file to rename
        dry_run: If True, don't actually rename, just show what would happen
        force: If True, overwrite existing files
        verbose: Verbosity level (bool for legacy, int for count-based)
        stats: Statistics tracker
    """
    # Get directory and filename
    directory = file_path.parent
    original_name = file_path.name

    # Convert to kebab-case
    new_name = to_kebab_case(original_name)

    # Check if name is already in kebab-case
    if original_name == new_name:
        logger.debug(f"Skipping {file_path} (already kebab-case)")
        stats.add_skipped_no_change()
        return

    # Create new path
    new_path = directory / new_name

    # Check if target exists
    if new_path.exists() and not force:
        logger.debug(f"Skipping {file_path} -> {new_name} (target exists)")
        stats.add_skipped_exists()
        return

    # Perform rename (or simulate)
    if dry_run:
        logger.info(f"Would rename: {file_path} -> {new_name}")
        stats.add_renamed()
    else:
        try:
            logger.debug(f"Renaming: {file_path} -> {new_name}")
            file_path.rename(new_path)
            logger.info(f"Renamed: {file_path} -> {new_name}")
            stats.add_renamed()
        except Exception as e:
            error_msg = f"Failed to rename {file_path}: {e}"
            logger.error(error_msg)
            logger.debug("Full traceback:", exc_info=True)
            stats.add_error(error_msg)


def rename_files(
    file_paths: list[Path], dry_run: bool, force: bool, verbose: bool | int
) -> RenameStats:
    """Rename multiple files to kebab-case.

    Args:
        file_paths: List of file paths to rename
        dry_run: If True, don't actually rename, just show what would happen
        force: If True, overwrite existing files
        verbose: Verbosity level (bool for legacy, int for count-based)

    Returns:
        RenameStats: Statistics about the rename operations
    """
    stats = RenameStats()
    stats.total_matched = len(file_paths)

    if dry_run:
        logger.warning("DRY RUN MODE - No files will be renamed")

    logger.info(f"Processing {stats.total_matched} file(s)")
    logger.debug(f"Dry run: {dry_run}, Force: {force}")

    for file_path in file_paths:
        rename_file(file_path, dry_run, force, verbose, stats)

    return stats
