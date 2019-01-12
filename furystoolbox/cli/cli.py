"""CLI commands."""
from asyncio import get_event_loop

import click


@click.group()
async def commands():
    """Click group."""


@commands.command('hass')
@click.argument('cmd', required=1)
@click.argument('number', required=0)
def hass(cmd, number):
    """Hass cmd."""
    if cmd == 'breaking':
        if not number:
            print("Missing release number.")
            return
        from furystoolbox.cli.hass import breaking_change
        breaking_change(number, True)


@commands.command('random')
@click.argument('cmd', required=1)
def device_info(cmd):
    """random cmd."""
    import random
    if cmd == 'commit':
        from furystoolbox.random import COMMIT
        print()
        print("      ", random.choice(COMMIT))
        print()

LOOP = get_event_loop()
CLI = click.CommandCollection(sources=[commands])
