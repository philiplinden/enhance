#!/usr/bin/env python3

##########################
# shared utility functions
##########################

import os
import logging

import cv2


log = logging.getLogger()


def test_logger():
    # these messages only appear if --debug is set
    log.debug('test debug')

    # these messages only appear if --verbose is set
    log.info('test info')

    # these messages always appear
    log.warning('test warning')
    log.critical('test critical')
    log.error('test error')


def check_dir_for_images(source_dir):
    # check if there are more than 2 images in the source directory

def load_images(source_dir):
    # Read images from files and append them to a list
    if not check_dir_for_images(source_dir):
        log.error(f'Not enough images in {source_dir}. Need at least two')
        return None
    files = [filename for filename in os.listdir(
        source_dir) if os.path.isfile(os.path.join(source_dir, filename))]
    images = []
    for filepath in files:
        image = cv2.imread(filepath)
        if not image:
            log.error(f'{filepath} was not a valid image file.')
        else:
            images.append(image)
    return images
