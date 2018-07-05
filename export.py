from two_neighbour_predict import TwoNeighbourPredictGroup

from keras import backend as K
import tensorflow as tf

def export_model(model_group: TwoNeighbourPredictGroup, char: str):
    model = model_group.get_model(char).weighted_model
    signature = tf.saved_model.signature_def_utils.predict_signature_def(
        inputs={'image': model.input}, outputs={'scores': model.output})

    builder = tf.saved_model.builder.SavedModelBuilder('./saved_models/%s/' % char)
    builder.add_meta_graph_and_variables(
        sess=K.get_session(),
        tags=[tf.saved_model.tag_constants.SERVING],
        signature_def_map={
            tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY:
                signature
        })
    builder.save()

if __name__ == '__main__':
    model_group = TwoNeighbourPredictGroup()
    export_model(model_group, '长')