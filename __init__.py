import os
import subprocess

import ranger.api
from ranger.api.commands import Command

hook_init_prev = ranger.api.hook_init
z_loc = os.getenv("_Z_SRC")  # location of rupa z source file


def hook_init(fm):
    def z_add(signal):
        arguments = f"source {z_loc} && _z --add {signal.new.path}"
        cmd = ["bash", "-c", arguments]

        subprocess.Popen(cmd)

    fm.signal_bind("cd", z_add)
    return hook_init_prev(fm)


ranger.api.hook_init = hook_init


class z(Command):
    """:z
    Uses .z file to set the current directory.
    """

    def execute(self):
        try:
            arguments = f"source {z_loc} && _z -e {' '.join(self.args[1:])}"
            cmd = ["bash", "-c", arguments]
            directory = subprocess.check_output(cmd).decode("utf-8").rstrip("\n")

            if directory and os.path.isdir(directory):
                self.fm.cd(directory)

        except subprocess.CalledProcessError:
            raise Exception("Directory not found")
