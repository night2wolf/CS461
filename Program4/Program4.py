from __future__ import absolute_import, division, print_function, unicode_literals
import functools
import tensorflow as tf
import numpy as np
import pandas as pd
# import training and test data
train_file_path = pd.read_csv("pulsar_stars_train.csv")
test_file_path = pd.read_csv("pulsar_stars_test.csv")
# look at the datatypes in case we need to convert anything
train_file_path.head()
train_file_path.dtypes
# get what class weare training on, convert the data and batch it.
target = train_file_path.pop('target_class')
dataset = tf.data.Dataset.from_tensor_slices(
    (train_file_path.values, target.values))
train_dataset = dataset.shuffle(len(train_file_path)).batch(64)

# the A.I. model and its optimization / backpropagation strategy


def get_compiled_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model


# train the model
model = get_compiled_model()
model.fit(train_dataset, epochs=15)
# import the test data the same as the training data, batch it and test it
test_target = test_file_path.pop('target_class')
te_dataset = tf.data.Dataset.from_tensor_slices(
    (test_file_path.values, test_target.values))
test_dataset = te_dataset.shuffle(len(test_file_path)).batch(64)
test_loss, test_accuracy = model.evaluate(test_dataset)
# display our test output
print('\n\nTest Loss {}, Test Accuracy {}'.format(test_loss, test_accuracy))
# import the validation data set and convert it / batch it in the same method
validation_file_path = pd.read_csv("pulsar_stars_eval.csv")
target_eval = validation_file_path.pop('target_class')
ev_dataset = tf.data.Dataset.from_tensor_slices(
    (validation_file_path.values, target_eval.values))
eval_dataset = ev_dataset.shuffle(len(test_file_path)).batch(64)
# evaluate the model and display the results
eval_loss, eval_accuracy = model.evaluate(eval_dataset)

print('\n\nValidation Loss {}, Validation Accuracy {}'.format(
    eval_loss, eval_accuracy))
