from two_neighbour_train import TwoNeighbourTrain
from word_vec import get_char_word_vec

class TwoNeighbourPredictGroup:

    model_group = {
        '长': {
            'model': None,
            'pinyins': ['chang2', 'zhang3'],
            'name': 'train_long_use_4_neighbour_focus',
            'n': 2,
            'use_focus': True
        },
        '冲': {
            'model': None,
            'pinyins': ['chong2', 'chong4'],
            'name': 'train_for_chong_4_neighbour-use_focus=True',
            'n': 2,
            'use_focus': True
        },
        '为': {
            'model': None,
            'pinyins': ['wei2', 'wei4'],
            'name': 'train_for_wei_8_neighbour-use_focus=True',
            'n': 4,
            'use_focus': True
        },
        '假': {
            'model': None,
            'pinyins': ['jia3', 'jia4'],
            'name': 'train_for_jia_8_neighbour-use_focus=True',
            'n': 4,
            'use_focus': True
        },
        '好': {
            'model': None,
            'pinyins': ['hao3', 'hao4'],
            'name': 'train_for_hao_10_neighbour-use_focus=False',
            'n': 5,
            'use_focus': False
        }
    }

    def __init__(self):
        word_vec = get_char_word_vec()
        for key, attributes in self.model_group.items():
            attributes['model'] =\
                TwoNeighbourTrain(attributes['name'], key, attributes['pinyins'], attributes['n'], attributes['use_focus'], word_vec)
            attributes['model'].prepare_model()


    def predict(self, char: str, sentence: str):
        return self.model_group[char]['model'].predict_sentence(sentence)


if __name__ == '__main__':
    group = TwoNeighbourPredictGroup()
    print(group.predict('冲', '不要冲着小孩子嚷嚷'))
    print(group.predict('冲', '对冲基金是什么啊'))
    print(group.predict('冲', '冲小李喊什么呢'))
    print(group.predict('冲', '冲小王喊什么呢'))
    print(group.predict('冲', '你为什么不冲着我来呢'))
    print(group.predict('冲', '嘿兄弟，你也网上冲浪呢？'))
    print(group.predict('冲', '你这人说话真冲。'))
    print(group.predict('冲', '味道很冲鼻子'))
    print(group.predict('冲', '什么味道这么冲啊'))
    print(group.predict('冲', '请你冲着我来'))
    print("")
    print(group.predict('假', '这是真的还是假的'))
    print(group.predict('假', '这叫做假说演绎法'))
    print(group.predict('假', '我还算有几天假'))
    print(group.predict('假', '今年我就没放几天假'))
    print(group.predict('假', '我今天放假'))
    print(group.predict('假', '这是群假党员'))
    print(group.predict('假', '印刷假钞是犯罪'))
    print(group.predict('假', '我想放假了'))
    print(group.predict('假', '我想请个假了'))
    print(group.predict('假', '请你批准我的假'))
    print(group.predict('假', '丈夫也可以休产假'))
    print(group.predict('假', '妻子可以休产假'))
    print(group.predict('假', '还有没有假放了？'))
    print(group.predict('假', '假借他人之手'))
    print(group.predict('假', '假作真时真亦假'))
    print(group.predict('假', '国庆有几天假'))
    print("")
    print(group.predict('好', '他就是好这口'))
    print(group.predict('好', '他好胜心很强'))
    print(group.predict('好', '他好喝酒，还好抽烟'))
    print(group.predict('好', '他是个好人'))
    print(group.predict('好', '这是好事'))
    print(group.predict('好', '不好'))
    print(group.predict('好', '好不好不是你说了算的'))
    print(group.predict('好', '好奇心把他引向深渊'))
    print(group.predict('好', '有好事群众围观'))
    print(group.predict('好', '好啊好啊'))
    print(group.predict('好', '有些网民好赌博'))
    print(group.predict('好', '有些网民好赌'))
    print(group.predict('好', '好吃懒做没好果子吃'))
    print(group.predict('好', '好的政策必然容易推行'))

