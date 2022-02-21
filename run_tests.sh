#! /bin/bash

echo "===> Running Tests..."

echo "===> Flake8 Running..."
flake8 . --exclude "*venv*"
echo "===> Flake8 Finished"

echo "===> Python3 Tests Running..."
python3 -m pytest -sv
echo "===> Python3 Tests Finished"
