#! /bin/bash

echo "===> Running Tests..."

echo "===> Flake8 Running..."
flake8 . --exclude "*venv*"
echo "===> Flake8 Finished"

echo "===> Python2 Tests Running..."
python2 -m pytest -v
echo "===> Python2 Tests Finished"

echo "===> Python3 Tests Running..."
python3 -m pytest -v
echo "===> Python3 Tests Finished"
