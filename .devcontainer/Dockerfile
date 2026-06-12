# [Choice] Debian OS version (use bullseye on local arm64/Apple Silicon): bullseye, buster, bookworm
ARG VARIANT=bookworm
FROM mcr.microsoft.com/vscode/devcontainers/jekyll:${VARIANT}

RUN rm -f /etc/apt/sources.list.d/yarn.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends python3 python3-pip python3-venv && \
    python3 -m venv /home/vscode/.venv && \
    /home/vscode/.venv/bin/pip install beautifulsoup4 && \
    chown -R vscode:vscode /home/vscode/.venv && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="/home/vscode/.venv/bin:${PATH}"
ENV VIRTUAL_ENV="/home/vscode/.venv"