class ConnectDB(object):
    def __init__(self, dbinfo):
        self.dbinfo = dbinfo

    def search(self, table_name):
        info = []
        info.append(self.dbinfo.db_filename)
        tableinfo = self.dbinfo.tableinfo_set.filter(table_name=table_name)[0]
        info.append(tableinfo.table_name)
        return " %s" % " ".join(info)
