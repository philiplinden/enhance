#!/usr/bin/env python3

import logging
import cv2


# Make one high resolution image from a set of lower resolution images

log = logging.getLogger()


def combine_images(source_dir, output='stitched_image.jpg'):
    print('hello')
    log.info('Input parameters\n----------------'
             f'\nsource directory: {source_dir}'
             f'\noutput file: {output}'
             )
    log.warning('world')
