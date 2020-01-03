#!/usr/bin/python3
# Fabric script that generates a .tgz
from datetime import datetime
from fabric.api import local


def do_pack():
    local('mkdir -p versions')
    time = datetime.now()
    folder = 'web_static'
    name_file = "{}{}{}{}{}{}{}".format(folder,
                                        time.year, time.month, time.day,
                                        time.hour, time.minute, time.second)
    local('tar -cavf {}.tar.gz web_static'.format(name_file))
    local('mv *.tar.gz versions/')
