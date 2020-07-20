#!/bin/bash

docker build \
    --build-arg USER_UID=$(id -u) \
    --tag demos-segmentation-dependency-builder \
    --file deps/Dockerfile .

docker run \
    --volume $(pwd)/requirements:/mnt \
    --rm \
    demos-segmentation-dependency-builder

docker rmi demos-segmentation-dependency-builder
