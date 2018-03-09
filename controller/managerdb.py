import sqlite3
from contextlib import closing


class ConnectDB(object):
    #########################
    def __init__(self, dbname):
        self.db_filename = "./db/%s" % dbname

    #########################
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

    #########################
    def get_detail_by_fileid(self, table_name, file_id):
        """
        this method is get management data by file_id from table
        """

        def dict_factory(cursor, row):
            """
            this method is convert the sqlite row to dictionary
            """
            d = {}
            for idx, col in enumerate(cursor.description):
                d[col[0]] = row[idx]
            return d

        detail_info = {}
        with closing(sqlite3.connect(self.db_filename)) as conn:
            sql = "select * from %s where FileID = :file_id" % table_name
            conn.row_factory = dict_factory
            cursor = conn.cursor()
            rows = cursor.execute(sql, {'file_id':file_id})
            detail_info = rows.fetchone()
        return detail_info


    def update(self, table_name, detail_info):
        with closing(sqlite3.connect(self.db_filename)) as conn:
            sql = """
                    update %s set
                    Comment = :comment,
                    FileName = :file_name
                    where
                    FileID = :fileid
                  """  % table_name
            cursor = conn.cursor()
            cursor.execute(sql, {
                'comment': "%s ...Update by django.. " % detail_info['Comment'],
                'file_name': detail_info['FileName'],
                'fileid': detail_info['FileID']
                })
            conn.commit()
        print("---------------", detail_info)
