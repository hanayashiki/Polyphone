import pandas as pd
import numpy as np

def sentence_to_two_neighbors(char: str, sentence: str, char_word_vec: pd.DataFrame):
    return sentence_to_n_neighbors(1, char, sentence, char_word_vec)

def sentence_to_n_neighbors(n: int, char: str, sentence: str, char_word_vec: pd.DataFrame):
    index = sentence.index(char)
    vec = np.array([])
    for i in range(index - n, index + n + 1):
        if i < 0 or i >= len(sentence):
            vec = np.hstack((vec, np.zeros(300)))
        elif i != index:
            vec = np.hstack((vec, char_word_vec.loc[sentence[i]].values))
    return vec

def sentence_cleaner(sentence: str):
    to_delete = { " ", "", "—", "·" }
    to_replace = {
        "，": "。",
        "；": "。",
        "、": "。",
        "！": "。",
        "0": "零",
        "1": "一",
        "2": "二",
        "3": "三",
        "4": "四",
        "5": "五",
        "6": "六",
        "7": "七",
        "8": "八",
        "9": "九",
        "「": "“",
        "」": "”"
    }
    for c in to_delete:
        sentence = sentence.replace(c, "")
    for c, t in to_replace.items():
        sentence = sentence.replace(c, t)
    return sentence

def get_training_data(dictionary: dict, char: str, pinyins: list, char_word_vec: pd.DataFrame, n=1):
    # dictionary = { 'chang2': [ 'xxx', 'yyy' ... ], 'zhang3': [ 'xxxx', 'yyyy' ] }
    x_count = 0
    y_count = {}
    x_sentences = []
    # count how many training datas we have
    for pinyin in pinyins:
        y_count[pinyin] = 0
        x_count += len(dictionary[pinyin])

    x = np.zeros((x_count, 300 * 2 * n))
    y = np.zeros((x_count, len(pinyins)))

    index = 0
    for y_index, pinyin in enumerate(pinyins):
        for sentence in dictionary[pinyin]:
            sentence = sentence_cleaner(sentence)
            try:
                x[index, :] = sentence_to_n_neighbors(n, char, sentence, char_word_vec)
                y[index, :] = np.zeros(len(pinyins))
                y[index, y_index] = 1

                x_sentences.append(sentence)
                index += 1
                y_count[pinyin] += 1
            except KeyError as e:
                print(e)
                print("problem with %s: %s" % (char, sentence))
            except ValueError as e:
                print(e)
                print("problem with %s: %s" % (char, sentence))

    x = x[0: index, :]
    y = y[0: index, :]

    return {'x': x, 'y': y, 'y_count': y_count, 'x_sentences': np.array(x_sentences)}


if __name__ == '__main__':
    import word_vec
    char_vec = word_vec.get_char_word_vec()
    print(sentence_to_two_neighbors('长', '习近平长期执政', char_vec).shape)
    print(sentence_to_two_neighbors('长', '习近平长期执政', char_vec).shape)

    from resource.training_长 import data

    td = get_training_data(data, '长', ['chang2', 'zhang3'], char_vec)
    print(td)


    usual_puncts = set(list("，。！，、；：“”——……《》·123456789「」ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    in_index = []
    out_index = []
    char_set = set(char_vec.index.values.tolist())

    for punct in usual_puncts:
        if punct in char_set:
            in_index.append(punct)
        else:
            out_index.append(punct)

    print("in: " + str(in_index))
    print("out: " + str(out_index))

    print(sentence_to_n_neighbors(2, "长", "习近平长期执政", char_vec).shape)
    print(sentence_to_n_neighbors(2, "长", "平长", char_vec).shape)