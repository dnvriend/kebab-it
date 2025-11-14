"""Tests for kebab_it.renamer module.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

from kebab_it.renamer import to_kebab_case


def test_to_kebab_case_simple() -> None:
    """Test basic kebab-case conversion."""
    assert to_kebab_case("My File.txt") == "my-file.txt"
    assert to_kebab_case("Hello World.md") == "hello-world.md"


def test_to_kebab_case_underscores() -> None:
    """Test conversion of underscores to hyphens."""
    assert to_kebab_case("my_file_name.py") == "my-file-name.py"
    assert to_kebab_case("test_utils.py") == "test-utils.py"


def test_to_kebab_case_mixed() -> None:
    """Test conversion with mixed case and special characters."""
    assert to_kebab_case("MO - 1.2 - Strategie.md") == "mo-1-2-strategie.md"
    assert to_kebab_case("Study Notes 2024.txt") == "study-notes-2024.txt"


def test_to_kebab_case_already_kebab() -> None:
    """Test that already kebab-case names are preserved."""
    assert to_kebab_case("my-file.txt") == "my-file.txt"
    assert to_kebab_case("test-utils.py") == "test-utils.py"


def test_to_kebab_case_extension_preserved() -> None:
    """Test that file extensions are preserved."""
    assert to_kebab_case("MyFile.TXT") == "myfile.TXT"
    assert to_kebab_case("Test File.py") == "test-file.py"
    assert to_kebab_case("document.PDF") == "document.PDF"


def test_to_kebab_case_no_extension() -> None:
    """Test conversion of files without extensions."""
    assert to_kebab_case("My File") == "my-file"
    assert to_kebab_case("README") == "readme"


def test_to_kebab_case_multiple_spaces() -> None:
    """Test conversion with multiple consecutive spaces."""
    assert to_kebab_case("my  file  name.txt") == "my-file-name.txt"


def test_to_kebab_case_special_characters() -> None:
    """Test handling of special characters."""
    assert to_kebab_case("file@name!.txt") == "file-name.txt"
    assert to_kebab_case("my (file).md") == "my-file.md"
