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

ZOOKEEPER_SERVERS = getattr(settings,'ZOOKEEPER_SERVERS')

class ZNode(object):
    def __init__(self, path='/'):
        self.path = path
        zk =  KazooClient(hosts=ZOOKEEPER_SERVERS, read_only=True, timeout=TIMEOUT)
        try:
            zk.start()
            self.data, stat = zk.get(path)
            self.stat = {}
            for k in dir(stat):
                if k.startswith('_'):
                    continue
                v = getattr(stat, k)
                if k in ['ctime', 'mtime']:
                    self.stat[k] = datetime.fromtimestamp(v/1000)
                else:
                    self.stat[k] = v
            self.children = zk.get_children(path) or []
            self.acls = []
            acls = zk.get_acls(path)[0] or []
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
                self.acls.append({'scheme': acl.id.scheme, 'id': acl.id.id, 'perm_list': perms_list})
        finally:
            zk.stop()
