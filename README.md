<p align="center">
  <img src=".github/assets/logo.png" alt="kebab-it logo" width="200">
</p>

# kebab-it

[![Python Version](https://img.shields.io/badge/python-3.14+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Type checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg)](https://github.com/python/mypy)
[![AI Generated](https://img.shields.io/badge/AI-Generated-blueviolet.svg)](https://www.anthropic.com/claude)
[![Claude Sonnet 4.5](https://img.shields.io/badge/Model-Claude_Sonnet_4.5-blue)](https://www.anthropic.com/claude)
[![Built with Claude Code](https://img.shields.io/badge/Built_with-Claude_Code-5A67D8.svg)](https://www.anthropic.com/claude/code)

A CLI tool to rename files to kebab-case using glob patterns.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Development](#development)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## About

`kebab-it` is a command-line utility that converts filenames to kebab-case format (lowercase with hyphens). It uses glob patterns to select files and provides comprehensive statistics on renaming operations.

**What is kebab-case?**

Kebab-case is a naming convention where:
- All letters are lowercase
- Words are separated by hyphens (`-`)
- No spaces, underscores, or special characters

Example: `My File Name.md` → `my-file-name.md`

## Features

- ✅ Convert filenames to kebab-case (lowercase with hyphens)
- ✅ Support for glob patterns (e.g., `**/*.md`, `*.py`)
- ✅ Glob expansion including `~`, variables, and relative paths
- ✅ Safe by default (preview mode), requires --execute to rename
- ✅ Statistics reporting (files renamed, skipped, errors)
- ✅ Safe renaming (skips if target exists)
- ✅ Type-safe with mypy strict mode
- ✅ Linted with ruff

## Installation

### Prerequisites

- Python 3.14 or higher
- [uv](https://github.com/astral-sh/uv) package manager

### Install from source

```bash
# Clone the repository
git clone https://github.com/yourusername/kebab-it.git
cd kebab-it

# Install globally with uv
uv tool install .
```

### Install with mise (recommended for development)

```bash
cd kebab-it
mise trust
mise install
uv sync
uv tool install .
```

### Verify installation

```bash
kebab-it --version
```

### Shell Completion

`kebab-it` supports shell completion for zsh and bash, making it easier to use the CLI with tab completion.

#### Quick Install (Recommended)

```bash
# From the project directory
./scripts/install-completion.sh
```

The script will:
- Detect your shell (zsh or bash)
- Add the completion configuration to your shell config file
- Provide instructions to activate it

#### Manual Installation

**For zsh** (add to `~/.zshrc`):
```bash
eval "$(_KEBAB_IT_COMPLETE=zsh_source kebab-it)"
```

**For bash** (add to `~/.bashrc`):
```bash
eval "$(_KEBAB_IT_COMPLETE=bash_source kebab-it)"
```

After adding the line, reload your shell:
```bash
source ~/.zshrc  # for zsh
source ~/.bashrc # for bash
```

#### Uninstall Completion

```bash
./scripts/install-completion.sh uninstall
```

## Usage

**IMPORTANT:** By default, `kebab-it` runs in **preview mode** (dry-run). It will show you what would be renamed without actually renaming files. Use `--execute` / `-e` to actually rename files.

### Basic Usage

```bash
# Preview changes (default behavior)
kebab-it "*.md"

# Actually rename files
kebab-it "*.md" --execute

# Preview all Python files recursively
kebab-it "**/*.py"

# Show help
kebab-it --help
```

### Options

```
Options:
  --execute, -e     Actually rename files (default is preview/dry-run mode)
  --verbose, -v     Show detailed output
  --force, -f       Overwrite existing files (only with --execute)
  --version         Show version and exit
  --help            Show help message and exit
```

### Advanced Usage

```bash
# Preview with verbose output
kebab-it "*.txt" --verbose

# Execute rename with force overwrite
kebab-it "*.md" --execute --force

# Multiple patterns with execute
kebab-it "*.md" "*.txt" --execute

# Preview recursively
kebab-it "**/*" --verbose
```

## Examples

### Before and After

```bash
# Example 1: Simple filename
Before: "My File Name.md"
After:  "my-file-name.md"

# Example 2: Underscores
Before: "Study_Notes_2024.md"
After:  "study-notes-2024.md"

# Example 3: Mixed case with special characters
Before: "MO - 1.2 - Strategie.md"
After:  "mo-1.2-strategie.md"
```

### Real-world Usage

```bash
# Rename all markdown files in a directory
cd ~/Documents/notes
kebab-it "*.md"

# Preview changes before renaming
kebab-it --dry-run "**/*.md"

# Rename all files in subdirectories
kebab-it "**/*.*"
```

## Development

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/yourusername/kebab-it.git
cd kebab-it

# Install dependencies
make install

# Show available commands
make help
```

### Available Make Commands

```bash
make install          # Install dependencies
make format           # Format code with ruff
make lint             # Run linting with ruff
make typecheck        # Run type checking with mypy
make test             # Run tests with pytest
make security         # Run security checks (bandit, pip-audit, trufflehog)
make check            # Run all checks (lint, typecheck, test)
make pipeline         # Run full pipeline (format, lint, typecheck, test, security, build, install-global)
make build            # Build package
make run ARGS="..."   # Run kebab-it locally
make clean            # Remove build artifacts
```

### Project Structure

```
kebab-it/
├── kebab_it/           # Main package
│   ├── __init__.py
│   ├── cli.py          # CLI entry point
│   ├── renamer.py      # Core renaming logic
│   ├── stats.py        # Statistics tracking
│   └── utils.py        # Utility functions
├── tests/              # Test suite
│   ├── __init__.py
│   ├── test_cli.py
│   ├── test_renamer.py
│   └── test_utils.py
├── pyproject.toml      # Project configuration
├── Makefile            # Development commands
├── README.md           # This file
├── LICENSE             # MIT License
└── CLAUDE.md           # Development documentation
```

## Security

The project includes comprehensive security scanning:

```bash
# Run all security checks
make security
```

### Security Tools

1. **Bandit** - Python security linter
   - Scans for common security issues in Python code
   - Note: Limited Python 3.14 AST compatibility

2. **pip-audit** - Dependency vulnerability scanner
   - Checks for known security vulnerabilities in dependencies
   - Uses the PyPI Advisory Database

3. **TruffleHog** - Secrets scanner
   - Scans for accidentally committed secrets and credentials
   - Install with: `brew install trufflehog` (macOS)

### Installing TruffleHog

```bash
# macOS
brew install trufflehog

# Linux/Windows with Go
go install github.com/trufflesecurity/trufflehog/v3@latest
```

## Testing

Run the test suite:

```bash
# Run all tests
make test

# Run tests with verbose output
uv run pytest tests/ -v

# Run specific test file
uv run pytest tests/test_utils.py

# Run with coverage
uv run pytest tests/ --cov=kebab_it
```

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run the full pipeline (`make pipeline`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines
- Use type hints for all functions
- Write docstrings for public functions
- Format code with `ruff`
- Pass all linting and type checks

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

The MIT License is one of the most permissive open source licenses. You are free to:

- Use commercially
- Modify
- Distribute
- Use privately
- Sublicense

The only requirement is to include the original copyright and license notice.

## Author

**Dennis Vriend**

- GitHub: [@dennisvriend](https://github.com/dennisvriend)

## Acknowledgments

- Built with [Click](https://click.palletsprojects.com/) for CLI framework
- Powered by [python-slugify](https://github.com/un33k/python-slugify) for robust kebab-case conversion
- Developed with [uv](https://github.com/astral-sh/uv) for fast Python tooling

---

**Generated with AI**

This project was generated using [Claude Code](https://www.anthropic.com/claude/code), an AI-powered development tool by [Anthropic](https://www.anthropic.com/). Claude Code assisted in creating the project structure, implementation, tests, documentation, and development tooling.

Made with ❤️ using Python 3.14
