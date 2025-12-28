#!/usr/bin/env bash

# ============================================
# Auto-commit script for bc-fastapi bootcamp
# Fedora 43 compatible
# ============================================

set -euo pipefail

# Configuration
REPO_DIR="/home/epti/Documents/epti-dev/bc-channel/bc-fastapi"
LOG_FILE="${REPO_DIR}/_scripts/logs/autocommit.log"
MAX_LOG_SIZE=1048576  # 1MB

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Create log directory if not exists
mkdir -p "$(dirname "$LOG_FILE")"

# Function to log messages
log() {
    local timestamp
    timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    echo "[$timestamp] $1" >> "$LOG_FILE"
    echo -e "${BLUE}[$timestamp]${NC} $1"
}

# Function to rotate log if too large
rotate_log() {
    if [[ -f "$LOG_FILE" ]] && [[ $(stat -c%s "$LOG_FILE" 2>/dev/null || echo 0) -gt $MAX_LOG_SIZE ]]; then
        mv "$LOG_FILE" "${LOG_FILE}.old"
        log "Log rotated"
    fi
}

# Function to detect change type based on files
detect_change_type() {
    local files="$1"
    local type="chore"
    
    # Check for specific patterns
    if echo "$files" | grep -qE "^bootcamp/week-[0-9]+/1-teoria/"; then
        type="docs"
    elif echo "$files" | grep -qE "^bootcamp/week-[0-9]+/2-practicas/"; then
        type="feat"
    elif echo "$files" | grep -qE "^bootcamp/week-[0-9]+/3-proyecto/"; then
        type="feat"
    elif echo "$files" | grep -qE "^bootcamp/week-[0-9]+/4-recursos/"; then
        type="docs"
    elif echo "$files" | grep -qE "^bootcamp/week-[0-9]+/5-glosario/"; then
        type="docs"
    elif echo "$files" | grep -qE "^_docs/"; then
        type="docs"
    elif echo "$files" | grep -qE "^_scripts/"; then
        type="chore"
    elif echo "$files" | grep -qE "^_assets/"; then
        type="feat"
    elif echo "$files" | grep -qE "\.(md|txt)$"; then
        type="docs"
    elif echo "$files" | grep -qE "\.(py)$"; then
        type="feat"
    elif echo "$files" | grep -qE "\.(yml|yaml|json|toml)$"; then
        type="chore"
    elif echo "$files" | grep -qE "^\.github/"; then
        type="ci"
    elif echo "$files" | grep -qE "fix|bug|error|issue" -i; then
        type="fix"
    elif echo "$files" | grep -qE "test" -i; then
        type="test"
    elif echo "$files" | grep -qE "refactor" -i; then
        type="refactor"
    fi
    
    echo "$type"
}

# Function to extract scope from files
extract_scope() {
    local files="$1"
    local scope=""
    
    # Extract week number if present
    if echo "$files" | grep -qoE "week-[0-9]+"; then
        scope=$(echo "$files" | grep -oE "week-[0-9]+" | head -1)
    elif echo "$files" | grep -qE "^_docs/"; then
        scope="docs"
    elif echo "$files" | grep -qE "^_scripts/"; then
        scope="scripts"
    elif echo "$files" | grep -qE "^_assets/"; then
        scope="assets"
    elif echo "$files" | grep -qE "^\.github/"; then
        scope="github"
    fi
    
    echo "$scope"
}

# Function to generate commit message
generate_commit_message() {
    local files="$1"
    local file_count="$2"
    
    local type
    local scope
    local what=""
    local for_what=""
    local impact=""
    
    type=$(detect_change_type "$files")
    scope=$(extract_scope "$files")
    
    # Generate WHAT description
    if [[ $file_count -eq 1 ]]; then
        local filename
        filename=$(basename "$files" | head -1)
        what="update $filename"
    else
        what="update $file_count files"
    fi
    
    # Generate FOR description based on type
    case "$type" in
        feat)
            for_what="add new content for students"
            ;;
        docs)
            for_what="improve documentation clarity"
            ;;
        fix)
            for_what="resolve reported issue"
            ;;
        chore)
            for_what="maintain project infrastructure"
            ;;
        ci)
            for_what="improve CI/CD pipeline"
            ;;
        test)
            for_what="ensure code quality"
            ;;
        refactor)
            for_what="improve code structure"
            ;;
        *)
            for_what="enhance bootcamp content"
            ;;
    esac
    
    # Generate IMPACT description
    case "$type" in
        feat)
            impact="students can access new learning materials"
            ;;
        docs)
            impact="better understanding for learners"
            ;;
        fix)
            impact="smoother learning experience"
            ;;
        chore)
            impact="improved project maintainability"
            ;;
        ci)
            impact="faster and more reliable deployments"
            ;;
        test)
            impact="higher confidence in code correctness"
            ;;
        refactor)
            impact="easier future development"
            ;;
        *)
            impact="enhanced bootcamp quality"
            ;;
    esac
    
    # Build commit message
    local subject
    if [[ -n "$scope" ]]; then
        subject="${type}(${scope}): ${what}"
    else
        subject="${type}: ${what}"
    fi
    
    # Full commit message with body
    local body
    body=$(cat <<EOF

What: ${what}
For: ${for_what}
Impact: ${impact}

Auto-committed by bc-fastapi autocommit script
EOF
)
    
    echo -e "${subject}\n${body}"
}

# Main function
main() {
    rotate_log
    log "Starting auto-commit check..."
    
    # Change to repo directory
    if [[ ! -d "$REPO_DIR" ]]; then
        log "ERROR: Repository directory not found: $REPO_DIR"
        exit 1
    fi
    
    cd "$REPO_DIR"
    
    # Check if it's a git repository
    if [[ ! -d ".git" ]]; then
        log "ERROR: Not a git repository: $REPO_DIR"
        exit 1
    fi
    
    # Get list of changed files
    local changed_files
    changed_files=$(git status --porcelain 2>/dev/null | awk '{print $2}')
    
    if [[ -z "$changed_files" ]]; then
        log "No changes detected. Skipping commit."
        exit 0
    fi
    
    # Count changed files
    local file_count
    file_count=$(echo "$changed_files" | wc -l)
    
    log "Detected $file_count changed file(s)"
    
    # Stage all changes
    git add -A
    
    # Generate commit message
    local commit_message
    commit_message=$(generate_commit_message "$changed_files" "$file_count")
    
    log "Generated commit message:"
    log "$(echo "$commit_message" | head -1)"
    
    # Commit changes
    if git commit -m "$commit_message"; then
        log "Changes committed successfully"
        
        # Try to push (optional, comment out if not needed)
        if git push 2>/dev/null; then
            log "Changes pushed to remote"
        else
            log "WARNING: Could not push to remote (offline or auth issue)"
        fi
    else
        log "ERROR: Commit failed"
        exit 1
    fi
    
    log "Auto-commit completed successfully"
}

# Run main function
main "$@"
