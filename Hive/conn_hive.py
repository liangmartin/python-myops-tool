from pyhive import hive

class HiveClient:
    def __init__(self, host, port=10000, username=None, password=None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = hive.connect(host=self.host, port=self.port, username=self.username, password=self.password)
        self.cursor = self.conn.cursor()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def execute(self, query):
        set_engine_query = "set hive.execution.engine=mr"
        self.cursor.execute(set_engine_query)

        self.cursor.execute(query)
        return self.cursor.fetchall()



if __name__ == '__main__':
    # 创建HiveClient对象并连接到Hive服务器
    hive_client = HiveClient(host='10.10.10.101')
    hive_client.connect()

    # 执行查询
    result = hive_client.execute('SELECT * FROM default.test_lzo')

    # 处理结果
    for row in result:
        print(row)

    # 关闭连接
    hive_client.close()
