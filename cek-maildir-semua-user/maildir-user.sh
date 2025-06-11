#!/bin/bash

for user in /home/*; do
    if [ -d "$user/Maildir" ]; then
        du -sh "$user/Maildir"
    fi
done
