import time_utils
import os_utils
import data_process_utils

# 测试获取时间戳
def test_get_time():
    print(time_utils.get_time())

# 测试获取当前时间，默认格式为：年-月-日 时:分:秒
def test_get_current_time():
    print(time_utils.get_current_time())

# 测试获取脚本文件的当前路径
def test_get_current_path(upper_levels=0):
    print(os_utils.get_current_path(upper_levels))

# 测试json有多少层
def test_json_level(json_str):
    print(data_process_utils.json_level(json_str))

test_json_level('{"a":1,"b":2,"c":3}')