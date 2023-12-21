#!/bin/bash

# Check if python is installed 
if command -v python3 &>/dev/null; then
    echo "Python3 has already been installed."
# If python not installed, will install python
else
    echo "Python3 has not been installed. Installing now..."
    sudo apt-get update
    sudo apt-get install python3 -y
fi