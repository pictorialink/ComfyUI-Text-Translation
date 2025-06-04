

# 判断是否包含中文
def has_chinese_character(string):
    """
    判断字符串中是否包含中文字符
    :param string: 待判断的字符串
    :return: True如果字符串中至少包含一个中文字符，否则返回False
    """
    for char in string:
        if '\u4e00' <= char <= '\u9fff':
            return True
    return False

# 判断是否有英文之外的字符
def has_non_english_character(string):
    """
    判断字符串中是否包含英文之外的字符
    :param string: 待判断的字符串
    :return: True如果字符串中至少包含一个非英文字符，否则返回False
    """
    for char in string:
        if not (('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9') or char.isspace()):
            return True
    return False

