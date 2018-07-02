import test_xpinyin, test_pypinyin

for unic in range(0x4e00, 0x9fbb):
    print(chr(unic) + ":" + test_pypinyin.get_pinyin_seq(chr(unic)))