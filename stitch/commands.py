#!/usr/bin/env python3

# Python packages
import click
import cv2

# local modules
import utilities


@click.group()
def cli():
    pass


@click.command()
@click.argument('source_dir', type=click.Path(exists=True, file_okay=False))
@click.option(
    '--output', '-o', default='stitched_image.jpg', show_default=True,
    help='The file name of the output image.'
)
@click.option(
    '--verbose', '-v', is_flag=True,
    help='Print detailed log messages.'
)
def stitch(source_dir, output, verbose):
    # The main function that runs when the CLI is called
    if verbose:
        print('Input parameters\n----------------'
              f'\nsource directory: {source_dir}'
              f'\noutput file: {output}'
              )
    print('hello')

cli.add_command(stitch)
