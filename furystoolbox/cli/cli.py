"""CLI commands."""
from asyncio import get_event_loop

import click


@click.group()
async def commands():
    """Click group."""


@commands.command('hass')
@click.argument('cmd', required=1)
@click.argument('number', required=0)
def device_info(cmd, number):
    """Hass cmd."""
    if cmd == 'breaking':
        if not number:
            print("Missing release number.")
            return
        from furystoolbox.cli.hass import breaking_change
        breaking_change(number)


LOOP = get_event_loop()
CLI = click.CommandCollection(sources=[commands])
