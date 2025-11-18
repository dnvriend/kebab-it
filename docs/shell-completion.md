# Shell Completion for kebab-it

This document describes the shell completion implementation for the kebab-it CLI tool.

## Overview

`kebab-it` supports shell completion for zsh and bash through Click's built-in completion system. This provides tab completion for:
- Command options (`--execute`, `--verbose`, `--force`)
- Short flags (`-e`, `-v`, `-f`)
- File and directory paths

## Implementation

### Built-in Click Support

Click (version 8.0+) includes native shell completion support. The completion is automatically available for any Click application without requiring additional code changes.

### How It Works

Click's completion works through environment variables:
- `_KEBAB_IT_COMPLETE=zsh_source kebab-it` - Generate zsh completion script
- `_KEBAB_IT_COMPLETE=bash_source kebab-it` - Generate bash completion script

The generated scripts are then sourced in the shell configuration file to enable completion.

## Installation Script

The `scripts/install-completion.sh` script automates the installation process:

### Features
- Detects shell type (zsh or bash) automatically
- Adds completion configuration to appropriate shell config file
- Provides uninstall capability
- Creates backups before modifying files
- Validates kebab-it installation before proceeding

### Usage

```bash
# Install completion
./scripts/install-completion.sh

# Uninstall completion
./scripts/install-completion.sh uninstall
```

## Manual Installation

### Zsh

Add to `~/.zshrc`:
```bash
eval "$(_KEBAB_IT_COMPLETE=zsh_source kebab-it)"
```

### Bash

Add to `~/.bashrc` or `~/.bash_profile`:
```bash
eval "$(_KEBAB_IT_COMPLETE=bash_source kebab-it)"
```

### Activation

After adding the completion line, reload your shell:
```bash
source ~/.zshrc   # for zsh
source ~/.bashrc  # for bash
```

## Testing Completion

### Test Script Generation

```bash
# Generate zsh completion script
_KEBAB_IT_COMPLETE=zsh_source kebab-it

# Generate bash completion script
_KEBAB_IT_COMPLETE=bash_source kebab-it
```

### Test in Shell

After installation, test completion by typing:
```bash
kebab-it --[TAB]
```

Should show:
- `--execute` / `-e`
- `--verbose` / `-v`
- `--force` / `-f`
- `--help`
- `--version`

## Supported Shells

- **Zsh**: Full support (tested on macOS)
- **Bash**: Full support (requires Bash 4.4+)
- **Fish**: Supported by Click but not included in install script

## Implementation Details

### File Structure

```
kebab-it/
├── scripts/
│   └── install-completion.sh   # Installation script
├── docs/
│   └── shell-completion.md     # This file
└── README.md                   # User-facing documentation
```

### No Code Changes Required

Click's completion is **automatically enabled** for all Click applications. No modifications to `cli.py` or other source files are needed.

### Environment Variables Used

- `_KEBAB_IT_COMPLETE=zsh_source` - Generate zsh completion
- `_KEBAB_IT_COMPLETE=bash_source` - Generate bash completion
- `_KEBAB_IT_COMPLETE=zsh_complete` - Runtime zsh completion
- `_KEBAB_IT_COMPLETE=bash_complete` - Runtime bash completion

## Troubleshooting

### Completion Not Working

1. Verify kebab-it is installed:
   ```bash
   which kebab-it
   ```

2. Check shell config file was modified:
   ```bash
   grep "kebab-it completion" ~/.zshrc   # or ~/.bashrc
   ```

3. Reload shell configuration:
   ```bash
   source ~/.zshrc  # or ~/.bashrc
   ```

### Installation Script Fails

- Ensure kebab-it is installed globally: `uv tool install .`
- Check shell type is supported: `echo $SHELL`
- Verify shell config file exists and is writable

## References

- [Click Documentation - Shell Completion](https://click.palletsprojects.com/en/8.1.x/shell-completion/)
- [Click GitHub Repository](https://github.com/pallets/click)

## Future Enhancements

Potential improvements:
- Support for Fish shell in installation script
- Completion for glob patterns
- Custom completion for file matching
- Interactive completion preview
