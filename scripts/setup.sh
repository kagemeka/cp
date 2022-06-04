#!/bin/bash

for f in ./scripts/install_*.sh; do
    echo "Running $f"
    bash "$f"
done

apt update
apt install -y \
    build-essential \
    clang-format \
    neovim
