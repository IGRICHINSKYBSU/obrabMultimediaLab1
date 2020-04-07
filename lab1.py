import datetime
from keras import datasets, layers, models, losses
from keras.callbacks import TensorBoard

def createModel():
  model = models.Sequential()
  model.add(layers.Flatten(input_shape=(32, 32, 3)))
  model.add(layers.Dense(128, activation='relu'))
  model.add(layers.Dense(128, activation='relu'))
  model.add(layers.Dense(64, activation='relu'))
  model.add(layers.Dense(64, activation='relu'))
  model.add(layers.Dense(10, activation='softmax'))
  model.compile(optimizer='adam',
  loss=losses.sparse_categorical_crossentropy,
  metrics=['accuracy'])
  print(model.summary())
  return model

def main():
  (train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
  train_images, test_images = train_images / 255.0, test_images / 255.0
  model = createModel()
  log_dir = 'logs/{}'.format(datetime.datetime.now())
  tensor_board = TensorBoard(log_dir=log_dir, histogram_freq=1)
  history = model.fit(train_images, train_labels, epochs=10, callbacks=[tensor_board],
  validation_data=(test_images, test_labels))
  test = model.evaluate(train_images[0], test_labels[0])
  print(test)

main()
