import pandas as pd
import numpy as np

def sentence_to_two_neighbors(char: str, sentence: str, char_word_vec: pd.DataFrame):
    index = sentence.index(char)
    vec = np.array([])
    if index >= 1:
        prev = sentence[index - 1]
        vec = np.hstack((vec, char_word_vec.loc[prev].values))
    else:
        vec = np.hstack((vec, np.zeros(300)))

    if index <= len(sentence) - 2:
        next = sentence[index + 1]
        vec = np.hstack((vec, char_word_vec.loc[next].values))
    else:
        vec = np.hstack((vec, np.zeros(300)))
    return vec

def sentence_cleaner(sentence: str):
    to_delete = {" ", ""}
    to_replace = {
        "，": "。",
        "；": "。",


    }

def get_training_data(dictionary: dict, char: str, pinyins: list, char_word_vec: pd.DataFrame):
    # dictionary = { 'chang2': [ 'xxx', 'yyy' ... ], 'zhang3': [ 'xxxx', 'yyyy' ] }
    x_count = 0
    y_count = {}
    x_sentences = []
    # count how many training datas we have
    for pinyin in pinyins:
        y_count[pinyin] = 0
        x_count += len(dictionary[pinyin])

    x = np.zeros((x_count, 300 * 2))
    y = np.zeros((x_count, len(pinyins)))

    index = 0
    for y_index, pinyin in enumerate(pinyins):
        for sentence in dictionary[pinyin]:
            try:
                x[index, :] = sentence_to_two_neighbors(char, sentence, char_word_vec)
                y[index, :] = np.zeros(len(pinyins))
                y[index, y_index] = 1

                x_sentences.append(sentence)
                index += 1
                y_count[pinyin] += 1
            except KeyError as e:
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