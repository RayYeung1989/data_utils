import time_utils

# 测试获取时间戳
def test_get_time():
    print(time_utils.get_time())

# 测试获取当前时间，默认格式为：年-月-日 时:分:秒
def test_get_current_time():
    print(time_utils.get_current_time())

test_get_current_time()