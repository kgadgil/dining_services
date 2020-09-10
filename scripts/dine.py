import tensorflow as tf
import numpy as np
import csv
import matplotlib.pyplot as plt

train_path = 'data/f2018.csv'

#Read CSV into list of lists
with open(train_path, 'r') as f:
    data = list(csv.reader(f, delimiter=','))
    #print(data[:3])
data_np = np.array(data)

#Convert last col (Qty Sold) to int data type
for item in data[1:]:       #start iterating from 2nd row in order to leave Qty Sold as string
    item[-1] = int(item[-1])
#print(data[:3]) #print first three rows

#Collect unique Major Groups, Family groups and menu item names
#Use set to get unique, list for list format
major_groups = list(set(data_np[1:-1:, 2]))
family_groups = list(set(data_np[1:-1, 1]))
menu_items = list(set(data_np[1:-1, 0]))
qty_sold = data_np[1:-1, 3]
#print('major groups\n', major_groups)
#print('family groups\n', family_groups)
#print('menu items\n', menu_items)

print(len(data_np[1:-1,0]))
print(len(qty_sold))

idx_menu = np.arange(len(data_np[1:-1,0]))
plt.bar(idx_menu, qty_sold)
plt.xlabel('Menu Items', fontsize=5)
plt.ylabel('Qty Sold', fontsize=5)
plt.xticks(idx_menu, data_np[1:-1,0], fontsize=5, rotation=30)
plt.title('Qty Sold per Menu Item')
plt.show()


#######################################
#######################################
#######################################
#data_tf = tf.convert_to_tensor(data)
#ITERATOR_BATCH_SIZE = 2
#NR_EPOCHS = 3

#data = np.genfromtxt(train_path, delimiter=',') 
#print(data)

#data_tf = tf.convert_to_tensor(data, preferred_dtype=tf.string)
#sess = tf.InteractiveSession()
#print(data_tf.eval())
#sess.close()

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

