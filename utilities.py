#!/usr/bin/env python3

import click
import os
import cv2


def load_images(source_dir):
    # Read images from files and append them to a list
    files = [filename for filename in os.listdir(
        source_dir) if os.path.isfile(os.path.join(source_dir, filename))]
    images = []
    for filepath in files:
        image = cv2.imread(filepath)
        if image.empty():
            raise IOError(f'{filepath} was not a valid image file.')
        images.append(image)
    return images
