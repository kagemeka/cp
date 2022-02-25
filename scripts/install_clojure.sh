#!/bin/bash

CLOJURE_VERSION=1.10.3.998
apt update
./scripts/install_common_pkgs.sh
apt install -y rlwrap

curl -O https://download.clojure.org/install/linux-install-${CLOJURE_VERSION}.sh
chmod +x linux-install-${CLOJURE_VERSION}.sh
sudo ./linux-install-${CLOJURE_VERSION}.sh
