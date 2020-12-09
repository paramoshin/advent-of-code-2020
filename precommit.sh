#!/bin/bash

. .venv/bin/activate
black "$@"
isort -y "$@"
mypy "$@"
