from pypinyin import pinyin
import pinyin_utils
import itertools

def get_pinyin_seq(c : str) -> str:
    pinyin_res = list(itertools.chain.from_iterable(pinyin(c)))
    return pinyin_utils.translate_pucts(' '.join(list(map(pinyin_utils.to_numbered_tone, pinyin_res))))