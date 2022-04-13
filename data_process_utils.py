import pandas as pd
# import modin.pandas as pd
import json

# 数据处理工具类
class DataProcessUtils:
    def __init__(self, pands_or_modin):
        """
        初始化
        Args:
            pands_or_modin: str, 'pandas' or 'modin'
        """
        self.pands_or_modin = pands_or_modin
        if pands_or_modin == 'pandas':
            import pandas as pd
        elif pands_or_modin == 'modin':
            import modin.pandas as pd

# json层数
def json_level(json_str):
    if isinstance(json_str, str):
        json_str = json.loads(json_str)
    if not isinstance(json_str, dict):
        return 0
    else:
        return 1 + max([json_level(v) for k, v in json_str.items()])

# 正则匹配
def regex_match(regex, string):
    import re
    return re.search(regex, string) != None

# 求字符串中特殊字符的占比
def special_char_rate(str):
    special_char = "~!@#$%^&*()_+-*/<>,.[]\/"
    count = 0
    for char in special_char:
        count += str.count(char)
    return count / len(str)

# 判断是否异常文本
def is_abnormal_text(text, lenRange=(1,20), Threshold=0.4):
    """
    判断是否异常文本
    Args:
        text: 文本
        lenRange: 正常文本长度范围
        Threshold: 文本中异常字符的占比阈值，默认为0.4

    Returns:

    """
    if len(text) < lenRange[0] or len(text) > lenRange[1]:
        return True
    if special_char_rate(text) > Threshold:
        return True
    return False

# pandas随机采样读取csv
def random_sample_csv(self, csv_path, sample_size=1000, seed=None):
    """
    pandas随机采样读取csv
    Args:
        csv_path: csv文件路径
        sample_size: 采样大小
        seed: 随机种子

    Returns:

    """
    df = pd.read_csv(csv_path)
    df = df.sample(sample_size, random_state=seed)
    return df

# 抽取指定格式json里的字典key，返回list，json格式为{'xxxx':[{'key', 'value'}, {'key', 'value'}]}
def extract_json_key_data(x, k):
    """
   抽取指定格式json里的字典key，返回list，json格式为{'xxxx':[{'key', 'value'}, {'key', 'value'}]}
    Args:
        x: json字符串
        k: 'xxxx'字段

    Returns: 字典key的list

    """
    # list(json.loads(jd_data["Relate"][0])['related_search_list'][0].keys())[0]
    lst = []
    if type(x) == str:
        _ = json.loads(x)[k]
        # print(_)
        for i in range(len(_)):
            lst.append(f'''{list(_[i].keys())[0]}''')
            # print(list(_[i].keys())[0])
    return lst

# 抽取指定格式json里的字典value，返回list，json格式为{'xxxx':[{'key', 'value'}, {'key', 'value'}]}
def extract_json_value_data(x, k, field):
    """
    抽取指定格式json里的字典value，返回list，json格式为{'xxxx':[{'key', 'value'}, {'key', 'value'}]}
    Args:
        x: json字符串
        k: 'xxxx'字段
        field: 抽取的字典value对应的key

    Returns: 字典value的list

    """
    # list(json.loads(jd_data["Relate"][0])['related_search_list'][0].keys())[0]
    lst = []
    if type(x) == str:
        _ = json.loads(x)[k]
        # print(_)
        for i in range(len(_)):
            lst.append(f'''{_[i][field]}''')
            # print(_[i][field])
    return lst

# pandas dataframe的指定列去重
def drop_duplicate_column(df, column):
    """
    pandas dataframe的指定列去重
    Args:
        df: pandas dataframe
        column: 指定列

    Returns:

    """
    df[column] = df[column].astype('str')
    df.drop_duplicates(subset=column, keep='first', inplace=True)
    return df