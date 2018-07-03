import pandas as pd
import numpy as np

def get_char_word_vec():
    df = pd.read_csv(r'./resource/char.only.sgns.zhihu.char.csv', skiprows=1, encoding='utf-8',
                     names=[str(x) for x in range(300)])
    #print(df.head())
    #print(df.shape)
    return df

def get_sim(a, b):
    A = df.loc[a].values
    B = df.loc[b].values

    num = np.sum(A.T * B)  # 若为行向量则 A * B.T
    denom = np.linalg.norm(A) * np.linalg.norm(B)
    cos = num / denom  # 余弦值
    sim = 0.5 + 0.5 * cos  # 归一化
    return sim

if __name__ == '__main__':
    df = get_char_word_vec()
    print(get_sim("吃", "喝"))
    print(get_sim("（", "）"))

