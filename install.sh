#!/usr/bin/env bash
pip3 install poetry
poetry build
pip3 install dist/ais-0.1.0-py3-none-any.whl --force-reinstall
