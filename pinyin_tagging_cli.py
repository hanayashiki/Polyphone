import lcmc_parser

df, context_getter  = lcmc_parser.get_corpus()

char = input("标注的汉字：")
n_pinyin = int(input("有几种读音："))
pinyins = []

for i in range(n_pinyin):
    pinyins.append(input("读音 %d：" % (i + 1)))

print(pinyins)

char_sentences = context_getter(char)

data = {}

for pinyin in pinyins:
    data[pinyin] = []


for index, row in enumerate(char_sentences):
    print("%d / %d" % (index + 1, len(char_sentences)))
    print(row)
    print(row.find(char) * "口" + "^")
    print("读音是：" + ' '.join(["(%d): %s : %d" % (index + 1, pinyin, len(data[pinyin])) for index, pinyin in enumerate(pinyins)]))
    while True:
        try:
            pinyin_index = int(input())
            break
        except:
            print("try again")
    pinyin = pinyins[pinyin_index - 1]

    print("got %s for %s" % (pinyin, row))
    data[pinyin].append(row)
    print(data)