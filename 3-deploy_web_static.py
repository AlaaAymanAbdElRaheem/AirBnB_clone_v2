#!/usr/bin/python3
""" Fabric script (based on the file 2-do_deploy_web_static.py) """

from fabric.api import *
import os.path
from datetime import datetime


env.user = "ubuntu"
env.hosts = ['54.175.75.247', '18.210.14.159']
env.key_filename = '~/.ssh/school'


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


def do_deploy(archive_path):
    """distributes an archive to your web servers"""

    if os.path.exists(archive_path) is False:
        return False

    try:
        put(archive_path, "/tmp/")
        file_name = archive_path.split("/")[-1].split(".")[0]
        new_folder = "/data/web_static/releases/" + file_name + "/"
        run("mkdir -p {}".format(new_folder))
        run("sudo tar -xzvf /tmp/{}.tgz -C {}".format(file_name, new_folder))
        run("sudo rm -rf /tmp/{}.tgz".format(file_name))
        run("sudo mv {}web_static/* {}".format(new_folder, new_folder))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf {} /data/web_static/current".format(new_folder))
        return True
    except Exception:
        return False


def deploy():
    """creates and distributes an archive to your web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
