#!/bin/bash

apt update
apt install -y ocaml opam
opam init -y
opam install -y \
    dune \
    ocaml-lsp-server
