#!/bin/bash

apt update
apt install -y build-essential clang-format

cat <<EOF >>~/.bashrc
gpp() {
    g++ \$1 -Wall -Wextra -Werror -std=c++17 -O2 -o a.out && ./a.out
}
EOF
