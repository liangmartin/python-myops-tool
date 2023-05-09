from hdfs import InsecureClient

class HDFSClient:
    def __init__(self, url, user):
        self.client = InsecureClient(url, user=user)

    def ls(self, path):
        return self.client.list(path)

    def read(self, path):
        with self.client.read(path) as f:
            return f.read()

    def write(self, path, data):
        with self.client.write(path) as f:
            f.write(data)

if __name__ == '__main__':
    # 创建HDFSClient对象并连接到HDFS
    hdfs_client = HDFSClient(url='http://10.10.10.101:50070', user='test')

    # 检索文件或目录列表
    file_list = hdfs_client.ls('/test/test_lzo_parquet6/ds=2020-09-23')

    # 读取文件内容
    content = hdfs_client.read('/test/test_lzo_parquet6/ds=2020-09-23/000000_0')

    # 写入文件内容
   # hdfs_client.write('/path/to/new_file', b'This is a test.')

    # 关闭连接
    hdfs_client.client.close()
