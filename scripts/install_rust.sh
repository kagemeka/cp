# ENV RUST_BACKTRACE=full
apt update
apt install -y curl
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
echo 'export PATH="$HOME/.cargo/bin:$PATH"' >>~/.bashrc
source ~/.bashrc