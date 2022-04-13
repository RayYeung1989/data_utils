import pandas as pd
import jaydebeapi
import redis

class HiveUtils:
    """
    Hive工具类
    """
    def __init__(self, db_driver, db_url, db_user, db_pass, db_jdbc_jar):
        """
        初始化
        Args:
            db_driver: Hive驱动jar包名称，如：org.apache.hive.jdbc.HiveDriver
            db_url: url（如果证书加密的话，url嵌套中要有证书的设置和密码等）
            db_user: 用户名
            db_pass: 密码
            db_jdbc_jar: jdbc驱动jar包路径
        """
        self.db_url = db_url
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_driver = db_driver
        self.db_jdbc_jar = db_jdbc_jar

    def get_data(self, sql):
        conn = jaydebeapi.connect(self.db_driver,
                                  self.db_url, [self.db_user, self.db_pass], self.db_jdbc_jar)
        try:
            df = pd.read_sql(sql, conn)
            conn.close()
            return df
        except Exception as e:
            print(e.args) # 访问异常的错误编号和详细信息
            conn.close()
            return None

    # 分批查询
    def get_data_by_batch(self, sql, batch_size=1000):
        conn = jaydebeapi.connect(self.db_driver,
                                  self.db_url, [self.db_user, self.db_pass], self.db_jdbc_jar)
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            while True:
                rows = cursor.fetchmany(batch_size)
                if not rows:
                    break
                yield rows
            conn.close()
        except Exception as e:
            print(e.args) # 访问异常的错误编号和详细信息
            conn.close()
            return None


# redis工具类
class RedisUtils:

    def __init__(self, host, port, db=None, password=None):
        """
        初始化
        Args:
            host: redis主机
            port: redis端口
            db: redis数据库
            password: redis密码
        """
        self.host = host
        self.port = port
        self.db = db
        self.password = password

    def connection_pool(self):
        """
        连接池
        Returns: Redis实例

        """
        self.pool = redis.ConnectionPool(host=self.host, port=self.port, db=self.db, password=self.password)
        self.r = redis.Redis(connection_pool=self.pool)
        return self.r

    def get_data(self, key):
        """
        获取数据
        Args:
            key: redis key

        Returns: redis value

        """
        return self.r.get(key)

    def get_data_by_batch(self, keys):
        """
        批量获取数据
        Args:
            keys: list 要批量获取的数据的Key列表

        Returns: 获取回来的Value列表

        """
        return self.r.mget(keys)

    def set_data_s(self, key, value, timeout_s=None):
        """
        设置数据（过期时间为秒）
        Args:
            key: redis key
            value: redis value
            timeout_s: redis过期时间，单位秒

        Returns: 设置是否成功

        """
        return self.r.setx(key, timeout_s, value)

    def set_data_ms(self, key, value, timeout_ms=None):
        """
        设置数据（过期时间为毫秒）
        Args:
            key: redis key
            value: redis value
            timeout_ms: redis过期时间，单位毫秒

        Returns: 设置是否成功

        """
        return self.r.setx(key, timeout_ms, value)

    def set_data_by_batch(self, key_value_dict):
        """
        批量设置数据
        Args:
            key_value_dict: key-value字典

        Returns: 设置是否成功

        """
        return self.r.mset(self.key_value_dict)

    def delete_data(self, key):
        """
        删除指定key的数据
        Args:
            key:

        Returns:

        """
        return self.r.delete(key)

    def delete_data_by_batch(self, keys):
        """
        批量删除指定key的数据
        Args:
            keys:

        Returns:

        """
        return self.r.delete(keys)





