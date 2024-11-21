FROM ubuntu:noble

ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/opt/venv

RUN apt update && apt install -y \
    nano \
    git \
    python3 \
    python3-venv \
    vim

RUN python3 -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

EXPOSE 8000