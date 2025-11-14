"""Statistics tracking for kebab-it.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

from dataclasses import dataclass, field


@dataclass
class RenameStats:
    """Track statistics for file renaming operations."""

    total_matched: int = 0
    renamed: int = 0
    skipped_no_change: int = 0
    skipped_exists: int = 0
    errors: int = 0
    error_messages: list[str] = field(default_factory=list)

    def add_renamed(self) -> None:
        """Increment the count of successfully renamed files."""
        self.renamed += 1

    def add_skipped_no_change(self) -> None:
        """Increment the count of files that didn't need renaming."""
        self.skipped_no_change += 1

    def add_skipped_exists(self) -> None:
        """Increment the count of files skipped because target exists."""
        self.skipped_exists += 1

    def add_error(self, message: str) -> None:
        """Add an error to the statistics.

        Args:
            message: Error message to record
        """
        self.errors += 1
        self.error_messages.append(message)

    def print_summary(self) -> None:
        """Print a summary of the rename operations."""
        print("\nSummary:")
        print(f"  Total files matched:    {self.total_matched}")
        print(f"  Successfully renamed:   {self.renamed}")
        print(f"  Skipped (no change):    {self.skipped_no_change}")
        print(f"  Skipped (exists):       {self.skipped_exists}")
        print(f"  Errors:                 {self.errors}")

        if self.error_messages:
            print("\nErrors:")
            for msg in self.error_messages:
                print(f"  - {msg}")
