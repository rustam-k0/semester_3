#!/bin/sh
# Include hidden names; skip directories and unmatched patterns.
for file in * .[!.]* ..?*; do
    [ -f "$file" ] || continue
    case "$file" in
        ???|????|?????) printf '%s\n' "$file" ;;
    esac
done
