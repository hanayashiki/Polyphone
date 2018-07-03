import two_neighbour_train
from resource.training_长 import data

tn_training = two_neighbour_train.TwoNeighbourTrain('长', ['chang2', 'zhang3'])

tn_training.load_data(data)

print("train_x: %d, %d" % tn_training.train_x.shape)
print("train_y: %d, %d" % tn_training.train_y.shape)

print("test_x: %d, %d" % tn_training.test_x.shape)
print("test_y: %d, %d" % tn_training.test_y.shape)

print("train_senteces: " + str(tn_training.train_raw_sentences))


