

import re

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


def has_non_english_character(string):
    """
    检查字符串中是否包含非英文字符。
    允许的字符包括：英文、数字、常见标点、空格和 Emoji。
    """
    # 定义允许的字符范围
    allowed_pattern = re.compile(
        r'^[a-zA-Z0-9\s\.,!?;:\'"@#$%^&*()_+=\-[\]{}|\\<>/`~'
        r'\U0001F600-\U0001F64F'  # Emoticons
        r'\U0001F300-\U0001F5FF'  # Misc Symbols and Pictographs
        r'\U0001F680-\U0001F6FF'  # Transport & Map
        r'\U0001F1E0-\U0001F1FF'  # Flags (iOS)
        r']+$',
        re.UNICODE
    )
    
    return not bool(allowed_pattern.fullmatch(string))

