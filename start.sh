#!/bin/bash

# 1. Установить Poetry на свой компьютер, если он еще не установлен
curl -sSL https://install.python-poetry.org | python3 -

# 2. установить все зависимости, указанные в pyproject.toml
poetry install

# 
# poetry shell

# 3. запустить стартовый скрипт проекта
poetry run python main.py
