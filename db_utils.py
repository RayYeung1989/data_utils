import pandas as pd
import jaydebeapi

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


