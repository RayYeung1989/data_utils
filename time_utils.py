import time

# 获取当前时间戳
def get_timestamp():
    return int(time.time())

# 获取当前时间，默认格式为：年-月-日 时:分:秒
def get_current_time(format='%Y-%m-%d %H:%M:%S'):
    """
    获取当前时间，默认格式为：年-月-日 时:分:秒
    Args:
        format: 指定当前时间的格式

    Returns: str

    """
    return time.strftime(format, time.localtime())


