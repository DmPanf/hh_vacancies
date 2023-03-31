#!/bin/bash

curl -sSL https://install.python-poetry.org | python3 -

poetry init

poetry install

poetry shell

poetry run python main.py
