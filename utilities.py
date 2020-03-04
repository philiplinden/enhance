#!/usr/bin/env python3

import os
import logging

import cv2


# shared utility functions

log = logging.getLogger()


def test_logger():
    # these messages only appear if --debug is set
    log.debug('test debug')
    log.critical('test critical')

    # these messages only appear if --verbose is set
    log.info('test info')

    # these messages always appear
    log.warning('test warning')
    log.error('test error')


def load_images(source_dir):
    # Read images from files and append them to a list
    files = [filename for filename in os.listdir(
        source_dir) if os.path.isfile(os.path.join(source_dir, filename))]
    images = []
    for filepath in files:
        image = cv2.imread(filepath)
        if image.empty():
            err_msg = f'{filepath} was not a valid image file.'
            log.error(err_msg)
            raise log.exception(IOError(err_msg))
        images.append(image)
    return images
