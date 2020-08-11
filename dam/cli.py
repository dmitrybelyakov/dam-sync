import click, os
from dam.colors import *

# -----------------------------------------------------------------------------
# Group setup
# -----------------------------------------------------------------------------


@click.group(help=yellow('DAM-Sync developer console'))
def cli():
    pass


# -----------------------------------------------------------------------------
# Commands
# -----------------------------------------------------------------------------

@cli.command(name='hello')
def hello():
    """ Say hello """
    print(green('\nHello from DAM-Sync!'))
    print(green('-' * 80))
    print()
