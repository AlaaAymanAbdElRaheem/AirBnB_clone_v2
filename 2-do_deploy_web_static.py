#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy"""

from fabric.api import *
import os.path


def do_deploy(archive_path):
    """distributes an archive to your web servers"""

    env.user = "ubuntu"
    env.hosts = ['54.175.75.247', '18.210.14.159']

    if os.path.exists(archive_path) is False:
        return False

    try:
        put(archive_path, "/tmp/")
        file_name = archive_path.split("/")[-1].split(".")[0]
        new_folder = "/data/web_static/releases/" + file_name + "/"
        run("mkdir -p {}".format(new_folder))
        run("sudo tar -xzf /tmp/{}.tgz -C {}".format(file_name, new_folder))
        run("sudo rm -rf /tmp/{}.tgz".format(file_name))
        run("sudo mv {}web_static/* {}".format(new_folder, new_folder))
        run("sudo rm -rf {}web_static".format(new_folder))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf {} /data/web_static/current".format(new_folder))
        return True
    except Exception:
        return False
