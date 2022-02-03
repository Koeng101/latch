"""
cli.main
~~~~~~~~~~~~~~
CLI entrypoints.
"""

from typing import Union

import click
from latch.services import cp as _cp
from latch.services import init as _init
from latch.services import login as _login
from latch.services import register as _register


@click.group("latch")
def main():
    """A commmand line toolkit to interact with the LatchBio platform"""
    ...


@click.command("register")
@click.argument("pkg_root", nargs=1, type=click.Path(exists=True))
@click.option(
    "--dockerfile",
    default=None,
    help="An explicit Dockerfile to define your workflow's execution environment",
)
@click.option(
    "--pkg_name",
    default=None,
    help="The name of your workflow package (the folder with __init__.py). This is a mandatory option if --dockerfile is provided",
)
def register(pkg_root: str, dockerfile: Union[str, None], pkg_name: Union[str, None]):
    _register(pkg_root, dockerfile, pkg_name)
    click.secho(
        "Successfully registered workflow. View @ console.latch.bio.", fg="green"
    )


@click.command("login")
def login():
    _login()
    click.secho("Successfully logged into LatchBio.", fg="green")


@click.command("init")
@click.argument("pkg_name", nargs=1)
def init(pkg_name: str):
    _init(pkg_name)
    click.secho(f"Created a latch workflow called {pkg_name}.", fg="green")
    click.secho("Run", fg="green")
    click.secho(f"\t$ cd {pkg_name}; latch register . ", fg="green")
    click.secho("To register the workflow with console.latch.bio.", fg="green")


@click.command("cp")
@click.argument("local_file", nargs=1, type=click.Path(exists=True))
@click.argument("remote_dest", nargs=1)
def cp(local_file: str, remote_dest: str):
    _cp(local_file, remote_dest)
    click.secho(f"Successfully copied {local_file} to {remote_dest}.", fg="green")


main.add_command(register)
main.add_command(login)
main.add_command(init)
main.add_command(cp)