import os
import logging
import subprocess
import sys

TARGET_DEVICE_UUID = "4C4C4544-0020-2010-8020-A0C04F202020-S314JA0G177977"#MY DEVICE

def get_uuid() -> str:
    return subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()

def get_hdd_id() -> str:
    serials = subprocess.check_output('wmic diskdrive get Name, SerialNumber').decode().split('\n')[1:]
    for serial in serials:
        if 'DRIVE0' in serial:
            return serial.split('DRIVE0')[-1].strip()

unique_id = get_uuid() + '-' + get_hdd_id()

if (TARGET_DEVICE_UUID != unique_id):
    print("This software is not licensed for your hardware. Please contact achal@burdaeducation.com to get your own licensed version")
    print("You can check sample at   https://drive.google.com/file/d/1ep7gMbmTISTmzElD-TEeviWlzQJZQ_P-/view?usp=sharing")
    sys.exit(1)
else :
    print("Configuring the system for license key")

logger = logging.getLogger()
REF_SIZE = 512


# Check current working directory.
directory = os.getcwd()
print("current directory = ",directory)
# # Check that a directory exists on your computer
# EXE
# input_image_dir_path = os.path.join(".", "input")
# pycharm
input_image_dir_path = os.path.join(".", "dist", "input")

# EXE
# output_image_dir_path = os.path.join(".", "output")
# pycharm
output_image_dir_path = os.path.join(".", "dist", "output")

# # Load Model
# EXE
# modelName = os.path.join(".", "pretrained", "mymodel.onnx")
# modelName = os.path.join(".", "pretrained", "modnet.onnx")
# pycharm
modelName = os.path.join(".", "dist", "pretrained", "mymodel.onnx")
# modelName = os.path.join(".", "dist", "pretrained", "modnet.onnx")
print("Configuration done")
#logging.info
# ("Configuration done")