#!/bin/sh
if [ "$(( $# % 2 ))" -ne 0 ]; then
    printf 'Usage: %s para1 para2 [para3 para4]...\n' "$0" >&2
    exit 1
fi
