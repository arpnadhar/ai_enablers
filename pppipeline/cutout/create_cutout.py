# Imports for the code
import onnx
import onnxruntime as rt
import numpy as np
import os
# import sys
import cv2
from PIL import Image
import config

# from psd_tools import PSDImage
# from psd_tools.api.mask import Mask
# from PIL import ImageFilter #Gaussian Blur
# from psd_tools.constants import ColorMode


# Get x_scale_factor & y_scale_factor to resize image


def get_scale_factor(im_h=0, im_w=0, ref_size=0):
    im_rh = 0
    im_rw = 0
    if max(im_h, im_w) < ref_size or min(im_h, im_w) > ref_size:
        if im_w >= im_h:
            im_rh = ref_size
            im_rw = int(im_w / im_h * ref_size)
        elif im_w < im_h:
            im_rw = ref_size
            im_rh = int(im_h / im_w * ref_size)
    else:
        im_rh = im_h
        im_rw = im_w

    im_rw = im_rw - im_rw % 32
    im_rh = im_rh - im_rh % 32

    x_scale_factor = im_rw / im_w
    y_scale_factor = im_rh / im_h

    return x_scale_factor, y_scale_factor


def unify_channels(im):
    # print("unifying channels")
    # unify image channels to 3
    if len(im.shape) == 2:
        im = im[:, :, None]
    if im.shape[2] == 1:
        im = np.repeat(im, 3, axis=2)
    elif im.shape[2] == 4:
        im = im[:, :, 0:3]
    return im


def normalize_image(im):
    # print("Normalize Image input ", im)
    # normalize values to scale it between -1 to 1
    im = (im - 127.5) / 127.5
    # print("Normalize Image output ", im)
    return im


def display_image(img):
    # Displaying the image
    cv2.imshow("Image", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

# MODNET Input:float32[batch_size,3,height,width]
# MODNET Output:float32[batch_size,1,height,width]


def execute_model(img):
    # Initialize session and get prediction
    session = rt.InferenceSession(config.modelName, None)
    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name
    print("input image for session run = ", img)
    result = session.run([output_name], {input_name: img})
    # print("Result from modnet",result[0].ravel()[:400])
    return result


def create_foreground(input_image_file, matte_image_path):
    output_file = os.path.basename(matte_image_path).split('.')[0]
    output_cutout_file = os.path.join(config.output_image_dir_path, output_file + "_after.png")

    try:
        input_pil = Image.open(input_image_file)
        img_mode = input_pil.mode
        # config.logging.info("Input image mode = ", img_mode)

        matte_pil = Image.open(matte_image_path)
        matte_mode = matte_pil.mode
        # config.logging.info("Matte image mode = ", matte_mode)

        if matte_mode != "L":
            # config.logging.info("Matte image mode after conversion= ", matte_pil.mode)
            matte_pil = matte_pil.convert("L")

        if img_mode == "CMYK":
            config.logging.info("For CMYK image %s only Matte will be generated",input_image_file)
            print("For CMYK image %s only Matte will be generated", input_image_file)
            # write_to_psd(im_pil, matte_image_path, output_file)
        else:
            input_pil.putalpha(matte_pil)  # add alpha channel to keep transparency
            input_pil.save(output_cutout_file)

    except Exception as e:
        config.logger.debug("Error while handling File = ", input_image_file)
        # print("Matte image path = ", matte_image_path)

        # if os.path.exists(matte_image_path):
        #    os.remove(matte_image_path)

        if os.path.exists(output_cutout_file):
            os.remove(output_cutout_file)

    finally:
        input_pil.close()
        matte_pil.close()

# function to be parallelized

def process_cutouts(input_file):
    try:
        config.logging.info("Processsing file for cutout = ", input_file)
        img = cv2.imread(input_file)
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        print("original image",rgb_img.shape)

        # unify image channels to 3
        rgb_img = unify_channels(rgb_img)
        # print("unified image = ", rgb_img)
        rgb_img = normalize_image(rgb_img)
        # print("normalize image = ", rgb_img)

        im_h, im_w, im_c = rgb_img.shape
        x, y = get_scale_factor(im_h, im_w, config.REF_SIZE)
        # print("Scale factor = ",x,y)

        # resize image
        rgb_img = cv2.resize(rgb_img, None, fx=x, fy=y, interpolation=cv2.INTER_AREA)
        # prepare input shape
        rgb_img = np.transpose(rgb_img)
        rgb_img = np.swapaxes(rgb_img, 1, 2)
        rgb_img = np.expand_dims(rgb_img, axis=0).astype('float32')

        result = execute_model(rgb_img)

        output_file = os.path.basename(input_file).split('.')[0]
        config.logging.info("output file = ", output_file)
        # print("output file = ", output_file)
        # refine matte
        # a mask is the same size as our image, but has only two pixel
        # values, 0 and 255 -- pixels with a value of 0 (background) are
        # ignored in the original image while mask pixels with a value of
        # 255 (foreground) are allowed to be kept
        matte = (np.squeeze(result[0]) * 255).astype('uint8')

        matte = cv2.resize(matte, dsize=(im_w, im_h), interpolation=cv2.INTER_AREA)
        output_matte_image = os.path.join(config.output_image_dir_path, output_file + "_matte.png")
        # print("matte writing ", outputMatteImage)
        cv2.imwrite(output_matte_image, matte)
        # print("matte image", matte.shape)

        create_foreground(input_file, output_matte_image)
    except Exception as e:
        config.logging.info("Error while handling File = ", input_file)
        print("Error while handling File = ", input_file)
        print(e)

    finally:
        print("***Processed ***  ", input_file)
