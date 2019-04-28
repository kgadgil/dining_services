import tensorflow as tf

tf.enable_eager_execution()

dataset = tf.data.experimental.CsvDataset(
   "data/f2018.csv",
   [tf.float32,  # Required field, use dtype or empty tensor
    tf.constant([0.0], dtype=tf.float32),  # Optional field, default to 0.0
    tf.int32,  # Required field, use dtype or empty tensor
   ],
   select_cols=[1,2,3]  # Only parse last three columns
)

for element in dataset:
    print(element)
