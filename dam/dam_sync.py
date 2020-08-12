#!/usr/bin/env python3
import click
from dam.colors import *

# -----------------------------------------------------------------------------
# Group setup
# -----------------------------------------------------------------------------


@click.group(help=yellow('DAM-Sync utility'))
def cli():
    pass


# -----------------------------------------------------------------------------
# Commands
# -----------------------------------------------------------------------------

@cli.command(name='configure')
def configure():
    """ Configure sync"""
    print(green('\nHello from DAM-Sync!'))
    print(green('-' * 80))
    print()


@cli.command(name='run')
@click.option('--disk/--skip-disk', default=False)
@click.option('--cloud/--skip-cloud', default=False)
def run(disk, cloud):
    """ Backup your assets """
    print(green('\nHello from DAM-Sync!'))
    print(green('-' * 80))
    print()

    """
    Collect options
    """

    sync_disk = False
    sync_cloud = False

    # by default sync all (no flags)
    if not disk and not cloud:
        sync_disk = True
        sync_cloud = True

    # sync all if both flags (weird, but ok)
    if disk and cloud:
        sync_disk = True
        sync_cloud = True

    # just sync disk
    if disk and not cloud:
        sync_disk = True
        sync_cloud = False

    # or just sync cloud
    if cloud and not disk:
        sync_disk = False
        sync_cloud = True

    """
    Do the sync
    """

    # sync disk
    if sync_disk:
        print('Syncing to disk')

    # sync cloud
    if sync_cloud:
        print('Syncing to S3')

