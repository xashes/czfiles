#!/usr/bin/env bash

sudo pacman -S python-pip --needed
sudo pacman -S nodejs --needed
sudo pacman -S npm --needed

pip install -U wheel
pip install -U pytest
pip install -U black
pip install -U pyflakes
pip install -U isort
pip install -U paramiko
pip install -U pandas
pip install -U jupyterlab

sudo npm update -g pyright
