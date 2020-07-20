# syntax=docker/dockerfile:experimental

FROM python:3.6-slim-buster AS builder

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y \
	ca-certificates \
	git \
	&& rm -rf /var/lib/apt/lists/*

ARG PIP_COMPILE_MULTI_FLAGS=""
ARG USER_UID=1000

RUN pip install pip-tools pip-compile-multi --no-cache-dir

ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements /opt/requirements

WORKDIR opt

RUN pip-compile-multi ${PIP_COMPILE_MULTI_FLAGS}

RUN printf "#!/bin/bash\n" >> /sbin/entrypoint.bash \
    && printf "cp /opt/requirements/*.txt /mnt/\n" >> /sbin/entrypoint.bash \
    && printf "chown $USER_UID:$USER_UID /mnt/*.txt\n" >> /sbin/entrypoint.bash \
    && printf "exec \$@\n" >> /sbin/entrypoint.bash \
    && chmod 744 /sbin/entrypoint.bash

CMD ["entrypoint.bash"]
