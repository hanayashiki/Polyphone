test_cases =[
    ("你这个爱好很好啊", "ni3 zhe4 ge4 ai4 hao4 hen3 hao3 a5"),
    ("吃着火锅唱着歌", "chi1 zhe5 huo3 guo1 chang4 zhe5 ge1"),
    ("率领解决圆周率", "shuai4 ling3 jie3 jue2 yuan2 zhou1 lv4"),
    ("他每次出差差不多都要出点差错", "ta1 mei3 ci4 chu1 chai1 cha4 bu4 duo1 dou1 yao4 chu1 dian3 cha1 cuo4"),
    ("你这着真绝，让他干着急，又无法着手应付，心里老是悬着。",
        "ni3 zhe4 zhao1 zhen1 jue2 ,5 rang4 ta1 gan1 zhao2 ji2 ,5 you4 wu2 fa3 zhuo2 shou3 ying4 fu1 ,5 xin1 li3 lao3 shi1 xuan2 zhe5 .5"),
    ("他呀，就好这口", "ta1 ya5, jiu4 hao4 zhe4 kou3"),
    ("马家堡西路", "ma3 jia1 pu4 xi1 lu4"),
    ("长得好", "zhang3 de2 hao3"),
    ("椅子很长", "yi3 zi5 hen3 chang2"),
    ("长宽高", "chang2 kuan1 gao1"),
    ("到中国银行买白银行不行", "dao4 zhong1 guo2 yin2 hang2 mai3 bai2 yin2 xing2 bu4 xing2"),
    ("乒乓球拍卖完了", "ping1 pang1 qiu2 pai1 mai4 wan2 le5"),
    ("小明有一只羊", ""),
    ("熊一只是个孩子", ""),
    ("只要够牛逼", ""),
    ("只是不明白", ""),
    ("我要一只鸡", ""),
    ("只你一个不懂", ""),
    ("一只只松鼠", "")
]

import Levenshtein

import test_xpinyin, test_pypinyin

package_list = [test_xpinyin, test_pypinyin]

for c, pinyin in test_cases:
    print("\n\ncase: " + c)
    for package in package_list:
        print(package.__name__)

        expected = pinyin.replace(' ', '')
        actual = package.get_pinyin_seq(c).replace(' ', '')
        if len(expected) > 0:
            judge = expected == actual
            print(str(judge) + "\tactual   (%s)" % package.get_pinyin_seq(c) + " vs \n\t\texpected (%s)\t\t\t" % pinyin)
            print("\tedit distance: %d" % Levenshtein.distance(expected, actual))
        else:
            print("not judged" + "\tactual   (%s)" % package.get_pinyin_seq(c) + " vs \n\t\texpected (%s)\t\t\t" % pinyin)


