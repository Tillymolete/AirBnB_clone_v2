#!/usr/bin/python3
""" A fabric script that generates a .tgz archive"""
from datetime import datetime
from fabric.api import local
import os

def do_pac():
    """ A python function that generate a .tgz archive"""

    local('mkdir -p versions')
    t = datetime.now()
    f = "%Y%m%d%H%M%S"

    path = 'version/web_static_{}.tgz'.format(t.strftime(f))
    archive = local('tar -cvzf {} web_static'.format(path))
    if archive.failed:
        return None
    return path
