#!/bin/bash

./scripts/install_common_pkgs.sh
apt update
apt install -y \
    unzip \
    zip

curl -s https://get.sdkman.io | bash
echo "source $HOME/.sdkman/bin/sdkman-init.sh" >>~/.bashrc
source ~/.bashrc
source $HOME/.sdkman/bin/sdkman-init.sh
sdk install kotlin
source ~/.bashrc