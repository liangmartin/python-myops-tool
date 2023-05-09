from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

transport = TTransport.TBufferedTransport(TSocket.TSocket('10.10.10.101', 10000))
transport.setTimeout(60)  # 设置连接、发送、接收超时时间均为 60 秒
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = transport.Client(protocol)
transport.open()

sql = "show databases"
client.execute(sql)