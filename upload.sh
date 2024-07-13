#!/bin/bash
rm -rf build dist oaikit.egg-info
python3 setup.py sdist bdist_wheel
twine upload dist/*
