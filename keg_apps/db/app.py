from __future__ import absolute_import
from __future__ import unicode_literals

from keg.app import Keg


class DBApp(Keg):
    import_name = 'keg_apps.db'
    db_enabled = True


if __name__ == '__main__':
    DBApp.cli_run()
