from augment import create_augments
import config
import os
import sys
from time import time


def run():
    print("Image augmentation started running")

    if os.path.exists(config.augment_image_dir_path):
        print(" Output augmented image path =  ", config.augment_image_dir_path)
    else:
        print(" No output directory specified for augmented images. Please create before executing.....")
        sys.exit(0)

    if os.path.exists(config.augment_mask_dir_path):
        print(" Output augmented mask path =  ", config.augment_mask_dir_path)
    else:
        print(" No output directory specified for augmented masks. Please create before executing.....")
        sys.exit(0)

    if os.path.exists(config.input_image_dir_path):
        print(" Input image path =  ", config.input_image_dir_path)
    else:
        print(" No input directory specified for  images. ")
        sys.exit(0)

    if os.path.exists(config.input_mask_dir_path):
        print(" Input mask path =  ", config.input_mask_dir_path)
    else:
        print(" No input directory specified for masks. Please create before executing.....")
        sys.exit(0)

    # print(" Model Name =  ", config.modelName)
    ts = time()
    # Create separate thread for each file
    image_file_list = []
    mask_file_list = []
    future_to_files = []
    for filename in os.listdir(config.input_image_dir_path):
        input_image_file = os.path.join(config.input_image_dir_path, filename)
        # print(input_file)
        image_file_list.append(input_image_file)


    for maskfilename in os.listdir(config.input_mask_dir_path):
        input_mask_file = os.path.join(config.input_mask_dir_path, maskfilename)
        # print(input_file)
        mask_file_list.append(input_mask_file)


    if len(image_file_list) == 0:
        print("No image files in input folder")
    elif len(mask_file_list) == 0:
        print("No mask files in input folder")
    elif (len(mask_file_list) < len(image_file_list)):
        print("All input images donot have corresponding masks")
    else:
        for i in range(len(image_file_list)):
            create_augments.augment_image_and_mask(image_file_list[i], mask_file_list[i]);