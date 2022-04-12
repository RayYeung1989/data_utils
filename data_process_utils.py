import pandas as pd
import json

# json有多少层
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
def random_sample_csv(csv_path, sample_size=1000, seed=None):
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


