import re
import pandas as pd
import os

def parse_lcmc_line(line: str):
    match = re.search("<s n=\"[0-9]+\">(.+)</s>", line)

    if match:
        raw_xml_sentence = match.group(1)
        words_match = re.findall("<[cw] POS=\"[a-z]*\">(.+?)</[cw]>", raw_xml_sentence)
        return ''.join(words_match)
        #print(words_match)
    return None

def parse_lcmc_corpus(char_files: list, pinyin_files: list) -> pd.DataFrame:
    stacked = []
    for char_file, pinyin_file in zip(char_files, pinyin_files):
        for file in [char_file, pinyin_file]:
            char_df = pd.read_csv(file, sep='whatver', encoding='utf-8', engine='python')
            char_df_parsed = char_df.apply(lambda s : parse_lcmc_line(s.values.tolist()[0]), axis=1)
            char_df_parsed = char_df_parsed.loc[char_df_parsed.isna() == False]
            stacked.append(char_df_parsed)
    return pd.concat(stacked, axis=0)

def get_corpus() -> tuple:
    char_files = os.listdir('resource/2474/2474/Lcmc/data/character')
    char_files.sort()
    char_files = [os.path.join('resource/2474/2474/Lcmc/data/character', x).replace('\\', '/') for x in char_files]
    pinyin_files = os.listdir('resource/2474/2474/Lcmc/data/pinyin')
    pinyin_files.sort()
    pinyin_files = [os.path.join('resource/2474/2474/Lcmc/data/pinyin', x).replace('\\', '/') for x in pinyin_files]

    lcmc_df = parse_lcmc_corpus(
        char_files,
        pinyin_files
    )

    def get_char_context(char: str):
        return lcmc_df.loc[lcmc_df.str.find(char) > -1]

    lcmc_df.get_char_context = get_char_context

    return lcmc_df, get_char_context

if __name__ == '__main__':
    parse_lcmc_line("""\
    <s n="0066"> <w POS="n">jing3guan1</w> <w POS="nr">yin3</w> <w POS="nr">zhi4cheng2</w> <w POS="v">jie4shao4</w> <w POS="u">le5</w> <w POS="r">ta1men5</w> <w POS="u">de5</w> <w POS="n">qing2kuang4</w> <c POS="ew">。</c> </s>
    """)

    char_files = os.listdir('resource/2474/2474/Lcmc/data/character')
    char_files.sort()
    char_files = [os.path.join('resource/2474/2474/Lcmc/data/character', x).replace('\\', '/') for x in char_files]
    pinyin_files = os.listdir('resource/2474/2474/Lcmc/data/pinyin')
    pinyin_files.sort()
    pinyin_files = [os.path.join('resource/2474/2474/Lcmc/data/pinyin', x).replace('\\', '/') for x in pinyin_files]

    lcmc_df = parse_lcmc_corpus(
        char_files,
        pinyin_files
    )

    contains_chong = lcmc_df.loc[lcmc_df.str.find('冲') > -1]
    print(contains_chong)