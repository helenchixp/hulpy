import sqlite3
from contextlib import closing


class ConnectDB(object):
    def __init__(self, dbinfo):
        self.db_filename = "./db/%s" % dbinfo.db_filename

    def search(self, table_name):
        '''
        '''
        infos = []
        with closing(sqlite3.connect(self.db_filename)) as conn:
            sql = "select * from %s limit 20" % table_name
            conn.row_factory = sqlite3.Row
            for row in conn.execute(sql):
                # dictory item defined by tuple.dont want to change the value
                infos.append({
                         'FileID': row['FileID'], 
                         'Comment': row['Comment'],
                         'UpdateUserID': row['UpdateUserID'],
                         'LastUpdate': row['LastUpdate'],
                         }) 
        return infos
