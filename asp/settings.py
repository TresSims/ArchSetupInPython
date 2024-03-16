import subprocess
from .utils import arch_chroot

# Keys from the YAML configuration
KEYMAP = "keymap"
FONT = "console_font"
AUR = "aur_helper"
BOOT = "bootloader"
WIFI = "wifi"
HOST = "hostname"
TZ = "timezone"


class Settings:
    """
    An object representing the settings to be configured for a newly installed system

    :param settings: The settings dictionary to conifure
    """

    def __init__(self, settings):
        self.settings = settings

    def configure_all(self):
        """
        Set up system settings: keymap, console font,
        aur helper, and wifi (not implemented)
        """
        self.configure_keymap()
        self.configure_console_font()
        self.configure_aur_helper()
        self.configure_wifi()

    def configure_keymap(self):
        """
        Set up keymap
        """
        if self.settings[KEYMAP] is "":
            return

        subprocess.run(["loadkeys", self.settings[KEYMAP]])

    def configure_console_font(self):
        """
        Set up console font
        """
        if self.settings[FONT] is "":
            return

        subprocess.run(["setfont", self.settings[FONT]])

    def configure_aur_helper(self):
        """
        Install AUR helper, currently supports: yay
        """
        if self.settings[AUR] is "":
            return

        if self.settings[AUR] is "yay":
            arch_chroot(
                ["pacman", "-S", "--needed", "--noconfirm", "git", "base-devel"]
            )
            arch_chroot(["git", "clone", "https://aur.archlinux.org/yay.git"])
            arch_chroot(["makepkg", "-si", "--noconfirm"], cwd="./yay")

    def configure_wifi(self):
        """
        Connect to wifi network.
        """
        pass
