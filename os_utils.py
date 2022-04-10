import os

# 获取脚本文件的当前路径
def get_current_path(upper_levels=0):
    """

    Args:
        upper_levels: 往上几级目录

    Returns: str

    """
    path = os.getcwd()
    for i in range(upper_levels):
        path = os.path.dirname(path)

    return path
