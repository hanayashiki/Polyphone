from two_neighbour_predict import TwoNeighbourPredictGroup

from keras import backend as K
import tensorflow as tf

def export_all_models_cmd_line():
    commands = ""

    two_neighbour_group = TwoNeighbourPredictGroup()
    for key, model_dict in two_neighbour_group.model_group.items():
        model_weight = model_dict['model'].model_weight
        simple_model_name = f"{model_dict['alias']}-{str(2*model_dict['n'])}-{str(model_dict['use_focus']).lower()}.pb"
        export_model_base_dir = "./export_models/"
        commands += \
            "python ./keras_to_tensorflow/keras_to_tensorflow.py -input_model_file %s -output_model_file %s\n" \
            % (model_weight, export_model_base_dir + simple_model_name)

    return commands

if __name__ == '__main__':
    print(export_all_models_cmd_line())