#!/usr/bin/env python3

import logging
import click

import utilities

import stitcher
import superres


@click.group()
@click.option('-v', '--verbose', is_flag=True)
@click.option('--debug', is_flag=True)
def cli(verbose, debug):
    FORMAT = '%(asctime)-15s %(levelname)+8s: %(message)s'
    logging.basicConfig(format=FORMAT, datefmt="%Y-%m-%dT%H:%M:%S%Z")
    log = logging.getLogger()

    if debug:
        log.setLevel(logging.DEBUG)
    elif verbose:
        log.setLevel(logging.INFO)
    else:
        log.setLevel(logging.WARNING)


@cli.command()
@click.argument('source_dir', type=click.Path(exists=True, file_okay=False))
@click.option(
    '--output', '-o', default='stitched_image.jpg', show_default=True,
    help='The file name of the output image.'
)
def stitch(source_dir, output):
    # The main function that runs when the CLI is called
    stitcher.stitch_images(source_dir, output)


@cli.command()
@click.argument('source_dir', type=click.Path(exists=True, file_okay=False))
@click.option(
    '--output', '-o', default='stitched_image.jpg', show_default=True,
    help='The file name of the output image.'
)
def zoom(source_dir, output):
    # The main function that runs when the CLI is called
    superres.combine_images(source_dir, output)


@cli.command()
def test():
    utilities.test_logger()


cli.add_command(stitch)
cli.add_command(test)


if __name__ == '__main__':
    cli()
