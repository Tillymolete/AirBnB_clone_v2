#!/usr/bin/python3
"""A fabric script for web deployment"""
from datetime import datetime
from fabric.api import *
import os

env.hosts = ['54.90.51.69', '18.233.66.101']
env.user = "ubuntu"

def do_pack():
    """A python function that generates a .tgz archive"""

    local('mkdir -p versions')
    t = datetime.now()
    f = "%Y%m%d%H%M%S"


    path = 'verison/web_static_{}.tgz'.format(t.strftime(f))
    archive = local('tar -cvzf {} web_static'.format(path))
    if archive.failed:
        return None
    return path

def do_deploy(archive_path):
    """ Function that distributes an archive to your web servers"""

    try:
        if not os.path.exists(archive_path):
            return False
        to_ex = os.path.basename(archive_path)
        no_ex, ex = os.path.splitext(to_ex)
        dpath = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("rm -rf {}{}/".format(dpath, no_ex))
        run("mkdir -p {}{}/".format(dpath, no_ex))
        run("tar -xzf /tmp/{} -C {}{}/".format(to_ex, dpath, no_ex))
        run("rm /tmp/{}".format(to_ex))
        run("mv {0}{1}/web_static/* {0}{1}".format(dpath, no_ex))
        run("rm -rf {}{}/web_static".format(dpath, no_ex))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(dpath, no_ex))
        print("New version deployed!")
        return True
    except Exception:
        return False

def deploy():
    """full deployment fubction"""

    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
