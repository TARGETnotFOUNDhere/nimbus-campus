#!/bin/bash
# protect-data.sh
# Pre-tool execution hook to enforce directory immutability for protected academic datasets.
# Prevents accidental or unauthorized modifications to critical university records.

set -euo pipefail

# In Claude Code / agent hooks, tool execution arguments are provided via environment variables or stdin JSON.
# Check for tool call payload or targets
TARGET_FILE="${TOOL_ARG_PATH:-${1:-}}"

PROTECTED_DIRS=(
  "mcp-server/data"
  "skills/timetable-helper/data"
  "plugins/campus-helpdesk/skills/timetable-helper/data"
)

if [ -z "$TARGET_FILE" ]; then
  # If input JSON is passed via stdin, check if it contains write operations to protected paths
  if [ ! -t 0 ]; then
    STDIN_DATA=$(cat)
    for pdir in "${PROTECTED_DIRS[@]}"; do
      if echo "$STDIN_DATA" | grep -q "$pdir"; then
        echo "[SECURITY HOOK BLOCKED]: Write access to protected directory '$pdir' is forbidden." >&2
        exit 1
      fi
    done
  fi
  exit 0
fi

# Canonical path check
for pdir in "${PROTECTED_DIRS[@]}"; do
  if [[ "$TARGET_FILE" == *"$pdir"* ]]; then
    echo "[SECURITY HOOK BLOCKED]: Write access to protected directory '$pdir' is forbidden." >&2
    exit 1
  fi
done

exit 0
