#!/bin/bash

apt update
apt install -y wget
wget \
    https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb \
    -O packages-microsoft-prod.deb
dpkg -i packages-microsoft-prod.deb
apt update
apt install -y dotnet-sdk-3.1
dotnet tool install -g dotnet-script
