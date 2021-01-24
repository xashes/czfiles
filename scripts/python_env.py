#!/usr/bin/env bash

sudo pacman -S python-pip --needed
sudo pacman -S nodejs --needed
sudo pacman -S npm --needed

pip install -U pytest
pip install -U black
pip install -U pyflakes
pip install -U isort

sudo npm install -g pyright
