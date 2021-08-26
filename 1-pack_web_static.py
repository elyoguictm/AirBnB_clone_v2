#!/usr/bin/python3
"""1. Compress before sending"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """Make a .tgz archive"""
    try:
        local("mkdir -p versions")
        now = datetime.now()
        time = now.strftime("%Y%m%d%H%M%S")
        file = "versions/web_static_" + time + ".tgz"
        local("tar -cvzf " + file + " web_static")
        return file
    except:
        return None
