#!/bin/bash

./scripts/install_common_pkgs.sh
apt update
curl -sL https://deb.nodesource.com/setup_current.x | sudo -E bash -
apt install -y nodejs
