#! /usr/bin/env bash
#
#rm -rf venv/lib/fancy
#rm -rf venv/bin/fancy
rm -rf venv/lib/__pycache__
rm -rf __pycache__

pip install . pyinstaller
pyinstaller --add-data="fancy/folders/*.icns:fancy/folders" -n="fancy-runner-mac" dist/fancy-runner.py

rm -rf build

