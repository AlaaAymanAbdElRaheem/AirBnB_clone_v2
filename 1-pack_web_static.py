#!/usr/bin/python3
"""Fabric script that generates a .tgz archive
from the contents of the web_static folder of your AirBnB Clone repo,
using the function do_pack."""

from fabric.api import local
from datetime import datetime
from fabric.main import main
from collections.abc import Mapping


def do_pack():
    """returns the archive path if the archive has been correctly generated.
    Otherwise, it should return None"""

    date = datetime.now().strftime("%Y%m%d%H%M%S")
    arch_name = "versions/web_static_{}.tgz".format(date)

    local("mkdir -p versions")
    result = local("tar -cvzf {} web_static".format(arch_name))

    if result.failed:
        return None
    else:
        
        return arch_name
