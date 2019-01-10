"""CLI commands."""
import click
from googledevices.helpers import gdh_loop


@click.group()
async def commands():
    """Click group."""


@commands.command('hass')
@click.argument('cmd', required=1)
@click.argument('url', required=0)
def device_info(cmd, url):
    """Hass cmd."""
    if cmd == 'breaking':
        from googledevices.cli.commands.hass import breaking_change
        breaking_change(url)


LOOP = gdh_loop()
CLI = click.CommandCollection(sources=[commands])
