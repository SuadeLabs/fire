#! /bin/bash

echo "===> Running Tests..."

echo "===> Flake8 Running..."
flake8 . --exclude "*venv*"
echo "===> Flake8 Finished"

echo "===> PyTest Running..."
pytest -v
echo "===> PyTest Finished"
