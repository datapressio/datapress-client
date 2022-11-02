#!/bin/bash

# [in development] The build process.
# 
# For local development, use the classic:
# pip install -e .

python setup.py bdist_wheel
rm -rf build
rm -rf datapress_client.egg-info
pip install --force-reinstall dist/datapress_client-0.0.1-py3-none-any.whl
