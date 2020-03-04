#!/usr/bin/env python3

import logging
import cv2


# Stitch images together into one larger image.
# https://www.pyimagesearch.com/2018/12/17/image-stitching-with-opencv-and-python


log = logging.getLogger()


def stitch_images(source_dir, output='stitched_image.jpg'):
    print('hello')
    log.info('Input parameters\n----------------'
             f'\nsource directory: {source_dir}'
             f'\noutput file: {output}'
             )
    log.warning('world')
