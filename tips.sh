#!/usr/bin/env bash

rm -rf dist
rm -rf build
rm -rf rlgridworld.egg-info
python setup.py bdist_wheel
python -m twine upload dist/*
sleep 6
pip install --no-cache-dir -U rlgridworld