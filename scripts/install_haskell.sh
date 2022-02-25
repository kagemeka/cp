#!/bin/bash

./scripts/install_common_pkgs.sh
apt update
apt install -y haskell-platform
curl --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org | sh
curl -sSL https://get.haskellstack.org/ | sh
