# 列表元素去重
def remove_duplicate(lst):
    lst = list(set(lst))
    lst.sort()
    return lst

# 字符串拆散成列表
def str_to_list(str):
    str_list = []
    for i in range(len(str)):
        str_list.append(str[i])
    return str_list

# 列表中元素频次
def element_frequency(lst, sort_type=None):
    """
    列表中元素频次
    Args:
        lst: 输入列表
        sort_type: 排序类型，默认为None，不排序，asc为升序，desc为降序

    Returns:

    """
    dict = {}
    for i in lst:
        if i in dict.keys():
            dict[i] += 1
        else:
            dict[i] = 1
    if sort_type == 'desc':
        dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    elif sort_type == 'asc':
        dict = sorted(dict.items(), key=lambda x: x[1])
    else:
        dict = dict.items() # 返回的是一个列表
    return dict