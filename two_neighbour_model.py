from keras.layers import Dense, Activation, Conv2D, Reshape, Input, multiply, RepeatVector
from keras.models import Sequential, Model
from keras.regularizers import l2

class TwoNeighbour:
    def __init__(self, name: str, pinyin: list, n=1, use_focus=False):
        self.pinyin = pinyin
        self.output_d = len(pinyin)
        self.name = name
        self.n = n
        self.use_focus = True

    def get_model(self):

        if self.use_focus:
            inputs = Input(shape=(300 * 2 * self.n, ))
            attention = Dense(2 * self.n, activation="sigmoid")(inputs)
            attention = RepeatVector(300)(attention)
            attention = Reshape(target_shape=(2 * self.n, 300))(attention)
            inputs_reshaped = Reshape(target_shape=(2 * self.n, 300))(inputs)
            attentioned = multiply([attention, inputs_reshaped])
            attentioned_reshaped = Reshape(target_shape=(300 * 2 * self.n,))(attentioned)
            output = Dense(units=self.output_d, activation="softmax")(attentioned_reshaped)

            return Model(inputs=inputs, outputs=output)

        else:
            model = Sequential()
            model.add(Dense(units=self.output_d, kernel_regularizer=l2(0.1),  activation="softmax", input_shape=(300 * 2 * self.n,)))
            return model

