#!/usr/bin/python

import os
import subprocess

folder = os.path.expanduser("~/.emacs.d")
if not os.path.isdir(folder):
    cmd = f"git clone --depth 1 https://github.com/hlissner/doom-emacs {folder}"
    subprocess.run(cmd, shell=True)
    subprocess.run("doom install", shell=True)

private_config_path = os.path.expanduser("~/.doom.d")
if not os.path.exists(private_config_path):
    cmd = f"git clone git@github.com:xashes/.doom.d.git {private_config_path}"
    subprocess.run(cmd, shell=True)
