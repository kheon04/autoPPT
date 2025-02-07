import re

def findNames(text):
    """
    숫자 또는 숫자 범위와 곡명을 추출하는 정규식
    1. 2. 또는 001 002으로 표현된 line을, 제목만 추출 후 list로 반환
    """
    return re.findall(r'\d+(?:-\d+)?\.?\s(.*?)\s[A-Z]', text)