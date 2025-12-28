#!/usr/bin/env bash

# Activate venv
source venv/Scripts/activate

# Run tests with environment
pytest --env=qa

# Generate Allure HTML report
allure generate allure-results -o allure-report --clean
