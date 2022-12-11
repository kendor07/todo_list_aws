#!/bin/bash

set -x
python3.7 -m venv todo-list-aws
source todo-list-aws/bin/activate
python -m pip install --upgrade pip
#For static testing
python -m pip install radon==5.1.0
python -m pip install flake8==5.0.4
python -m pip install flake8-polyfill==1.0.2
python -m pip install bandit==1.7.4
#For integration testing
python -m pip install pytest==7.2.0
#For unit testing
python -m pip install boto3==1.26.27
python -m pip install moto==4.0.11
python -m pip install mock==4.0.3
python -m pip install coverage==6.5.0


pwd
