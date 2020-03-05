#!/usr/bin/env python3

##########################
# shared utility functions
##########################

import os
import logging

import cv2


log = logging.getLogger()

ALLOWED_FILE_TYPES = [  # all formats supported by cv2.imread
    '.bmp', '.dib'  # windows bitmaps
    '.jpeg', '.jpg', '.jpe',  # JPEG
    '.png',  # Portable Network Graphics
    '.pbm', '.pgm', '.ppm',  # Portable image format
    '.sr', '.ras',  # Sun rasters
    '.tiff', '.tif'  # TIFF
]


def test_logger():
    # these messages only appear if --debug is set
    log.debug('test debug')

    # these messages only appear if --verbose is set
    log.info('test info')

    # these messages always appear
    log.warning('test warning')
    log.critical('test critical')
    log.error('test error')


def _is_valid_image_filename(filename):
    if os.path.splitext(filename)[1].lower() in ALLOWED_FILE_TYPES:
        return True
    else:
        log.error(f'{filename} is not a valid image file type. Valid file '
                  f'types: {ALLOWED_FILE_TYPES}')
        return False


def check_dir_for_images(source_dir):
    # check if there are more than 2 images in the source directory
    log.debug(f'Looking for image files in {source_dir}...')
    image_paths = []
    for root, subdirs, files in os.walk(source_dir):
        for file in files:
            if _is_valid_image_filename(file):
                image_paths.append(os.path.join(root, file))
    log.debug(f'Found {len(image_paths)} images.')
    return image_paths


def load_images(source_dir):
    # look for image files in the source directory
    images_to_load = check_dir_for_images(source_dir)
    if len(images_to_load) < 2:
        log.error(f'Not enough images in {source_dir}. Need at least two image'
                  ' files in this directory.')
        return None

    # Read images from files and append them to a list
    log.debug(f'Loading {len(images_to_load)} images from {source_dir}...')
    images = []
    for filepath in images_to_load:
        image = cv2.imread(filepath)
        if image.size == 0:
            log.error(f'{filepath} was not a valid image file.')
        else:
            images.append(image)
    return images


def save_image(output_filename, image):
    # if it is a valid image and filename, save the image to that path
    if _is_valid_image_filename(output_filename) and image.size > 0:
        cv2.imwrite(output_filename, image)
        log.info(f'Saved {output_filename}')
    else:
        log.error('Save aborted.')
