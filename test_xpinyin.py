from xpinyin import Pinyin
import pinyin_utils

def get_pinyin_seq(c : str) -> str:
    p = Pinyin()
    pinyin = p.get_pinyin(c, splitter=' ', show_tone_marks=True)
    return pinyin_utils.translate_pucts(' '.join(list(map(pinyin_utils.to_numbered_tone, pinyin.split(' ')))))
