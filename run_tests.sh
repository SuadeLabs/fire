#! /bin/bash

echo "===> Running Tests..."

echo "===> Flake8 Running..."
flake8 . --exclude "*venv*"
echo "===> Flake8 Finished"

echo "===> Python Tests Running..."
pytest -v
echo "===> Python Tests Finished"

