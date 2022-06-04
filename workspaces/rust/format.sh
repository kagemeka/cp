#!/bin/bash

./install_nightly.sh
./install_rustfmt.sh

cargo fmt \
    --all \
    --verbose \
    --manifest-path=Cargo.toml \
    --message-format=human
# --check
