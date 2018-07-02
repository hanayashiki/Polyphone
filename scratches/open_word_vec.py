import re

f = open(r'D:\BaiduNetdiskDownload\sgns.zhihu.char\sgns.zhihu.char', 'r')
g = open(r'./resource/char.only.sgns.zhihu.char.csv', 'w', encoding='utf-8')



i = 0
for line in f:
    #print(line.split(' '))
    l = line.strip().split(' ')
    if re.match(r'^[a-zA-Z，。？（）\u4e00-\u9fbb]$', l[0]):
        g.write(','.join(l) + '\n')
        i += 1


print("generated %d lines" % i)
