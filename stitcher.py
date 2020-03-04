#!/usr/bin/env python3

#################################################
# Stitch images together into one larger image. #
# https://www.pyimagesearch.com/2018/12/17/image-stitching-with-opencv-and-python
#################################################

import logging
import utils
import cv2


log = logging.getLogger()


def stitch_images(images):
    # stitch a set of images
    stitcher = cv2.Stitcher_create()
    (status, stitched) = stitcher.stitch(images)
    enum_status = {
        0: 'OK',
        1: 'ERR_NEED_MORE_IMAGES',
        2: 'ERR_HOMOGRAPHY_EST_FAIL',
        3: 'ERR_CAMERA_PARAMS_ADJUST_FAIL',
    }
    if status == 0:
        log.info(f'Successfully stitched {len(images)} images.')
        return stitched
    elif status in enum_status:
        log.error(f'Stitching failed. ({enum_status[status]})')
    else:
        log.error('Stitching failed due to an unknown error.')
    return None


def stitch(source_dir, output='stitched_image.jpg'):
    # load images to stitch
    log.info(f'Inputs [source directory: {source_dir} '
             f'| output file {output}]')
    images = utils.load_images(source_dir)

    # stitch images
    stitched_image = stitch_images(images)

    # save result to disk
    if stitched_image:
        cv2.imwrite(stitched_image)

    return stitched_image
