# Albumentations is a fast and flexible image augmentation library. The library is widely used in industry,
# deep learning research, machine learning competitions, and open source projects. Albumentations is written
# in Python, and it is licensed under the MIT license.
import albumentations as A
import cv2
import config
import os

def augment_image_and_mask(img, mask):
    output_file = os.path.basename(img).split('.')[0]
    #define augmentation pipeline
    #transform = A.Compose([
    #    A.HorizontalFlip(p=1),
    #    A.RandomBrightnessContrast(p=0.2),
    #])

    # Reading an image
    image = cv2.imread(img)
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # read mask
    mask = cv2.imread(mask, cv2.IMREAD_GRAYSCALE)

    #TRANSFORM 1
    transform = A.HorizontalFlip(p=1)
    #pass image and mask to augmented pipeline and receive augmented image and mask
    transformed = transform(image=image, mask=mask)
    transformed_image = transformed['image']
    transformed_mask = transformed['mask']


    output_trfimg_file = os.path.join(config.augment_image_dir_path, output_file + "_trf1.jpg")
    output_trfmask_file = os.path.join(config.augment_mask_dir_path, output_file + "_trfmask1.png")
    cv2.imwrite(output_trfimg_file, transformed_image)
    cv2.imwrite(output_trfmask_file, transformed_mask)

    # TRANSFORM 2
    transform = A.RandomRotate90(p=1)

    # pass image and mask to augmented pipeline and receive augmented image and mask
    transformed = transform(image=image, mask=mask)
    transformed_image = transformed['image']
    transformed_mask = transformed['mask']

    output_trfimg_file = os.path.join(config.augment_image_dir_path, output_file + "_trf2.jpg")
    output_trfmask_file = os.path.join(config.augment_mask_dir_path, output_file + "_trfmask2.png")
    cv2.imwrite(output_trfimg_file, transformed_image)
    cv2.imwrite(output_trfmask_file, transformed_mask)

    #transform3
    transform = A.Transpose(p=1)
    # pass image and mask to augmented pipeline and receive augmented image and mask
    transformed = transform(image=image, mask=mask)
    transformed_image = transformed['image']
    transformed_mask = transformed['mask']

    output_trfimg_file = os.path.join(config.augment_image_dir_path, output_file + "_trf3.jpg")
    output_trfmask_file = os.path.join(config.augment_mask_dir_path, output_file + "_trfmask3.png")
    cv2.imwrite(output_trfimg_file, transformed_image)
    cv2.imwrite(output_trfmask_file, transformed_mask)

    # TRANSFORM 4
    transform = A.RandomRotate90(p=2)

    # pass image and mask to augmented pipeline and receive augmented image and mask
    transformed = transform(image=image, mask=mask)
    transformed_image = transformed['image']
    transformed_mask = transformed['mask']

    output_trfimg_file = os.path.join(config.augment_image_dir_path, output_file + "_trf4.jpg")
    output_trfmask_file = os.path.join(config.augment_mask_dir_path, output_file + "_trfmask4.png")
    cv2.imwrite(output_trfimg_file, transformed_image)
    cv2.imwrite(output_trfmask_file, transformed_mask)

    #transform 5
#    transform = A.ElasticTransform (alpha=0, sigma=70, alpha_affine=70, interpolation=1, border_mode=4, value=None, mask_value=None, always_apply=True, approximate=False, same_dxdy=False, p=0.5)

    # pass image and mask to augmented pipeline and receive augmented image and mask
#    transformed = transform(image=image, mask=mask)
#    transformed_image = transformed['image']
#    transformed_mask = transformed['mask']

#    output_trfimg_file = os.path.join(config.augment_image_dir_path, output_file + "_trf5.jpg")
#    output_trfmask_file = os.path.join(config.augment_mask_dir_path, output_file + "_trfmask5.png")
#    cv2.imwrite(output_trfimg_file, transformed_image)
#    cv2.imwrite(output_trfmask_file, transformed_mask)

    #transform 6
    transform = A.RandomBrightnessContrast(p=0.9)

    # pass image and mask to augmented pipeline and receive augmented image and mask
    transformed = transform(image=image, mask=mask)
    transformed_image = transformed['image']
    transformed_mask = transformed['mask']

    output_trfimg_file = os.path.join(config.augment_image_dir_path, output_file + "_trf6.jpg")
    output_trfmask_file = os.path.join(config.augment_mask_dir_path, output_file + "_trfmask6.png")
    cv2.imwrite(output_trfimg_file, transformed_image)
    cv2.imwrite(output_trfmask_file, transformed_mask)