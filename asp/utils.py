import validators
import yaml
import os
import requests
import subprocess

ROOT = "/mnt"


def load_config(location):
    """
    Returns YAML dictionary from url or file path
    """
    if validators.url(location):
        resp = requests.get(location)
        file = resp.raw

    elif os.path.isfile(location):
        file = location

    else:
        raise FileNotFoundError(f"{location} does not exist, and cannot be loaded")

    with open(file) as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as e:
            raise yaml.YAMLError(f"Yaml was not able to be parsed: {e}")


def arch_chroot(command):
    """
    Run shell commands in chroot-ed environment
    """
    full_command = ["arch-chroot", ROOT]
    full_command.append(command)

    subprocess.run(full_command)
