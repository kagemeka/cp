FROM ubuntu:latest AS base-stage
SHELL ["/bin/bash", "-c"]
ARG DEBIAN_FRONTEND=noninteractive
WORKDIR /root/
RUN \
  apt -q=2 update \
  && apt -yq=2 install \
  apt-utils \
  neovim \
  software-properties-common \
  xclip \  
  xsel \
  && rm -rf /var/lib/apt/lists/* \
  && apt clean -y \
  && echo "PS1='\w\$ '" >> ~/.bashrc \
  && echo "bind '\"\t\":menu-complete'" >> ~/.bashrc


FROM base-stage AS python-stage
WORKDIR /root/ 
ARG PYVER=3.9
RUN \
  apt -q=2 update \
  && apt -yq=2 install \
  python3-neovim \
  python3-pip \
  && add-apt-repository -y \
  ppa:deadsnakes/ppa \
  && apt -q=2 update \
  && apt install -y \
  python$PYVER \
  python$PYVER-distutils \
  python$PYVER-dev \
  && ln -fns \
  /usr/bin/python$PYVER \
  /usr/bin/python3 \
  && ln -fns \
  /usr/bin/python3 \
  /usr/bin/python

COPY lang/python/requirements.txt .
RUN \
  pip3 install -U pip \
  && pip install -Uqr requirements.txt \
  && rm requirements.txt


FROM python-stage AS rust-stage
ENV RUST_BACKTRACE=full
RUN \
  apt -q=2 update \
  && apt install -yq=2 \
  apt-utils \
  build-essential \
  curl \
  && curl \
  --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs \
  | sh -s -- -y \
  && echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> ~/.bashrc 


FROM rust-stage AS go-stage
ARG GOVER=1.17.1
RUN \
  apt -q=2 update \
  && apt install -y \
  apt-utils \
  wget \ 
  && wget -qO - \
  https://dl.google.com/go/go${GOVER}.linux-amd64.tar.gz \
  | tar -xzC /usr/local/ 
  # && echo 'export GOPATH=/usr/local/go' >> ~/.bashrc \
  # && source ~/.bashrc \
  # && echo 'export PATH=$PATH:$GOPATH/bin' >> ~/.bashrc


FROM go-stage AS cpp-stage
RUN \
  apt update -q=2 \
  && apt install -yq=2 \
  apt-utils \
  build-essential \
  xclip \
  xsel 


FROM cpp-stage AS csharp-stage
RUN \
  apt update -q=2 \
  && apt install -yq=2 \
  apt-utils \
  wget \
  && wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb \
  -O packages-microsoft-prod.deb \
  && dpkg -i packages-microsoft-prod.deb \
  && apt -q=2 update \
  && apt install -yq=2 \
  dotnet-sdk-3.1 \
  && dotnet tool install -g dotnet-script


FROM csharp-stage AS dart-stage
RUN \
  apt -q=2 update \
  && apt install -yq=2 \
  apt-utils \
  apt-transport-https \
  gnupg2 \
  wget \
  xclip \
  xsel \
  && wget -qO - \
  https://dl-ssl.google.com/linux/linux_signing_key.pub \
  | apt-key add - \
  && wget -qO - \
  https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list \
  > /etc/apt/sources.list.d/dart_stable.list \
  && apt -q=2 update \
  && apt -yq=2 install dart \
  && echo \
  'export PATH="$PATH:/usr/lib/dart/bin"' \
  >> ~/.bashrc


FROM dart-stage AS julia-stage
ARG MAJOR=1
ARG MINOR=6
ARG PATCH=3
ARG MM_VER=${MAJOR}.${MINOR}
ARG VER=${MM_VER}.${PATCH}
RUN \
  apt update -q=2 \
  && apt install -yq=2 \
  apt-utils \
  wget \
  && wget -O - \
  https://julialang-s3.julialang.org/bin/linux/x64/${MM_VER}/julia-${VER}-linux-x86_64.tar.gz \
  | tar \
  -xvzC /usr/local \
  --transform=s/-${VER}// \
  && ln -fns \
  /usr/local/julia/bin/julia \
  /usr/bin/julia


FROM julia-stage AS java-stage
RUN \
  apt -q=2 update \
  && apt install -yq=2 \
  apt-utils \
  default-jre


FROM java-stage AS kotlin-stage
RUN \
  apt install -yq=2 \
  curl \
  unzip \
  zip \
  && curl -s https://get.sdkman.io | bash \
  && echo \
  'source $HOME/.sdkman/bin/sdkman-init.sh' \
  >> ~/.bashrc \
  && source ~/.bashrc \
  && source $HOME/.sdkman/bin/sdkman-init.sh \
  && sdk install kotlin 


FROM kotlin-stage AS javascript-stage
RUN \
  apt update -q=2 \
  && apt install -yq=2 \
  apt-utils \
  curl \
  sudo \
  && curl \
  -sL https://deb.nodesource.com/setup_current.x \
  | sudo -E bash - \
  && apt install -y nodejs


FROM javascript-stage AS typescript-stage
RUN \
  apt update -q=2 \
  && apt install -yq=2 \
  apt-utils \
  curl \
  sudo \
  && curl \
  -sL https://deb.nodesource.com/setup_current.x \
  | sudo -E bash - \
  && apt install -y nodejs \
  && npm install -g \
  typescript \
  ts-node


FROM ubuntu:20.04 AS lsp-builder
RUN \
  apt -q=2 update \
  && apt install -yq=2 \
  curl \
  git \
  sudo \
  && curl \
  -sL https://deb.nodesource.com/setup_current.x \
  | sudo -E bash - \
  && apt install -y nodejs \
  && git clone https://github.com/apple/sourcekit-lsp.git \
  && cd sourcekit-lsp/Editors/vscode/ \
  && npm install \
  && npm run dev-package \
  && mv sourcekit-lsp-development.vsix /root/


FROM typescript-stage AS swift-stage
ENV SOURCEKIT_TOOLCHAIN_PATH=/usr/local/swift
ARG SWIFT_VER=5.4.2
COPY --from=lsp-builder /root/sourcekit-lsp-development.vsix .
RUN \
  apt update -q=2 \
  && apt install -yq=2 \
  apt-utils \
  binutils \
  git \
  gnupg2 \
  libc6-dev \
  libcurl4 \
  libedit2 \
  libgcc-9-dev \
  libpython2.7 \
  libsqlite3-0 \
  libstdc++-9-dev \
  libxml2 \
  libz3-dev \
  pkg-config \
  tzdata \
  wget \
  zlib1g-dev \
  && wget -O - \
  https://swift.org/builds/swift-${SWIFT_VER}-release/ubuntu2004/swift-${SWIFT_VER}-RELEASE/swift-${SWIFT_VER}-RELEASE-ubuntu20.04.tar.gz \
  | tar -xzC /usr/local/ \
  --transform=s/-${SWIFT_VER}-RELEASE-ubuntu20.04// \
  && echo \
  'export "PATH=/usr/local/swift/usr/bin:$PATH"' >> ~/.bashrc \
  && source ~/.bashrc


FROM swift-stage AS haskell-stage
RUN \
  apt update \
  && apt install -y \
  curl \
  haskell-platform \
  && curl --proto '=https' --tlsv1.2 -sSf \
  https://get-ghcup.haskell.org | sh \
  && curl -sSL https://get.haskellstack.org/ | sh


FROM haskell-stage AS dlang-stage
RUN \
  apt update \
  && curl https://dlang.org/install.sh | bash -s


FROM dlang-stage AS perl-stage 
RUN \
  apt update 


FROM perl-stage AS ocaml-stage
RUN \
  apt update \
  && apt install -y \
  ocaml \
  opam 
  # && opam init -y 
  # && opam install -y \
  # dune 
  # ocaml-lsp-server


FROM ocaml-stage AS php-stage
RUN \
  apt update \
  && apt install -y \
  php


FROM php-stage AS scala-stage
RUN \
  apt update \
  && apt install -y \
  default-jdk \
  scala


FROM scala-stage AS clojure-stage 
ARG CLOJURE_VERSION=1.10.3.998
RUN \
  curl -O https://download.clojure.org/install/linux-install-${CLOJURE_VERSION}.sh \
  && chmod +x linux-install-${CLOJURE_VERSION}.sh \
  && sudo ./linux-install-${CLOJURE_VERSION}.sh \

