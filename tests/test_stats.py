"""Tests for kebab_it.stats module.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

from kebab_it.stats import RenameStats


def test_rename_stats_initialization() -> None:
    """Test that RenameStats initializes with zero counts."""
    stats = RenameStats()
    assert stats.total_matched == 0
    assert stats.renamed == 0
    assert stats.skipped_no_change == 0
    assert stats.skipped_exists == 0
    assert stats.errors == 0
    assert stats.error_messages == []


def test_rename_stats_add_renamed() -> None:
    """Test adding a renamed file."""
    stats = RenameStats()
    stats.add_renamed()
    assert stats.renamed == 1
    stats.add_renamed()
    assert stats.renamed == 2


def test_rename_stats_add_skipped_no_change() -> None:
    """Test adding a skipped file (no change needed)."""
    stats = RenameStats()
    stats.add_skipped_no_change()
    assert stats.skipped_no_change == 1


def test_rename_stats_add_skipped_exists() -> None:
    """Test adding a skipped file (target exists)."""
    stats = RenameStats()
    stats.add_skipped_exists()
    assert stats.skipped_exists == 1


def test_rename_stats_add_error() -> None:
    """Test adding an error."""
    stats = RenameStats()
    stats.add_error("Test error message")
    assert stats.errors == 1
    assert len(stats.error_messages) == 1
    assert stats.error_messages[0] == "Test error message"


def test_rename_stats_multiple_operations() -> None:
    """Test tracking multiple operations."""
    stats = RenameStats()
    stats.total_matched = 10
    stats.add_renamed()
    stats.add_renamed()
    stats.add_renamed()
    stats.add_skipped_no_change()
    stats.add_skipped_exists()
    stats.add_error("Error 1")
    stats.add_error("Error 2")

    assert stats.total_matched == 10
    assert stats.renamed == 3
    assert stats.skipped_no_change == 1
    assert stats.skipped_exists == 1
    assert stats.errors == 2
    assert len(stats.error_messages) == 2
