#!/usr/bin/env bash
# Shell completion installation script for kebab-it
#
# This script installs shell completion for kebab-it in zsh or bash.
# Click provides native completion support that we leverage here.
#
# Note: This code was generated with assistance from AI coding tools
# and has been reviewed and tested by a human.

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Detect shell
detect_shell() {
    if [ -n "$ZSH_VERSION" ]; then
        echo "zsh"
    elif [ -n "$BASH_VERSION" ]; then
        echo "bash"
    else
        echo "unknown"
    fi
}

# Get shell config file
get_shell_config() {
    local shell_type="$1"
    case "$shell_type" in
        zsh)
            echo "$HOME/.zshrc"
            ;;
        bash)
            # Try bashrc first, then bash_profile
            if [ -f "$HOME/.bashrc" ]; then
                echo "$HOME/.bashrc"
            else
                echo "$HOME/.bash_profile"
            fi
            ;;
        *)
            echo ""
            ;;
    esac
}

# Install completion
install_completion() {
    local shell_type="$1"
    local config_file="$2"
    local completion_marker="# kebab-it completion"

    # Check if already installed
    if grep -q "$completion_marker" "$config_file" 2>/dev/null; then
        echo -e "${YELLOW}Shell completion for kebab-it is already installed in $config_file${NC}"
        return 0
    fi

    # Determine completion command based on shell
    local completion_cmd
    case "$shell_type" in
        zsh)
            completion_cmd='eval "$(_KEBAB_IT_COMPLETE=zsh_source kebab-it)"'
            ;;
        bash)
            completion_cmd='eval "$(_KEBAB_IT_COMPLETE=bash_source kebab-it)"'
            ;;
        *)
            echo -e "${RED}Unsupported shell: $shell_type${NC}"
            return 1
            ;;
    esac

    # Add completion to config file
    echo "" >> "$config_file"
    echo "$completion_marker" >> "$config_file"
    echo "$completion_cmd" >> "$config_file"

    echo -e "${GREEN}Shell completion installed successfully!${NC}"
    echo -e "Completion added to: ${GREEN}$config_file${NC}"
    echo ""
    echo "To enable completion in your current shell, run:"
    echo -e "${YELLOW}  source $config_file${NC}"
    echo ""
    echo "Or start a new shell session."
}

# Uninstall completion
uninstall_completion() {
    local config_file="$1"
    local completion_marker="# kebab-it completion"

    if ! grep -q "$completion_marker" "$config_file" 2>/dev/null; then
        echo -e "${YELLOW}Shell completion is not installed in $config_file${NC}"
        return 0
    fi

    # Create backup
    cp "$config_file" "${config_file}.backup"

    # Remove completion lines
    sed -i.tmp "/$completion_marker/,+1d" "$config_file"
    rm -f "${config_file}.tmp"

    echo -e "${GREEN}Shell completion uninstalled successfully!${NC}"
    echo -e "Backup saved to: ${GREEN}${config_file}.backup${NC}"
    echo ""
    echo "To apply changes, run:"
    echo -e "${YELLOW}  source $config_file${NC}"
}

# Main function
main() {
    local action="${1:-install}"

    echo "kebab-it Shell Completion Installer"
    echo "===================================="
    echo ""

    # Detect shell
    local shell_type
    shell_type=$(detect_shell)

    if [ "$shell_type" = "unknown" ]; then
        echo -e "${RED}Error: Unable to detect shell type${NC}"
        echo "This script supports bash and zsh."
        exit 1
    fi

    echo "Detected shell: $shell_type"

    # Get config file
    local config_file
    config_file=$(get_shell_config "$shell_type")

    if [ -z "$config_file" ]; then
        echo -e "${RED}Error: Unable to determine shell config file${NC}"
        exit 1
    fi

    echo "Config file: $config_file"
    echo ""

    # Verify kebab-it is installed
    if ! command -v kebab-it &> /dev/null; then
        echo -e "${RED}Error: kebab-it command not found${NC}"
        echo "Please install kebab-it first:"
        echo "  cd /path/to/kebab-it"
        echo "  uv tool install ."
        exit 1
    fi

    # Perform action
    case "$action" in
        install)
            install_completion "$shell_type" "$config_file"
            ;;
        uninstall)
            uninstall_completion "$config_file"
            ;;
        *)
            echo -e "${RED}Error: Unknown action '$action'${NC}"
            echo "Usage: $0 [install|uninstall]"
            exit 1
            ;;
    esac
}

# Run main with arguments
main "$@"
