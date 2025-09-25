#!/usr/bin/env bash
set -e
python predictive/train.py
python rootcause/train.py
python testprio/train.py
echo "All models trained. Models are under ai/<service>/models/"
