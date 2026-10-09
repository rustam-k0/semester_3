#!/bin/sh
# Keep the original argument numbers. Avoid eval and external commands.
position=$#
while [ "$position" -gt 0 ]; do
    current=1
    for argument do
        if [ "$current" -eq "$position" ]; then
            printf '%s: %s\n' "$position" "$argument"
            break
        fi
        current=$(( current + 1 ))
    done
    position=$(( position - 1 ))
done
