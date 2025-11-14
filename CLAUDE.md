# kebab-it - Project Specification

## Goal

Create a CLI tool that renames files to kebab-case format using glob patterns. The tool should be simple, safe, and provide clear feedback on operations performed.

## What is kebab-it?

`kebab-it` is a command-line utility that converts filenames to kebab-case (lowercase with hyphens instead of spaces/underscores). It uses glob patterns to select files and provides statistics on the renaming operations.

## Technical Requirements

### Runtime

- Python 3.14+
- Installable globally with mise
- Cross-platform (macOS, Linux, Windows)

### Dependencies

- `click` - CLI framework
- `python-slugify` - Robust kebab-case conversion

### Development Dependencies

- `ruff` - Linting and formatting
- `mypy` - Type checking
- `pytest` - Testing framework

## CLI Arguments

```bash
kebab-it [OPTIONS] PATTERN [PATTERN...]
```

### Positional Arguments

- `PATTERN` - One or more glob patterns (e.g., `*.md`, `**/*.py`)
  - Must support glob expansion (`~`, variables, relative paths)
  - Multiple patterns can be provided

### Options

- `--execute` / `-e` - Actually rename files (default is preview/dry-run mode)
- `--verbose` / `-v` - Show detailed output
- `--force` / `-f` - Overwrite existing files (only with --execute)
- `--help` / `-h` - Show help message
- `--version` - Show version

**Default Behavior:** The tool runs in preview mode (dry-run) by default. Files are NOT renamed unless `--execute` is specified.

## Behavior

### File Renaming Logic

1. Accept glob pattern(s) from command line
2. Expand glob patterns (handle `~`, variables, relative paths)
3. For each matched file:
   - Extract filename (without path)
   - Convert to kebab-case using `python-slugify`
   - Check if target filename already exists
   - Rename file (only if `--execute` is specified, otherwise preview only)
   - Track statistics

### Kebab-case Conversion

- Convert all letters to lowercase
- Replace spaces with hyphens (`-`)
- Replace underscores with hyphens (`-`)
- Remove or replace special characters
- Collapse multiple consecutive hyphens into single hyphen
- Preserve file extensions

Examples:
- `My File Name.md` → `my-file-name.md`
- `Study_Notes_2024.md` → `study-notes-2024.md`
- `MO - 1.2 - Strategie.md` → `mo-1-2-strategie.md`

### Safety Features

- **Safe by default**: Preview mode (dry-run) is the default behavior
- Requires explicit `--execute` flag to actually rename files
- Skip files if target already exists (unless `--force`)
- Warn user about conflicts
- Never rename if source and target are identical

### Statistics Reporting

Display summary at the end:
```
Summary:
  Total files matched: 42
  Successfully renamed: 38
  Skipped (no change): 2
  Skipped (exists): 1
  Errors: 1
```

### Error Handling

- Permission errors - report and continue
- File not found - report and continue
- Invalid glob pattern - exit with error
- Target exists - skip and report (unless `--force`)

## Project Structure

```
kebab-it/
├── kebab_it/
│   ├── __init__.py
│   ├── cli.py           # Click CLI entry point
│   ├── renamer.py       # Core renaming logic
│   └── stats.py         # Statistics tracking
├── tests/
│   ├── __init__.py
│   ├── test_cli.py
│   ├── test_renamer.py
│   └── test_stats.py
├── pyproject.toml       # Project configuration
├── README.md            # User documentation
├── CLAUDE.md            # This file
├── Makefile             # Development commands
└── .gitignore
```

## Code Style

- Type hints for all functions
- Docstrings for all public functions
- Use `from typing import List` (not `list[str]` for compatibility)
- Follow PEP 8 via ruff
- 100 character line length
- Strict mypy checking

## Development Workflow

```bash
# Install dependencies
make install

# Run linting
make lint

# Format code
make format

# Type check
make typecheck

# Run tests
make test

# Run security checks
make security

# Run all checks
make check

# Run full pipeline (format, lint, typecheck, test, security, build, install)
make pipeline
```

## Security

The project includes three security scanning tools:

1. **Bandit** - Python security linter (note: Python 3.14 AST compatibility limited)
2. **pip-audit** - Dependency vulnerability scanner
3. **TruffleHog** - Secrets scanner (requires separate installation)

Run all security checks:
```bash
make security
```

## Installation Methods

### Global installation with mise

```bash
cd /path/to/kebab-it
mise use -g python@3.14
uv sync
uv tool install .
```

After installation, `kebab-it` command is available globally.

### Local development

```bash
uv sync
uv run kebab-it [args]
```

## Future Enhancements (Out of Scope for v0.1.0)

- Support for other case conversions (snake-case, camelCase, PascalCase)
- Undo functionality
- Interactive mode
- Configuration file support
- Exclude patterns
- Recursive directory handling with depth control
- Backup before rename
