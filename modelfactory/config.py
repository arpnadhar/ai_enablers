import os
import logging
import subprocess
import sys


# Check current working directory.
directory = os.getcwd()
print("current directory = ",directory)
# # Check that a directory exists on your computer
# EXE
# ckpt_path = os.path.join(".", "input")
# pycharm
ckpt_path = os.path.join(".", "savemodel", "modnet_webcam_portrait_matting.ckpt")

# EXE
# model_path = os.path.join(".", "output")
# pycharm
model_path = os.path.join(".", "savemodel", "modnet.onnx")

