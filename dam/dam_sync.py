#!/usr/bin/env python3
import click
import os
import yaml
from dam.colors import *
from pprint import pprint as pp

# -----------------------------------------------------------------------------
# Group setup
# -----------------------------------------------------------------------------


@click.group(help=yellow('DAM-Sync utility'))
def cli():
    pass


# -----------------------------------------------------------------------------
# Commands
# -----------------------------------------------------------------------------

config_dir = os.path.expanduser('~/.dam-sync')
config_path = os.path.join(config_dir, 'config.yml')


def get_config():
    """
    Returns current config for your environment
    """
    if not os.path.isdir(config_dir):
        os.makedirs(config_dir)

    if not os.path.isfile(config_path):
        return None

    with open(config_path) as file:
        config = yaml.load(file, Loader=yaml.SafeLoader)

    pp(config)
    return config


@cli.command(name='configure')
@click.option(
    '--source',
    default=None,
    prompt=True,
    help='Local library path to backup'
)
@click.option(
    '--destination',
    default=None,
    prompt=True,
    help='Target local path to backup to'
)
@click.option(
    '--s3-bucket',
    default=None,
    prompt=True,
    help='AWS S3 bucket name. Can also contain name/path.'
)
@click.option(
    '--aws-profile',
    default=None,
    prompt=True,
    help='AWS CLI profile to use for authentication'
)
def configure(source, destination, s3_bucket, aws_profile):
    """ Configure sync"""
    print(green('\nHello from DAM-Sync!'))
    print(green('-' * 80))
    print()

    # check config
    config = get_config()
    if config:
        print(red('Found configuration at "{}" '.format(config_path)))
        if not click.confirm(red('Do you want to continue and overwrite it?')):
            print(cyan('Skipping...\n'))
            return

    # write config
    with open(config_path, 'w') as file:
        config = dict(
            source=source,
            destination=destination,
            s3_bucket=s3_bucket,
            aws_profile=aws_profile,
        )
        yaml.dump(config, file)

    # report success
    print(green('\nSuccessfully written config to "{}"\n'.format(config_path)))
    return


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

