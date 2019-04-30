import tensorflow as tf

tf.enable_eager_execution()

dataset = tf.data.experimental.CsvDataset(
   "data/f2018.csv",
   [tf.string,
    tf.string,
    tf.string,
    tf.string
   ],
   select_cols=[0,1,2,3]  # Only parse last three columns
)

for element in dataset:
    print(element)

