from django.conf import settings

from datetime import datetime
from kazoo.client import KazooClient

PERM_READ = 1
PERM_WRITE = 2
PERM_CREATE = 4
PERM_DELETE = 8
PERM_ADMIN = 16
PERM_ALL = PERM_READ | PERM_WRITE | PERM_CREATE | PERM_DELETE | PERM_ADMIN

TIMEOUT = 10.0

ZOOKEEPER_SERVERS = getattr(settings, 'ZOOKEEPER_SERVERS')

def _convert_stat(stat):
    rtv = {}
    for key in dir(stat):
        if key.startswith('_'):
            continue
        value = getattr(stat, key)
        if key in ['ctime', 'mtime']:
            rtv[key] = datetime.fromtimestamp(value / 1000)
        else:
            rtv[key] = value
    return rtv

def _convert_acls(acls):
    rtv = []
    for acl in acls:
        perms = acl.perms
        perms_list = []
        if perms & PERM_READ:
            perms_list.append('PERM_READ')
        if perms & PERM_WRITE:
            perms_list.append('PERM_WRITE')
        if perms & PERM_CREATE:
            perms_list.append('PERM_CREATE')
        if perms & PERM_DELETE:
            perms_list.append('PERM_DELETE')
        if perms & PERM_ADMIN:
            perms_list.append('PERM_ADMIN')
        if perms & PERM_ALL == PERM_ALL:
            perms_list = ['PERM_ALL']
        rtv.append({'scheme': acl.id.scheme, 'id': acl.id.id, 'perm_list': perms_list})
    return rtv

class ZNode(object):
    def __init__(self, path='/'):
        self.path = path
        zk_client =  KazooClient(hosts=ZOOKEEPER_SERVERS, read_only=True, timeout=TIMEOUT)
        try:
            zk_client.start()
            self.data, stat = zk_client.get(path)
            self.stat = _convert_stat(stat)
            self.children = zk_client.get_children(path) or []
            self.acl = _convert_acls(zk_client.get_acls(path)[0])
        finally:
            zk_client.stop()
