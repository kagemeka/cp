#!/bin/bash

for f in ./scripts/install_*.sh; do
    echo "Running $f"
    bash "$f"
done
