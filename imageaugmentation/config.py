import os
import logging
import subprocess
import sys

# Check current working directory.
directory = os.getcwd()
print("current directory = ",directory)
# # Check that a directory exists on your computer
# EXE
# input_image_dir_path = os.path.join(".", "image")
# pycharm
augment_image_dir_path = os.path.join(".", "dist","output_image")

# EXE
# output_image_dir_path = os.path.join(".", "alpha")
# pycharm
augment_mask_dir_path = os.path.join(".", "dist", "output_alpha")

# input_image_dir_path = os.path.join(".", "image")
# pycharm
input_image_dir_path = os.path.join(".", "dist", "input_images")
# input_mask_dir_path = os.path.join(".", "mask")
# pycharm
input_mask_dir_path = os.path.join(".", "dist", "input_masks")