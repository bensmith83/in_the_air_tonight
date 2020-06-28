#!/bin/sh

touch in_the_air_tonight/__init__.py
python3 setup.py bdist_wheel --universal 
