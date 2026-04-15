#!/usr/bin/env bash

# ============================================
# Install/Uninstall autocommit cron job
# Fedora 43 compatible (systemd timer)
# ============================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AUTOCOMMIT_SCRIPT="${SCRIPT_DIR}/autocommit.sh"
SERVICE_NAME="bc-fastapi-autocommit"
TIMER_DIR="$HOME/.config/systemd/user"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

print_header() {
    echo -e "${BLUE}"
    echo "╔══════════════════════════════════════════╗"
    echo "║   BC-FastAPI Auto-commit Installer       ║"
    echo "║   Fedora 43 - systemd timer              ║"
    echo "╚══════════════════════════════════════════╝"
    echo -e "${NC}"
}

# Create systemd service file
create_service() {
    mkdir -p "$TIMER_DIR"
    
    cat > "${TIMER_DIR}/${SERVICE_NAME}.service" << EOF
[Unit]
Description=BC-FastAPI Bootcamp Auto-commit Service
After=network.target

[Service]
Type=oneshot
ExecStart=${AUTOCOMMIT_SCRIPT}
WorkingDirectory=${SCRIPT_DIR}/..
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=default.target
EOF

    echo -e "${GREEN}✓${NC} Service file created"
}

# Create systemd timer file
create_timer() {
    local interval="$1"
    
    cat > "${TIMER_DIR}/${SERVICE_NAME}.timer" << EOF
[Unit]
Description=BC-FastAPI Bootcamp Auto-commit Timer
Requires=${SERVICE_NAME}.service

[Timer]
OnBootSec=5min
OnUnitActiveSec=${interval}
Persistent=true
RandomizedDelaySec=60

[Install]
WantedBy=timers.target
EOF

    echo -e "${GREEN}✓${NC} Timer file created (interval: ${interval})"
}

# Install the timer
install_timer() {
    local interval="${1:-30min}"
    
    echo -e "${BLUE}Installing auto-commit timer...${NC}"
    echo ""
    
    # Make script executable
    chmod +x "$AUTOCOMMIT_SCRIPT"
    echo -e "${GREEN}✓${NC} Made autocommit.sh executable"
    
    # Create service and timer
    create_service
    create_timer "$interval"
    
    # Reload systemd
    systemctl --user daemon-reload
    echo -e "${GREEN}✓${NC} Systemd daemon reloaded"
    
    # Enable and start timer
    systemctl --user enable "${SERVICE_NAME}.timer"
    systemctl --user start "${SERVICE_NAME}.timer"
    echo -e "${GREEN}✓${NC} Timer enabled and started"
    
    echo ""
    echo -e "${GREEN}Installation complete!${NC}"
    echo ""
    echo "Timer will run every ${interval}"
    echo ""
    echo "Useful commands:"
    echo "  Check status:  systemctl --user status ${SERVICE_NAME}.timer"
    echo "  View logs:     journalctl --user -u ${SERVICE_NAME}.service"
    echo "  Run manually:  systemctl --user start ${SERVICE_NAME}.service"
    echo "  Stop timer:    systemctl --user stop ${SERVICE_NAME}.timer"
    echo "  Disable:       systemctl --user disable ${SERVICE_NAME}.timer"
}

# Uninstall the timer
uninstall_timer() {
    echo -e "${YELLOW}Uninstalling auto-commit timer...${NC}"
    echo ""
    
    # Stop and disable timer
    systemctl --user stop "${SERVICE_NAME}.timer" 2>/dev/null || true
    systemctl --user disable "${SERVICE_NAME}.timer" 2>/dev/null || true
    echo -e "${GREEN}✓${NC} Timer stopped and disabled"
    
    # Remove files
    rm -f "${TIMER_DIR}/${SERVICE_NAME}.service"
    rm -f "${TIMER_DIR}/${SERVICE_NAME}.timer"
    echo -e "${GREEN}✓${NC} Service files removed"
    
    # Reload systemd
    systemctl --user daemon-reload
    echo -e "${GREEN}✓${NC} Systemd daemon reloaded"
    
    echo ""
    echo -e "${GREEN}Uninstallation complete!${NC}"
}

# Check timer status
check_status() {
    echo -e "${BLUE}Auto-commit timer status:${NC}"
    echo ""
    
    if systemctl --user is-active "${SERVICE_NAME}.timer" &>/dev/null; then
        echo -e "${GREEN}● Timer is ACTIVE${NC}"
    else
        echo -e "${RED}● Timer is INACTIVE${NC}"
    fi
    
    echo ""
    systemctl --user status "${SERVICE_NAME}.timer" 2>/dev/null || echo "Timer not installed"
    
    echo ""
    echo -e "${BLUE}Next scheduled run:${NC}"
    systemctl --user list-timers "${SERVICE_NAME}.timer" 2>/dev/null || echo "Timer not scheduled"
}

# Show usage
usage() {
    echo "Usage: $0 <command> [options]"
    echo ""
    echo "Commands:"
    echo "  install [interval]  Install and start the auto-commit timer"
    echo "                      Default interval: 30min"
    echo "                      Examples: 15min, 1h, 2h"
    echo ""
    echo "  uninstall           Stop and remove the auto-commit timer"
    echo ""
    echo "  status              Check the timer status"
    echo ""
    echo "  run                 Run auto-commit manually once"
    echo ""
    echo "Examples:"
    echo "  $0 install          # Install with 30min interval"
    echo "  $0 install 1h       # Install with 1 hour interval"
    echo "  $0 uninstall        # Remove the timer"
    echo "  $0 status           # Check status"
    echo "  $0 run              # Run manually"
}

# Main
print_header

case "${1:-}" in
    install)
        install_timer "${2:-30min}"
        ;;
    uninstall)
        uninstall_timer
        ;;
    status)
        check_status
        ;;
    run)
        echo -e "${BLUE}Running auto-commit manually...${NC}"
        bash "$AUTOCOMMIT_SCRIPT"
        ;;
    -h|--help|help)
        usage
        ;;
    *)
        usage
        exit 1
        ;;
esac
