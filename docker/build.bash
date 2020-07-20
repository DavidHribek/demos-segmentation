#!/usr/bin/env bash

docker build \
    --target dev \
    -t demos-segmentation-dev:1.0 \
    -f docker/Dockerfile .
