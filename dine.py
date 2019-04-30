import tensorflow as tf
import numpy as np

#ITERATOR_BATCH_SIZE = 2
#NR_EPOCHS = 3
train_path = 'data/f2018.csv'

data = np.genfromtxt(train_path, dtype=None, delimiter=',', names=True) 
print(data)


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

