#!/usr/bin/env bash

poetry build
pip3 install dist/ais-0.1.0-py3-none-any.whl --force-reinstall
