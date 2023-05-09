from pyhive import hive


import socket

timeout = 10
socket.setdefaulttimeout(timeout)

host = "10.10.10.101"
port = 10000
game = "test"
database = "default"

# 连接到远程 Metastore
conn = hive.Connection(host=host, port=port,username=test,database=database)
# 查询表信息
cursor = conn.cursor()
cursor.execute("input your sql")
tables = cursor.fetchall()

#time.sleep(10)
# 输出查询结果
print(tables)

# 关闭连接
cursor.close()
conn.close()