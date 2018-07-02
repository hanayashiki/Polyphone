import pandas as pd
import re


def get_c_frequency() -> pd.DataFrame:
    df = pd.read_csv('resource/c_frequency.txt', sep='\s+', header=None, names=['c', 'frequency'])
    df = df.loc[df['c'].apply(lambda c: re.match(r"[\u4e00-\u9fa5]", c) != None)]
    return df

def get_polyphones() -> pd.DataFrame:
    df = pd.read_csv('resource/frequent_polyphones.txt',
                     sep='whatever', engine='python', header=None, names=['origin'], squeeze=False)
    df = df.loc[df['origin'].apply(lambda c: re.match(r"^[0-9]+\..*", c) != None)]

    def get_pinyins(line: str) -> list:
        l = re.findall(r"[a-zāáǎàōóǒòêēéěèīíǐìūúǔùǖǘǚǜüńňǹɑɡ]+", line)
        assert len(l) > 0
        return l

    df['pinyins'] = df['origin'].apply(get_pinyins)
    df['c'] = df['origin'].apply(lambda c: re.search(r"^[0-9]+\.\s*([\u4e00-\u9fa5])", c).group(1))

    return df[['c', 'pinyins']]

def get_c_pinyin_freq():
    return pd.merge(get_c_frequency(), get_polyphones(), on=['c'], how='outer')

def get_important_polyphones():
    return ['的', '着', '得', '过', '和', '好', '中', '都',
            '什', '种', '发', '当', '给', '作', '正', '分',
            '几', '相', '处', '阿', '啊', '娜', '服', '度',
            '空', '量', '背', '数', '塞', '假', '冲', '差',
            '号', '堡', '为', '长']


if __name__ == '__main__':
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    # print(get_c_frequency().head(1000))
    # print(get_polyphones())
    print(get_c_pinyin_freq())
