#!/usr/bin/python3
'''Fabric script generating .tgz archive'''

from datetime import datetime
from fabric.decorators import task
from fabric.api import local


@task
def do_pack():
    '''develops from the contents of the web_static folder' .tgz archive'''
    local("mkdir -p versions")
    path = ("versions/web_static_{}.tgz"
            .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    result = local("tar -cvzf {} web_static"
                   .format(path))

    if result.failed:
        return None
    return path
