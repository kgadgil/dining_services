import tensorflow as tf
import numpy as np
#from io import StringIO
import csv

#ITERATOR_BATCH_SIZE = 2
#NR_EPOCHS = 3
train_path = 'data/f2018.csv'

data = np.genfromtxt(train_path, delimiter=',') 
print(data)

data_tf = tf.convert_to_tensor(data, preferred_dtype=tf.string)
sess = tf.InteractiveSession()
print(data_tf.eval())
sess.close()

#tf.enable_eager_execution()

#dataset = tf.data.experimental.CsvDataset(
#   train_path,
#   [tf.string,
#    tf.string,
#    tf.string,
#    tf.string
#   ],
#   select_cols=[0,1,2,3]  # Only parse last three columns    
#)

#for element in dataset:
#    print(element)

