#!/usr/bin/env python3

from setuptools import setup


setup(name='enhance',
      version='0.1',
      description='Image stitching and multi-frame super-resolution from '
                  'video',
      url='http://github.com/philiplinden/enhance',
      author='Philip Linden',
      author_email='lindenphilipj@gmail.com',
      license='MIT',
      packages=['enhance'],
      install_requires=[
          'numpy',
          'Click',
          'opencv-contrib-python'
      ],
    entry_points='''
        [console_scripts]
        enhance=cli:test
    ''',
      zip_safe=False)