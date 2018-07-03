from keras.layers import Dense, Activation
from keras.models import Sequential
from keras.regularizers import l2

class TwoNeighbour:
    def __init__(self, name: str, pinyin: list):
        self.pinyin = pinyin
        self.output_d = len(pinyin)
        self.name = name

    def get_model(self):
        model = Sequential()
        model.add(Dense(units=self.output_d, kernel_regularizer=l2(0.01),  activation="softmax", input_shape=(600,)))
        return model

