#!/bin/bash

# ./scripts/install_common_pkgs.sh
apt update
apt install -y curl
curl https://dlang.org/install.sh | bash -s

# for activate dmd,
# source ~/dlang/dmd-2.099.1/activate
# update compiler version manually. 
# run `deactivate` for exit.
# https://dlang.org/install.html#activate


# run main.d file.
# rdmd main.d
# https://tour.dlang.org/tour/en/welcome/run-d-program-locally