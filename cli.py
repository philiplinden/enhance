#!/usr/bin/env python3

import click
from stitch import commands as stitch


@click.group(context_settings={'help_option_names': ['-h', '-?', '--help']},
             invoke_without_command=True)
@click.argument('source_dir', type=click.Path(exists=True, file_okay=False))
@click.pass_context
def cli(ctx, source_dir):
    click.echo('Hello world!', err=True)
    if ctx.invoked_subcommand is None:
        print(ctx.obj.json)


@cli.command()
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
    print('hello again')


if __name__ == '__main__':
    cli()
