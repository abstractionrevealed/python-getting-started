import tensorflow as tf
if tf.test.is_built_with_cuda:
    print('TensorFlow built with CUDA')
else:
    raise SystemError('TensorFlow not built with CUDA')
device_name = tf.test.gpu_device_name()
if device_name != '/device:GPU:0':
    raise SystemError('GPU device not found')
print('Found GPU at: {}'.format(device_name))