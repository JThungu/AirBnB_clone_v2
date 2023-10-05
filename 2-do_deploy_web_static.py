#!/usr/bin/python3

import os
from fabric.api import env, put, run

# Define the remote hosts
env.hosts = ['54.234.94.20', '100.24.242.71']


def do_deploy(archive_path):
    """
    Deploys the static files from the given archive to the host servers.
    
    Args:
        archive_path (str): The path of the archive to distribute.
        
    Returns:
        bool: Trueif all operations were completed successfully, otherwise false
    """
    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('New version deployed!')
        success = True
    except Exception:
        success = False
    return success
