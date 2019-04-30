import tensorflow as tf

#tf.enable_eager_execution()

#dataset = tf.data.experimental.CsvDataset(
#   "data/f2018.csv",
#   [tf.string,
#    tf.string,
#    tf.string,
#    tf.string
#   ],
#   select_cols=[0,1,2,3]  # Only parse last three columns
#)

#for element in dataset:
#    print(element)

ITERATOR_BATCH_SIZE = 2
NR_EPOCHS = 3
train_path = 'data/f2018.csv'

dataset = tf.data.experimental.CsvDataset(
        train_path,
        [tf.string,
         tf.string,
         tf.string,
         tf.string
            ],
        header=True,
        field_delim=' '
        )

dataset = dataset.map(lambda *x: tf.convert_to_tensor(x))
dataset = dataset.batch(ITERATOR_BATCH_SIZE)

with tf.Session() as sess :
    for i in range (NR_EPOCHS):
        print('\nepochs',i)
        iterator = dataset.make_one_shot_iterator()
        next_element = iterator.get_next()
        while True:
            try:
                data_and_target = sess.run(next_element)
            except tf.errors.OutOfRangeError:
                break
            print("\n\n",data_and_target)
