import click
from .configuration import Configuration


@click.group()
def cli():
    pass


@cli.command()
@click.argument("config")
@click.option(
    "--settings", default=False, is_flag=True, help="Apply setting configuration"
)
@click.option(
    "--system", default=False, is_flag=True, help="Pacstrap packages to new system"
)
@click.option("--packages", default=False, is_flag=True, help="Install packages")
@click.option("--disks", default=False, is_flag=True, help="Format disks")
@click.option(
    "--daemons", default=False, is_flag=True, help="Start up system processes"
)
@click.option("--all", default=False, is_flag=True, help="Install all settings")
def install(config, settings, system, packages, disks, daemons, all):
    config = Configuration(config)

    if all:
        config.full_install()
    else:
        if settings:
            config.configure_settings()
        if system:
            config.install_system()
        if disks:
            config.format_disks()

        if packages:
            config.install_packages()

        if daemons:
            pass
