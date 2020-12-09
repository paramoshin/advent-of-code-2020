#!/bin/bash

. .venv/bin/activate
black "$@"
isort -y "$@"
mypy --config-file pyproject.toml "$@"
