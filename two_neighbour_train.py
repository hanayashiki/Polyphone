import two_neighbour_model
import two_neighbour_data
import word_vec
import utils
import json

import numpy as np

from keras.callbacks import ModelCheckpoint
from keras.callbacks import Callback

class TwoNeighbourTrain:
    def __init__(self, train_name, char: str, pinyins: list, n=1, use_focus=False, _word_vec=None):
        self.train_name = train_name
        self.char = char
        self.pinyins = pinyins
        self.model_weight = "traning_checkpoints/" + train_name + ".h5"
        self.cate_count = len(pinyins)
        self.n = n
        self.two_neighbour = two_neighbour_model.TwoNeighbour(char, pinyins, n=n, use_focus=use_focus)
        if type(_word_vec) != type(None):
            self.word_vec = _word_vec
        else:
            self.word_vec = word_vec.get_char_word_vec()

    def load_data(self, dictionary, train_split=0.7):
        self.data = two_neighbour_data.get_training_data(dictionary, self.char, self.pinyins, self.word_vec, self.n)
        # split the data into train and test, each class at the same ratio
        train_x_set = []
        train_y_set = []
        test_x_set = []
        test_y_set = []
        train_raw_sentences = []
        test_raw_sentences = []
        for cate_index, pinyin in enumerate(self.pinyins):
            cate_total_count = self.data['y_count'][pinyin]
            train_size = int(train_split * cate_total_count)
            cate_all_indexes = (self.data['y'] == utils.index_to_one_hot(cate_index, self.cate_count)).all(axis=1)
            train_x_set.append(self.data['x'][cate_all_indexes, :][0 : train_size])
            train_y_set.append(self.data['y'][cate_all_indexes, :][0 : train_size])
            test_x_set.append(self.data['x'][cate_all_indexes, :][train_size : ])
            test_y_set.append(self.data['y'][cate_all_indexes, :][train_size: ])
            train_raw_sentences.append(self.data['x_sentences'][cate_all_indexes][0 : train_size])
            test_raw_sentences.append(self.data['x_sentences'][cate_all_indexes][train_size: ])

        self.train_x = np.vstack(train_x_set)
        self.train_y = np.vstack(train_y_set)
        self.test_x = np.vstack(test_x_set)
        self.test_y = np.vstack(test_y_set)
        self.train_raw_sentences = np.hstack(train_raw_sentences)
        self.test_raw_sentences = np.hstack(test_raw_sentences)


    def store_training_info(self, dictionary: dict):
        # dictionary = {
        #     'epoch': 1,
        #     'val_acc': 0.1,
        #     'train_loss': 0.1,
        #     'val_loss': 0.1
        # }
        f = open('./training_info/' + self.train_name + ".json", 'w')
        f.write(json.dumps(dictionary))
        f.close()

    def get_training_info(self):
        try:
            f = open('./training_info/' + self.train_name + ".json", 'r')
            s = json.loads(f.read())
            f.close()
            return s
        except IOError as io:
            print(io)
            print("training_info/" + self.train_name + ".json " + " seems not to exist. use init values.")
            return {
                'epoch': 1,
                'val_acc': 0,
                'train_loss': 9999,
                'val_loss': 9999
            }


    def train(self):
        model = self.prepare_model()
        training_info = self.get_training_info()
        epoch_count = training_info['epoch']

        def on_epoch_end(epoch, log):
            nonlocal epoch_count
            epoch_count += 1
            self.store_training_info({
                'epoch': epoch_count,
                'val_acc': log['val_acc'],
                'train_loss': log['loss'],
                'val_loss': log['val_loss']
            })

        training_info_call_back = Callback()
        training_info_call_back.on_epoch_end = on_epoch_end

        model.fit(self.train_x, self.train_y,
                  batch_size=2, epochs=100,
                  validation_data=(self.test_x, self.test_y),
                  initial_epoch=epoch_count, callbacks=[ModelCheckpoint(self.model_weight), training_info_call_back])

    def prepare_model(self):
        model = self.two_neighbour.get_model()
        model.compile('sgd', loss='categorical_crossentropy', metrics=['accuracy'])
        print(model.summary())
        try:
            model.load_weights(self.model_weight)
        except:
            print("old weights %s not found. train from zero." % self.model_weight)
        self.weighted_model = model
        return model

    def predict_sentence(self, sentence):
        _sentence = two_neighbour_data.sentence_cleaner(sentence)
        vec = two_neighbour_data.sentence_to_n_neighbors(self.n, self.char, _sentence, self.word_vec)
        predict = self.weighted_model.predict(np.expand_dims(vec, axis=0))[0, :]
        return (sentence, predict.tolist(), self.pinyins[int(np.argmax(predict))])




if __name__ == '__main__':
    from resource.training_好 import data

    for use_focus in [False, True]:
        for i in range(1, 7):
            tn_train = TwoNeighbourTrain('train_for_hao_%d_neighbour-use_focus=%s' %  (2*i, str(use_focus)), '好', ['hao3', 'hao4'], i, use_focus=use_focus)
            tn_train.load_data(data)
            tn_train.train()

            tn_train.prepare_model()
            # print(tn_train.predict_sentence("有什么以中国人为主角的电影？"))
            # print(tn_train.predict_sentence("现在有多少人，为了孩子倾家荡产"))
            # print(tn_train.predict_sentence("勿以善小而不为，勿以恶小而为之"))
            # print(tn_train.predict_sentence("知其不可为而为之"))
            # print(tn_train.predict_sentence("心理学家研究行为科学"))
            # print(tn_train.predict_sentence("大象鼻子为什么那么长"))
            # print(tn_train.predict_sentence("党员应该为人民服务"))
            # print(tn_train.predict_sentence("男人应该为女人服务"))
            # print(tn_train.predict_sentence("男人应该为女人服务"))
            # print(tn_train.predict_sentence("这到底是为什么"))

    # print(tn_train.predict_sentence("你长得很高啊！"))
    # print(tn_train.predict_sentence("路还很长"))
    # print(tn_train.predict_sentence("刘翔是一个长跑运动员"))
    # print(tn_train.predict_sentence("金正恩将长时间担任朝鲜领导人"))
    # print(tn_train.predict_sentence("为什么说“少壮不努力长大学会计”？"))
    # print(tn_train.predict_sentence("长"))



