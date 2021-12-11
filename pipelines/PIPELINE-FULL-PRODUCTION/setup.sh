#!/bin/bash

set -x
python3.7 -m venv todo-list-aws
source todo-list-aws/bin/activate
python -m pip install --upgrade pip
python -m pip install awscli
python -m pip install aws-sam-cli
# For integration testing
python -m pip install pytest
pwd