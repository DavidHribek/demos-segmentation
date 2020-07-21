ARG VENV_PATH=/opt/venv

FROM python:3.8-slim-buster as dev

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y \
	git \
	libglib2.0-0 \
	wget \
	sudo \
	gosu \
	&& rm -rf /var/lib/apt/lists/*

# Create Python virtual environment
ARG VENV_PATH
ENV VIRTUAL_ENV=$VENV_PATH
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies
COPY docker/requirements/ /tmp/requirements
RUN pip install \
	-r /tmp/requirements/base.txt \
	-r /tmp/requirements/dev.txt \
	-r /tmp/requirements/test.txt \
	--no-cache-dir \
	&& rm -R /tmp/requirements

WORKDIR /app

COPY docker/create-user.bash /sbin/create-user
RUN chmod 755 /sbin/create-user &&\
    chown root:root /sbin/create-user

ENTRYPOINT [ "create-user" ]
