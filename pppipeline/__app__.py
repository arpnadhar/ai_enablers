from cutout import create_cutout
import config
import os
import sys
from time import time
import concurrent.futures

# For exe uncomment run()

# def run():
print("Cutout App started running")

if os.path.exists(config.input_image_dir_path):
    print(" Input image path =  ", config.input_image_dir_path)
else:
    print(" Input folder does not exist. Please create before executing.....")
    sys.exit(0)

if os.path.exists(config.output_image_dir_path):
    print(" Output image path =  ", config.output_image_dir_path)
else:
    print(" Output folder does not exist. Please create before executing.....")
    sys.exit(0)

# print(" Model Name =  ", config.modelName)
ts = time()
# Create separate thread for each file
file_list = []

for filename in os.listdir(config.input_image_dir_path):
    input_file = os.path.join(config.input_image_dir_path, filename)
    # print(input_file)
    # create_cutout.process_cutouts(input_file)
    file_list.append(input_file)

if len(file_list) == 0:
    print("No files in input folder")

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its file name
    future_to_files = {executor.submit(create_cutout.process_cutouts, filename): filename for filename in file_list}

    for future in concurrent.futures.as_completed(future_to_files):
        file = future_to_files[future]
        try:
            data = future.result()
        except Exception as exc:
            print('Generated an exception: ', exc)

print('Total time (in seconds) taken for the batch is = ', time() - ts)
print('Usage Statistics have been sent  to achal@burdaeducation.com')
