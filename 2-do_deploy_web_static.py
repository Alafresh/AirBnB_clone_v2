#!/usr/bin/python3
# Fabric script that generates a .tgz
from datetime import datetime
from fabric.api import local, put, run, env
from os import path

env.hosts = ['35.231.113.169', '34.73.247.107']


def do_pack():
    local('mkdir -p versions')
    time = datetime.now()
    folder = 'web_static_'
    name_file = "{}{}{}{}{}{}{}.tgz".format(folder, time.year,
                                            time.month, time.day,
                                            time.hour, time.minute,
                                            time.second)
    local('tar -cavf {} web_static'.format(name_file))
    local('mv *.tgz versions/')


def do_deploy(archive_path):
    if not path.exists(archive_path):
        return False
    tmp = archive_path[9:]
    tmp1 = archive_path[9:-4]
    try:
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}'.format(tmp1))
        run('tar -xzf /tmp/{} -C\
        /data/web_static/releases/{}/'.format(tmp, tmp1))
        run('rm /tmp/{}'.format(tmp))
        run('mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/'.format(tmp1, tmp1))
        run("rm -rf /data/web_static/releases/{}/web_static".format(tmp1))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/\
         /data/web_static/current'.format(tmp1))
    except Exception:
        return False
