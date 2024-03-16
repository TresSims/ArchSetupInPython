from .utils import load_config
from .settings import Settings


class Configuration:
    """
    An object representing a system Configuration

    :param config: The configuration to load and install to the system.
    """

    def __init__(self, config):
        self.system_config = load_config(config)
        self.needs_chroot = True

    def full_install(self):
        """
        Install all defined components
        """
        self.configure_settings()
        self.format_disks()
        self.install_system()
        self.install_packages()

    def configure_settings(self):
        """
        Configure system settings.
        """
        Settings(self.system_config["settings"]).configure_all()

    def format_disks(self):
        """
        Create disk partitions
        """
        pass

    def install_system(self):
        """
        Pacstrap base packages to new system
        """
        pass

    def install_packages(self):
        """
        Interactively install base packages.
        """
        pass
