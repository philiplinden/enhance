#!/usr/bin/env python3

#################################################
# Stitch images together into one larger image. #
# https://www.pyimagesearch.com/2018/12/17/image-stitching-with-opencv-and-python
#################################################

import logging
import utils
import cv2
import numpy as np


log = logging.getLogger()


def _mask_null_pixels(image, buffer_pixels=10):
    log.info('Determining crop area...')
    # add pixels to edge to help mask the area
    cv2.copyMakeBorder(image,
                       buffer_pixels,
                       buffer_pixels,
                       buffer_pixels,
                       buffer_pixels,
                       cv2.BORDER_CONSTANT,
                       (0, 0, 0))
    # convert the image to grayscale and threshold it
    # such that all pixels greater than zero are set to 255
    # (foreground) while all others remain 0 (background)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    binary_mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]
    return binary_mask


def _get_outline_from_mask(binary_mask):
    # find all external contours in the threshold image
    contours = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)[0]
    # find the largest contour which will be the contour/outline of
    # the stitched image
    return max(contours, key=cv2.contourArea)


def _get_rectangle_from_outline(outline, array_shape):
    # allocate memory for the mask which will contain the
    # rectangular bounding box of the stitched image region
    mask = np.zeros(array_shape, dtype="uint8")
    (x, y, w, h) = cv2.boundingRect(outline)
    cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)
    return mask


def _erode_binary_mask_to_boundary(binary_mask, boundary_mask):
    # create two copies of the mask: one to serve as our actual
    # minimum rectangular region and another to serve as a counter
    # for how many pixels need to be removed to form the minimum
    # rectangular region
    minRect = mask.copy()
    sub = mask.copy()
    # keep looping until there are no non-zero pixels left in the
    # subtracted image
    while cv2.countNonZero(sub) > 0:
        # erode the minimum rectangular mask and then subtract
        # the thresholded image from the minimum rectangular mask
        # so we can count if there are any non-zero pixels left
        minRect = cv2.erode(minRect, None)
        sub = cv2.subtract(minRect, thresh)


def crop_to_rectangle(image, buffer_pixels=10):
    # mask the outer edge of the image
    pass


def stitch_images(images):
    # stitch a set of images
    stitcher = cv2.Stitcher_create()
    log.info(f'Stitching {len(images)} images...')
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
        log.error(f'Stitching failed: {enum_status[status]}. Are images too '
                  'dissimilar?')
    else:
        log.error('Stitching failed due to an unknown error.')
    return np.array([])


def stitch(source_dir, output_path='stitched_image.jpg', crop_output=False):
    # load images to stitch
    log.info(f'Directory to source images: {source_dir}')
    log.info(f'Path to output file: {output_path}')
    images = utils.load_images(source_dir)

    # stitch images
    stitched_image = stitch_images(images)

    if crop_output:
        # crop output to largest full rectangle
        stitched_image = _crop_to_rectangle(stitched_image)

    # save result to disk
    utils.save_image(output_path, stitched_image)

    return stitched_image
