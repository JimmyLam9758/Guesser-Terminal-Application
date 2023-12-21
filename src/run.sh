#!/bin/bash

# Create virtual environment
python3 -m venv .venv
# activate virtual environment
source .venv/bin/activate
# install eternal python package
pip3 install colored
# run program
python3 wordguess.py

# deactivate and remove virtual environment 
deactivate
rm -r .venv