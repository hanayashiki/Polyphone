from keras import backend as K
from tensorflow.python.framework import graph_util
from tensorflow.python.framework import graph_io

weight_file_path = 'path to your keras model'
net_model = load_model(weight_file_path)
sess = K.get_session()

constant_graph = graph_util.convert_variables_to_constants(sess, sess.graph.as_graph_def(), 'name of the output tensor')
graph_io.write_graph(constant_graph, 'output_folder_path', 'output.pb', as_text=False)
print('saved the constant graph (ready for inference) at: ', osp.join('output_folder_path', 'output.pb'))